from celery import Celery

app = Celery(__name__, backend="amqp://localhost", broker="redis://localhost")

@app.task
def multiple(x,y):
    z = x**y
    print(z)
    return z