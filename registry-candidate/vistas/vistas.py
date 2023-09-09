from flask import request
from flask_restful import Resource

from modelos import db, Candidato


class VistaCandidato(Resource):

    def post(self):

        candidato = Candidato(
            nombre=request.json["nombre"],
            experiencia=request.json["experiencia"],
            telefono=request.json["telefono"]
        )

        db.session.add(candidato)
        db.session.commit()

        return {"mensaje": "Candidato creado", "result": True}
