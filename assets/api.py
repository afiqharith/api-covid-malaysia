from .utils import DataHandler as helper
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import request
from flask import url_for
from flask import jsonify


api = Blueprint("api", __name__)

@api.route("/cases", methods=["GET"])
def cases():

    if request.method == "GET":
        client_state = request.args.get("state", default=None, type=str)
        client_date = request.args.get("date", default=None, type=str)

        if client_state == None:
            results = helper.get_cases_malaysia(client_date)
        elif client_state != None:
            results = helper.get_state_cases(client_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "date" : client_date, "cases": results})
        else:
            return jsonify({"status": "failed", "date": client_date, "cases": None})


@api.route("/deaths", methods=["GET"])
def deaths():
    if request.method == "GET":
        client_state = request.args.get("state", default=None, type=str)
        client_date = request.args.get("date", default=None, type=str)

        if client_state == None:
            results = helper.get_deaths_malaysia(client_date)
        elif client_state != None:
            results = helper.get_deaths_state(client_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "date" : client_date, "death_cases": results})
        else:
            return jsonify({"status": "failed", "date": client_date, "death_cases": None})