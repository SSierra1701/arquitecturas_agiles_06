""" from celery import Celery
import time

app = Celery('tasks', backend='sqlite:///dbapp.sqlite',
             broker='amqp://guest@arquitectura//')


@app.task()
def add(x, y):

    time.sleep(15)

    result = x + y

    return result """
