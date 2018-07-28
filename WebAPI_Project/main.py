from flask import Flask, jsonify, Response
from back import parse
from celery.result import AsyncResult
import os
import json

app = Flask(__name__)

@app.route("/")
def main_page():
    return "Anasayfa"

@app.route("/start_parse")
def start_parse():
    k = parse.delay()
    return k.id

@app.route("/get_result")
def get_result():
    file_path = "data.json"
    if os.path.exists(file_path):
        with open("data.json", "r") as f:
            return jsonify(json.load(f))
    else:
        return Response("Sayfa bulunamadı", status=404)

@app.route("/get_status/<status_id>")
def get_status(status_id):
    result = AsyncResult(status_id, app=parse)
    return jsonify(
        status = result.status,
        data = result.result
    )

if __name__ == '__main__':
    app.run(debug=True)