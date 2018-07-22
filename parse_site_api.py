import flask
from parse_site import get_goc_data, get_weather_data_xpath, get_itugnu_data, get_beyazperde_data, get_weather_response

blueprint = flask.Blueprint('parse_site_api', __name__)


@blueprint.route("/goc")
def api_get_goc_data():
    return flask.jsonify(get_goc_data())


@blueprint.route("/hava")
def api_get_weather_data_xpath():
    return flask.jsonify(get_weather_data_xpath(get_weather_response()))


@blueprint.route("/itugnu")
def api_get_itugnu_data():
    return flask.jsonify(get_itugnu_data())


@blueprint.route("/beyazperde")
def api_get_beyazperde_data():
    return flask.jsonify(get_beyazperde_data())


@blueprint.route("/beyazperde/<int:sayi>")
def api_get_beyazperde_data_sayili(sayi):
    return flask.jsonify(get_beyazperde_data(sayi))
