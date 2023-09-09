from flask import request
from flask_restful import Resource

import pika

from modelos import db, Candidato


class VistaCandidato(Resource):

    def post(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('172.17.0.2'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')

        connection.close()

        return {'mesage': 'mensage delivered', 'result': True}
