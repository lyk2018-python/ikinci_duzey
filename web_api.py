import flask

from parse_site import get_goc_data, get_weather_data_xpath, get_itugnu_data, get_beyazperde_data, get_weather_response

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.jsonify({
        "goc":"/goc",
        "hava":"/hava",
        "itugnu":"/itugnu",
        "beyazperde":"/beyazperde",
    })


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


if __name__ == '__main__':
    app.run()
