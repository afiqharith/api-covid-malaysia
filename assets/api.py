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
        client_start_date = request.args.get("start_date", default=None, type=str)
        client_end_date = request.args.get("end_date", default=None, type=str)

        if client_state == None:
            results = helper.get_cases_malaysia(client_start_date, client_end_date)
        elif client_state != None:
            results = helper.get_state_cases(client_start_date, client_end_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "cases": results})
        else:
            return jsonify({"status": "failed", "cases": results})

@api.route("/deaths", methods=["GET"])
def deaths():
    if request.method == "GET":
        client_state = request.args.get("state", default=None, type=str)
        client_start_date = request.args.get("start_date", default=None, type=str)
        client_end_date = request.args.get("end_date", default=None, type=str)

        if client_state == None:
            results = helper.get_deaths_malaysia(client_start_date, client_end_date)
        elif client_state != None:
            results = helper.get_deaths_state(client_start_date, client_end_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "death_cases": results})
        else:
            return jsonify({"status": "failed", "death_cases": results})

@api.route("/tests", methods=["GET"])
def tests():
    if request.method == "GET":
        client_state = request.args.get("state", default=None, type=str)
        client_start_date = request.args.get("start_date", default=None, type=str)
        client_end_date = request.args.get("end_date", default=None, type=str)

        if client_state == None:
            results = helper.get_tests_malaysia(client_start_date, client_end_date)
        elif client_state != None:
            results = helper.get_tests_state(client_start_date, client_end_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "tests": results})
        else:
            return jsonify({"status": "failed", "tests": results})

@api.route("/hospital", methods=["GET"])
def hospital():
    if request.method == "GET":
        client_state = request.args.get("state", default=None, type=str)
        client_start_date = request.args.get("start_date", default=None, type=str)
        client_end_date = request.args.get("end_date", default=None, type=str)

        if client_state != None:
            results = helper.get_hospital(client_start_date, client_end_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "hospital": results})
        else:
            return jsonify({"status": "failed",  "hospital": results})