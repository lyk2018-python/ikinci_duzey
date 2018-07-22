import datetime

import flask

blueprint = flask.Blueprint("test_api", __name__)


@blueprint.route("/token")
def token_deneme():
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


@blueprint.route("/get_post", methods=["GET", "POST"])
def get_post_deneme():
    if flask.request.method == "GET":
        return "GET"
    elif flask.request.method == "POST":
        return "POST " + str(dict(flask.request.form))
    else:
        return ""


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
