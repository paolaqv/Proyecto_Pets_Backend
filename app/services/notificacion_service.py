from app.repositories.notificacion_repository import NotificacionRepository
from datetime import datetime

class NotificacionService:

    @staticmethod
    def crear_notificacion(data):
        print(f"[Servicio] Datos recibidos: {data}")
        # Extraer datos del payload
        mensaje = data.get('mensaje')
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        intervalo = data.get('intervalo')
        unidad_intervalo = data.get('unidad_intervalo')
        recordatorio_tipo = data.get('recordatorio_tipo')
        recordatorio_cantidad = data.get('recordatorio_cantidad')
        recordatorio_hora = data.get('recordatorio_hora')
        actividad_id = data.get('Actividad_id_actividad')
        usuario_id = data.get('Usuario_id_usuario')

        # Validar campos obligatorios comunes
        if not mensaje or not fecha_inicio or not actividad_id or not usuario_id:
            raise ValueError("Campos obligatorios faltantes: mensaje, fecha_inicio, actividad_id, usuario_id")
        
        print(f"[Servicio] Campos obligatorios validados: mensaje={mensaje}, fecha_inicio={fecha_inicio}, actividad_id={actividad_id}, usuario_id={usuario_id}")

        # Validar formato de fecha/hora
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%dT%H:%M")
            if fecha_fin:
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%dT%H:%M")
        except ValueError:
            raise ValueError("Formato de fecha/hora inválido. Use: 'YYYY-MM-DDTHH:MM'.")

        if data.get('type') == 'repeat':
            if not intervalo or not unidad_intervalo or not fecha_fin:
                raise ValueError("Campos obligatorios faltantes para notificación 'repetir': intervalo, unidad_intervalo y fecha_fin.")
            if intervalo <= 0:
                raise ValueError("El intervalo debe ser mayor a 0.")

            print(f"[Servicio] Notificación 'repetir': fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}")

        else:  # Caso "una vez"
            # Solo establece en None si realmente no se están enviando
            intervalo = intervalo if intervalo else None
            unidad_intervalo = unidad_intervalo if unidad_intervalo else None
            fecha_fin = fecha_fin if fecha_fin else None
            print(f"[Servicio] Notificación 'una vez': fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}")


        if recordatorio_tipo == "before":
            if not recordatorio_cantidad or not recordatorio_hora:
                raise ValueError("Campos obligatorios faltantes para notificación 'antes de': recordatorio_cantidad y recordatorio_hora.")
            if recordatorio_cantidad <= 0:
                raise ValueError("La cantidad del recordatorio debe ser mayor a 0.")
            print(f"[Servicio] Recordatorio 'antes de': recordatorio_cantidad={recordatorio_cantidad}, recordatorio_hora={recordatorio_hora}")

        else:  # Caso "en la hora"
            recordatorio_cantidad = None
            recordatorio_hora = None
        print(f"[Servicio] Recordatorio 'en la hora': recordatorio_cantidad={recordatorio_cantidad}, recordatorio_hora={recordatorio_hora}")

        # Log para verificar datos enviados al repositorio
        print(f"[Servicio] Datos finales para el repositorio: mensaje={mensaje}, fecha_inicio={fecha_inicio}, fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}, recordatorio_tipo={recordatorio_tipo}, recordatorio_cantidad={recordatorio_cantidad}, recordatorio_hora={recordatorio_hora}, actividad_id={actividad_id}, usuario_id={usuario_id}")

        # Crear la notificación en el repositorio
        nueva_notificacion = NotificacionRepository.crear_notificacion(
            mensaje=mensaje,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            intervalo=intervalo,
            unidad_intervalo=unidad_intervalo,
            recordatorio_tipo=recordatorio_tipo,
            recordatorio_cantidad=recordatorio_cantidad,
            recordatorio_hora=recordatorio_hora,
            actividad_id=actividad_id,
            usuario_id=usuario_id
        )
        print(f"[Servicio] Notificación creada: {nueva_notificacion}")


        return nueva_notificacion
