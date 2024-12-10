from app.repositories.notificacion_repository import NotificacionRepository
from datetime import datetime, timedelta
from twilio.rest import Client
from app.models import Notificacion, Usuario
from apscheduler.schedulers.background import BackgroundScheduler
from app import create_app 
from app import db

# Configura tus credenciales de Twilio
ACCOUNT_SID = config('ACCOUNT_SID')
AUTH_TOKEN = config('AUTH_TOKEN')
FROM_WHATSAPP = config('FROM_WHATSAPP')
PREFIJO = config('PREFIJO')

class NotificacionService:
    
    @staticmethod
    def enviar_notificacion(numero, mensaje,es_repetitiva=False, fecha_fin=None):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        to_whatsapp = f'whatsapp:{PREFIJO}{numero}'
         
        # Mensaje personalizado 
        if not es_repetitiva:
            mensaje_personalizado = f"""
            🌟 ¡Hola! 🌟 
            Petcare te recuerda: 🐾
            📅 {mensaje}
                        
            Gracias por confiar en Petcare. ¡Que tengas un excelente día! 😊
            """
        else:
            # Mensaje personalizado para notificaciones repetitivas
            mensaje_personalizado = f"""
                🌟 ¡Hola! 🌟 
                Petcare te recuerda: 🐾
                📅 {mensaje}
                ⏰ Esta notificación se repetirá hasta el {fecha_fin.strftime('%d de %B')}.
                            
                Gracias por confiar en Petcare. ¡Que tengas un excelente día! 😊
            """

        try:
            message = client.messages.create(
                body=mensaje_personalizado,
                from_=FROM_WHATSAPP,
                to=to_whatsapp
            )
            print(f"Mensaje enviado con SID: {message.sid}")
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    @staticmethod
    def enviar_notificaciones_automaticas():
        app = create_app()  

        with app.app_context():
            ahora = datetime.now()

            notificaciones = Notificacion.query.filter(
                Notificacion.estado == "Activo",
                Notificacion.fecha_inicio <= ahora
            ).all()

            for notificacion in notificaciones:
                usuario = Usuario.query.get(notificacion.Usuario_id_usuario)
                if usuario:
                    try:
                        es_repetitiva = notificacion.intervalo is not None and notificacion.fecha_fin is not None

                           # Enviar mensaje 
                        NotificacionService.enviar_notificacion(
                            numero=usuario.telefono,
                            mensaje=notificacion.mensaje,
                            es_repetitiva=es_repetitiva,
                            fecha_fin=notificacion.fecha_fin
                        )

                        # Manejo de estado y fechas
                        if es_repetitiva:
                            # Si esta en intervalo permitido
                            if ahora + timedelta(minutes=notificacion.intervalo) <= notificacion.fecha_fin:
                                notificacion.fecha_inicio += timedelta(minutes=notificacion.intervalo)
                            else:
                                notificacion.estado = "Enviado"  # Marcar si supera la fecha_fin
                        else:
                            notificacion.estado = "Enviado"

                        db.session.commit()  # Guardar cambios
                    except Exception as e:
                        print(f"Error al enviar notificación {notificacion.id_notificacion}: {e}")


    @staticmethod
    def crear_notificacion(data):
        print(f"[Servicio] Datos recibidos: {data}")

        # Extraer datos del payload (front)
        mensaje = data.get('mensaje')
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        intervalo = data.get('intervalo')
        unidad_intervalo = data.get('unidad_intervalo')
        actividad_id = data.get('Actividad_id_actividad')
        usuario_id = data.get('Usuario_id_usuario')

        # Validar campos obligatorios comunes
        if not mensaje or not fecha_inicio or not actividad_id or not usuario_id:
            raise ValueError("Campos obligatorios faltantes: mensaje, fecha_inicio, actividad_id, usuario_id")
        
        print(f"[Servicio] Campos obligatorios validados: mensaje={mensaje}, fecha_inicio={fecha_inicio}, actividad_id={actividad_id}, usuario_id={usuario_id}")

        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%dT%H:%M")
            if fecha_fin:
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%dT%H:%M")
        except ValueError:
            raise ValueError("Formato de fecha/hora inválido. Use: 'YYYY-MM-DDTHH:MM'.")

        if data.get('type') == 'repeat':
            # Validar campos obligatorios para "repetir"
            if not intervalo or not unidad_intervalo or not fecha_fin:
                raise ValueError("Campos obligatorios faltantes para notificación 'repetir': intervalo, unidad_intervalo y fecha_fin.")
            if intervalo <= 0:
                raise ValueError("El intervalo debe ser mayor a 0.")

            print(f"[Servicio] Notificación 'repetir': fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}")
        else:  # Caso "una vez"
            fecha_fin = None
            intervalo = None
            unidad_intervalo = None
            print(f"[Servicio] Notificación 'una vez': fecha_inicio={fecha_inicio}, mensaje={mensaje}")

        print(f"[Servicio] Datos finales para el repositorio: mensaje={mensaje}, fecha_inicio={fecha_inicio}, fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}, actividad_id={actividad_id}, usuario_id={usuario_id}")

        nueva_notificacion = NotificacionRepository.crear_notificacion(
            mensaje=mensaje,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            intervalo=intervalo,
            unidad_intervalo="minutes" if unidad_intervalo == "minutos" else unidad_intervalo,
            actividad_id=actividad_id,
            usuario_id=usuario_id
        )
        print(f"[Servicio] Notificación creada: {nueva_notificacion}")

        return nueva_notificacion