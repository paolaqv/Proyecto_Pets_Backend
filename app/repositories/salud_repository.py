from app import db
from app.models import Salud

class SaludRepository:

    @staticmethod
    def add_salud(data):
        nueva_salud = Salud(
            fecha=data.get('fecha'),
            observacion=data.get('observacion'),
            archivo=data.get('archivo'),
            tipo_salud_id_tipo_salud=data.get('tipo_salud_id_tipo_salud'),
            mascota_id_mascota=data.get('mascota_id_mascota')
        )
        db.session.add(nueva_salud)
        db.session.commit()
        return nueva_salud

    @staticmethod
    def get_salud_by_id(salud_id):
        return Salud.query.get(salud_id)

    @staticmethod
    def update_salud(salud_id, data):
        salud = Salud.query.get(salud_id)
        if salud:
            salud.fecha = data.get('fecha')
            salud.observacion = data.get('observacion')
            salud.archivo = data.get('archivo')
            salud.tipo_salud_id_tipo_salud = data.get('tipo_salud_id_tipo_salud')
            salud.mascota_id_mascota = data.get('mascota_id_mascota')
            db.session.commit()
        return salud

    @staticmethod
    def delete_salud(salud_id):
        salud = Salud.query.get(salud_id)
        if salud:
            db.session.delete(salud)
            db.session.commit()
        return salud
