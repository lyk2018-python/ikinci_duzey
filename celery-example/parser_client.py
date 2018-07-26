from celery import Celery

app = Celery(__name__, backend="redis://localhost", broker="amqp://localhost")