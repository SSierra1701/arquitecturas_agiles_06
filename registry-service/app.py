from flask import Flask
from flask_restful import Api

from vistas import VistaServicio, VistaCandidato

import redis
import pika

from flask_executor import Executor
from flask_coney import Coney

# ----------> FLASK APP CONFIG
app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["CONEY_BROKER_URI"] = "amqp://guest:guest@172.17.0.2"


api = Api(app)

# ----------> REDIS CONFIG

api.add_resource(VistaServicio, '/servicios-ip')

api.add_resource(VistaCandidato, '/hello')

# -------

coney = Coney(app)


@coney.queue(queue_name="hello")
def process_queue(ch, method, props, body):
    # do something with body
    rere = body
    print(type(rere))
    print(body.decode('utf-8'), flush=True)


""" class BackgroundRunner:
    def __init__(self, executor):
        self.executor = executor
        redis_client = redis.StrictRedis(
            host='localhost', port=6379, db=0, decode_responses=True)

    redis_client = redis.StrictRedis(
        host='localhost', port=6379, db=0, decode_responses=True)
    # ----------> SUSCRIPCION TOPICO REGISTRAR SERVICO

    def registrarServicio(ch, method, properties, body):
        servicio_information = body.split(",")
        redis_client.set(
            servicio_information[0], servicio_information[1], ex=2)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('172.17.0.2'))

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=registrarServicio)

    channel.basic_qos(prefetch_count=1)

    channel.start_consuming() """
