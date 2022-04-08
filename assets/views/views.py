from datetime import datetime
from flask import render_template
from flask import Blueprint
from flask import request
import datetime

views = Blueprint("views", __name__)

@views.route("/index", methods=["GET"])
@views.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", title = "Web API Covid-19 Malaysia", year=datetime.datetime.now().strftime("%Y"))