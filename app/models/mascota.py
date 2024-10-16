from app import db

class Mascota(db.Model):
    __tablename__ = 'Mascota'
    
    id_mascota = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(20), nullable=False)
    peso = db.Column(db.Numeric(5,2), nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    foto = db.Column(db.String(250), nullable=False)
    Usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    especie_id_especie = db.Column(db.Integer, db.ForeignKey('especie.id_especie'), nullable=False)
    
    usuario = db.relationship('Usuario', backref='mascotas')
    especie = db.relationship('Especie', backref='mascotas')
