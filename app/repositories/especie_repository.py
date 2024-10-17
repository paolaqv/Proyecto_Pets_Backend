from app import db
from app.models import Especie

class EspecieRepository:

    @staticmethod
    def add_especie(data):
        nueva_especie = Especie(
            especie=data.get('especie')
        )
        db.session.add(nueva_especie)
        db.session.commit()
        return nueva_especie

    @staticmethod
    def get_especie_by_id(especie_id):
        return Especie.query.get(especie_id)

    @staticmethod
    def update_especie(especie_id, data):
        especie = Especie.query.get(especie_id)
        if especie:
            especie.especie = data.get('especie')
            db.session.commit()
        return especie

    @staticmethod
    def delete_especie(especie_id):
        especie = Especie.query.get(especie_id)
        if especie:
            db.session.delete(especie)
            db.session.commit()
        return especie
