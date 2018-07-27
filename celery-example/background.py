from celery import Celery

app = Celery(__name__, backend="amqp://localhost", broker="redis://localhost")


@app.task
def multiple(x, y):
    z = x ** y
    print(z)
    return z


@app.task
def topla(x, y):
    return x + y


@app.task
def cikar(a, b):
    return a - b


"""
chord([topla.s(1, 2), topla.s(3, 4)], cikar.s())
"""