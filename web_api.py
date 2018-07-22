import flask
import parse_site_api
import test_api
import urllib.parse

app = flask.Flask(__name__)
app.register_blueprint(parse_site_api.blueprint)
app.register_blueprint(test_api.blueprint, url_prefix="/test")


@app.route("/index")
def index_html():
    return flask.render_template("index.html", adi="deneme")


@app.route("/")
def index():
    urls = {}
    for urlrule in list(app.url_map.iter_rules()):
        if urlrule.rule in ['/', '/static/<path:filename>']:
            continue
        urls[urlrule.endpoint] = urllib.parse.urljoin(flask.request.url_root, urlrule.rule)
    return flask.jsonify(urls)


if __name__ == '__main__':
    app.run(debug=True)
