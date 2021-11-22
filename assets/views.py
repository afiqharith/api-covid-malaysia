from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import request
from flask import url_for
from flask import jsonify
import requests
import json


views = Blueprint("views", __name__)

@views.route("/index", methods=["GET"])
@views.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", title = "Malaysia Covid-19 API")
    
    if request.method == "POST":
        if request.form.get('submit') == 'isPosted':
            headers = {'Content-type': 'application/json',}
            url_cases = "https://api-covid19-malaysia.herokuapp.com/epidemic/cases"
            url_vaccine = "https://api-covid19-malaysia.herokuapp.com/vaccine"

            payload = json.loads('{"start_date": "2021-02-03", "end_date": "2021-07-05", "state": "Selangor"}')

            response = requests.post(url_vaccine, headers=headers, json=payload)

            return redirect(jsonify(response))

