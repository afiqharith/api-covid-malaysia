from .utils import DataHandler as helper
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import request
from flask import url_for
from flask import jsonify


views = Blueprint("views", __name__)

@views.route("/index", methods=["GET"])
@views.route("/", methods=["GET"])
def index():
    return render_template("index.html", title = "Malaysia Covid-19 API")