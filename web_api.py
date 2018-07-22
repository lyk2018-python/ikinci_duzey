import flask

from parse_site import get_goc_data, get_weather_data_xpath, get_itugnu_data, get_beyazperde_data, get_weather_response

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.jsonify({
        "goc": flask.request.url_root + "goc",
        "hava": flask.request.url_root + "hava",
        "itugnu": flask.request.url_root + "itugnu",
        "beyazperde": flask.request.url_root + "beyazperde",
        "token": flask.request.url_root + "token",
    })


@app.route("/token")
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


@app.route("/goc")
def api_get_goc_data():
    return flask.jsonify(get_goc_data())


@app.route("/hava")
def api_get_weather_data_xpath():
    return flask.jsonify(get_weather_data_xpath(get_weather_response()))


@app.route("/itugnu")
def api_get_itugnu_data():
    return flask.jsonify(get_itugnu_data())


@app.route("/beyazperde")
def api_get_beyazperde_data():
    return flask.jsonify(get_beyazperde_data())


@app.route("/beyazperde/<int:sayi>")
def api_get_beyazperde_data_sayili(sayi):
    return flask.jsonify(get_beyazperde_data(sayi))


@app.route("/get_post", methods=["GET", "POST"])
def get_post_deneme():
    if flask.request.method == "GET":
        return "GET"
    elif flask.request.method == "POST":
        return "POST" + str(dict(flask.request.form))
    else:
        return ""


if __name__ == '__main__':
    app.run()
