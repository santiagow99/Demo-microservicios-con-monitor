from flask import request
from sqlalchemy import func
from flask_restful import Resource
from modelos import db, Candidato, CandidatoSchema
from collections import Counter

candidato_schema = CandidatoSchema()

class VistaGrupos(Resource):
    def get(self):
        candidatos = Candidato.query.order_by(func.random()).limit(3).all()
        return [candidato_schema.dump(candidato) for candidato in candidatos]
    
class VistaAnaliticas(Resource):
    def get(self):
        candidatos = Candidato.query.all()
        cantidad_candidatos = len(candidatos)
        profesiones = dict(Counter([x.profesion for x in candidatos]))
        min_edad = min([x.edad for x in candidatos])
        max_edad = max([x.edad for x in candidatos])
        return f"""Total candidatos: {cantidad_candidatos}. Profesiones: {profesiones}. Rango de dad candidatos: {min_edad} - {max_edad}"""


