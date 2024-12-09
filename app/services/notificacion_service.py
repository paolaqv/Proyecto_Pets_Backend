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

        # Configuración específica según el tipo
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

        # Log para verificar datos enviados al repositorio
        print(f"[Servicio] Datos finales para el repositorio: mensaje={mensaje}, fecha_inicio={fecha_inicio}, fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}, actividad_id={actividad_id}, usuario_id={usuario_id}")

        # Crear la notificación en el repositorio
        nueva_notificacion = NotificacionRepository.crear_notificacion(
            mensaje=mensaje,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            intervalo=intervalo,
            unidad_intervalo=unidad_intervalo,
            actividad_id=actividad_id,
            usuario_id=usuario_id
        )
        print(f"[Servicio] Notificación creada: {nueva_notificacion}")

        return nueva_notificacion