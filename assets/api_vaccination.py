from .utils import DataHandlerVaccination as helper
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import request
from flask import url_for
from flask import jsonify
import json

api_vaccination= Blueprint("api_vaccination", __name__)

@api_vaccination.route("", methods=["GET", "POST"])
def vaccine():
    if request.method == "GET":
        client_state = request.args.get("state", default=None, type=str)
        client_start_date = request.args.get("start_date", default=None, type=str)
        client_end_date = request.args.get("end_date", default=None, type=str)

        if client_state == None or client_state == "":
            results = helper.get_vaccine_malaysia(client_start_date, client_end_date)
        elif client_state != None:
            results = helper.get_vaccine_state(client_start_date, client_end_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

    if request.method == "POST":
        json_obj = json.loads(json.dumps(request.get_json()))
        client_state = json_obj.get("state")
        client_start_date = json_obj.get("client_start_date")
        client_end_date = json_obj.get("client_end_date")

        if client_state == None or client_state == "":
            results = helper.get_vaccine_malaysia(client_start_date, client_end_date)
        elif client_state != None:
            results = helper.get_vaccine_state(client_start_date, client_end_date, client_state)
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})