from app import db

class Mascota(db.Model):
    __tablename__ = 'Mascota'
    
    id_mascota = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.TIMESTAMP, nullable=False)  # Mantén TIMESTAMP si es necesario, pero puedes considerar usar Date
    raza = db.Column(db.String(20), nullable=False)
    peso = db.Column(db.Numeric(5, 2), nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    foto = db.Column(db.String(250), nullable=True)  # Si es necesario manejar imágenes, podrías almacenar una URL
    
    # Relación con la tabla Usuario (ForeignKey)
    Usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    usuario = db.relationship('Usuario', backref='mascotas')  # Relación con el modelo Usuario

    # Relación con la tabla Especie (ForeignKey)
    especie_id_especie = db.Column(db.Integer, db.ForeignKey('especie.id_especie'), nullable=False)
    especie = db.relationship('Especie', backref='mascotas')  # Relación con el modelo Especie

    def __repr__(self):
        return f"<Mascota {self.nombre} ({self.raza})>"

    # Método para convertir los datos a formato JSON
    def to_dict(self):
        return {
            "id_mascota": self.id_mascota,
            "nombre": self.nombre,
            "fecha_nacimiento": self.fecha_nacimiento.strftime('%Y-%m-%d') if self.fecha_nacimiento else None,  # Convertir fecha a string si es necesario
            "raza": self.raza,
            "peso": str(self.peso),  # Convertir el valor decimal a string para evitar problemas de serialización
            "sexo": self.sexo,
            "descripcion": self.descripcion,
            "foto": self.foto,
            "Usuario_id_usuario": self.Usuario_id_usuario,
            "especie_id_especie": self.especie_id_especie
        }

