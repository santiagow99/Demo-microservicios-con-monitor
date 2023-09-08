from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    profesion = db.Column(db.String(128))
    edad = db.Column(db.Integer)
    telefono = db.Column(db.String(50))


class CandidatoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Candidato
        include_relationships = True
        load_instance = True
    id = fields.String()
    nombre = fields.String()
    profesion = fields.String()
    edad = fields.Integer()
    telefono = fields.String()

    