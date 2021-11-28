from .utils import DataHandlerVaccination
from flask import Blueprint
from flask import request
from flask import jsonify

api_vaccination = Blueprint("api_vaccination", __name__)

@api_vaccination.route("", methods=["GET", "POST"])
def vaccine():
    if request.method == "GET":
        helper = DataHandlerVaccination()
        helper.client_query_state = request.args.get("state", default=None, type=str)
        helper.client_query_start_date = request.args.get("start_date", default=None, type=str)
        helper.client_query_end_date = request.args.get("end_date", default=None, type=str)

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_vaccine_malaysia()
        elif helper.client_query_state != None:
            results = helper.get_vaccine_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

    if request.method == "POST":
        json_obj = request.get_json()
        helper = DataHandlerVaccination()
        helper.client_query_state = json_obj.get("state")
        helper.client_query_start_date = json_obj.get("start_date")
        helper.client_query_end_date = json_obj.get("end_date")

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_vaccine_malaysia()
        elif helper.client_query_state != None:
            results = helper.get_vaccine_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})