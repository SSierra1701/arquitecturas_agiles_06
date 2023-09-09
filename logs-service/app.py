from flask import Flask
from flask_restful import Api

from modelos import db
from vistas import VistaCandidato

from flask_migrate import Migrate

import pika

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost:5432/arquitectura"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

# app_context = app.app_context()
# app_context.push()

db.init_app(app)

# migrate = Migrate(app, db)

api = Api(app)

api.add_resource(VistaCandidato, '/sign-up')


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters('172.17.0.2'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


channel.basic_qos(prefetch_count=1)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
