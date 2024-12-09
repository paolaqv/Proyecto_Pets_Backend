from app import db
from app.models import Notificacion

class NotificacionRepository:

    @staticmethod
    def crear_notificacion(
        mensaje, fecha_inicio, fecha_fin, intervalo, unidad_intervalo,
        actividad_id, usuario_id
    ):
        print(f"Datos recibidos en repositorio: fecha_fin={fecha_fin}, intervalo={intervalo}, unidad_intervalo={unidad_intervalo}")

        nueva_notificacion = Notificacion(
            mensaje=mensaje,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,  # Debe recibir el valor del servicio
            intervalo=intervalo,  # Debe recibir el valor del servicio
            unidad_intervalo=unidad_intervalo,  # Debe recibir el valor del servicio
            Actividad_id_actividad=actividad_id,
            Usuario_id_usuario=usuario_id
        )

        db.session.add(nueva_notificacion)
        db.session.commit()
        return nueva_notificacion
