from flask import request
from flask_restful import Resource

import pika
import redis

redis_client = redis.StrictRedis(
    host='localhost', port=6379, db=0, decode_responses=True)


class VistaServicio(Resource):

    def post(self):
        service_name_pattern = request.json['servicio_name'] + '*'
        servicios_keys = redis_client.keys(service_name_pattern)
        servicios_ip = redis_client.mget(servicios_keys)
        return {"servicios_ip": servicios_ip}


class VistaCandidato(Resource):

    def post(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('172.17.0.2'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        servicio_info = ['rem', 2]
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=request.json['nombre'])

        connection.close()

        return {'mesage': 'mensage delivered', 'result': True}


class VistaSave(Resource):

    def post(self):
        redis_client.set(request.json['nombre'], request.json['ip'], ex=5)
        return {'mesage': 'data persisted on redis', 'result': True}

    def get(self):
        keys = redis_client.keys('dan*')
        valued = redis_client.mget(keys)
        return keys
