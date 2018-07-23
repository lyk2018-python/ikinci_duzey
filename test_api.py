import datetime

import flask

blueprint = flask.Blueprint("test_api", __name__)


@blueprint.route("/token")
def token_deneme():
    """
    An Endpoint to try post and get methods
    ---
    definitions:
      - schema:
          id: Header
          type: string
      - schema:
          id: Token
          type: object
          properties:
            "tür":
              type: string
              description: Type of the Token
            "değer":
              type: string
              description: Token Value
    responses:
      401:
        description: Requests Basic Auth
      200:
        description: Returns authentication info
        schema:
          type: object
          properties:
            header:
              $ref: '#/definitions/Header'
            token:
              $ref: '#/definitions/Token'
    security:
      - basicAuth: []
      - apiAuth: []

    """
    header = flask.request.headers.get("AUTHORIZATION")
    if header is not None and len(header.split(" ")) == 2:
        tur, deger = header.split(" ")
        token = {"tür": tur, "değer": deger}
    else:
        token = {}
    response = flask.jsonify(header=header, token=token)
    if not token:
        response.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
        response.status_code = 401
    return response


@blueprint.route("/get_ve_post", methods=["GET"])
def get_deneme():
    """
    An Endpoint to try POST and GET methods, this doc is for GET
    ---
    definitions:
      - schema:
          id: Debug Response
          type: string
    responses:
      200:
        description: Returns "GET"
        schema:
          $ref: '#/definitions/Debug Response'
    """
    return "GET"

@blueprint.route("/get_ve_post", methods=["POST"])
def post_deneme():
    """
    An Endpoint to try POST and GET methods, this doc is for POST
    ---
    definitions:
      - schema:
          id: Debug Response
          type: string
    responses:
      200:
        description: Returns "POST"  and a debug string
        schema:
          $ref: '#/definitions/Debug Response'
    """
    return "POST " + str(dict(flask.request.form))


eski_hash = "-"


@blueprint.route("/cookie")
def cookie_deneme():
    global eski_hash
    response = flask.Response()
    eski_cookie = flask.request.cookies.get("ga_as_537191298345", None)

    import hashlib
    hashed = hashlib.md5("-".join([
        flask.request.headers.get("HTTP_USER_AGENT", ""),
        flask.request.headers.get("HTTP_ACCEPT_LANGUAGE", ""),
        flask.request.headers.get("REMOTE_ADDR", ""),
    ]).encode())

    if eski_hash == eski_cookie:
        response.data = "Seni tanıyorum"
    else:
        hashed = hashed.hexdigest()
        response.set_cookie("ga_as_537191298345", hashed, max_age=9999999999,
                            expires=datetime.datetime.now() + datetime.timedelta(days=10))
        eski_hash = hashed
        response.data = "Nice to meet you"

    return response
