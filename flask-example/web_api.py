import flask
import parse_site_api
import test_api
import urllib.parse
from flask_swagger_ui import get_swaggerui_blueprint

swaggerui_blueprint = get_swaggerui_blueprint(
    '/spec/ui',
    '/spec/json',
)

app = flask.Flask(__name__)
app.register_blueprint(parse_site_api.blueprint)
app.register_blueprint(test_api.blueprint, url_prefix="/test")
app.register_blueprint(swaggerui_blueprint, url_prefix="/spec/ui")


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/api_urls")
def api_urls():
    """
    With this endpoint you can view all the endpoints in this web service.
    ---
    definitions:
      - schema:
          id: Endpoint
          type: object
          properties:
            name:
              type: string
              description: Endpoint's Name
            url:
              type: string
              description: Endpoint's URL
    responses:
      200:
        description: An array of endpoints
        schema:
          type: array
          items:
            $ref: '#/definitions/Endpoint'
    """
    urls = []
    for urlrule in list(app.url_map.iter_rules()):
        if urlrule.rule in ['/', '/static/<path:filename>']:
            continue
        urls.append({"name": urlrule.endpoint, "url": urllib.parse.urljoin(flask.request.url_root, urlrule.rule)})
    return flask.jsonify(urls)


@app.route("/spec/json")
def spec():
    from flask_swagger import swagger
    swagger_data = swagger(app, prefix="/")
    swagger_data["info"]["title"] = "Flask Örnek"
    return flask.jsonify(swagger_data)


if __name__ == '__main__':
    app.run(debug=True)
