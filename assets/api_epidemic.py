from .utils import DataHandlerEpidemic
from flask import Blueprint
from flask import request
from flask import jsonify

api_epidemic = Blueprint("api_epidemic", __name__)

@api_epidemic.route("/cases", methods=["GET", "POST"])
def cases():
    if request.method == "GET":
        helper = DataHandlerEpidemic()
        helper.client_query_state = request.args.get("state", default=None, type=str)
        helper.client_query_start_date = request.args.get("start_date", default=None, type=str)
        helper.client_query_end_date = request.args.get("end_date", default=None, type=str)

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_cases_malaysia()
        elif helper.client_query_state  != None:
            results = helper.get_cases_state()
        elif helper.client_query_state  != None and helper.client_query_state.lower() == "all":
            results = helper.get_cases_state_all()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})

        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

    if request.method == "POST":
        json_obj = request.get_json()
        helper = DataHandlerEpidemic()
        helper.client_query_state = json_obj.get("state")
        helper.client_query_start_date = json_obj.get("start_date")
        helper.client_query_end_date = json_obj.get("end_date")

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_cases_malaysia() 
        elif helper.client_query_state != None:
            results = helper.get_cases_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})


@api_epidemic.route("/deaths", methods=["GET", "POST"])
def deaths():
    if request.method == "GET":
        helper = DataHandlerEpidemic()
        helper.client_query_state = request.args.get("state", default=None, type=str)
        helper.client_query_start_date = request.args.get("start_date", default=None, type=str)
        helper.client_query_end_date = request.args.get("end_date", default=None, type=str)

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_deaths_malaysia()
        elif helper.client_query_state != None:
            results = helper.get_deaths_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

    if request.method == "POST":
        json_obj = request.get_json()
        helper = DataHandlerEpidemic()
        helper.client_query_state = json_obj.get("state")
        helper.client_query_start_date = json_obj.get("start_date")
        helper.client_query_end_date = json_obj.get("end_date")

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_deaths_malaysia()
        elif helper.client_query_state != None:
            results = helper.get_deaths_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

@api_epidemic.route("/tests", methods=["GET", "POST"])
def tests():
    if request.method == "GET":
        helper = DataHandlerEpidemic()
        helper.client_query_state = request.args.get("state", default=None, type=str)
        helper.client_query_start_date = request.args.get("start_date", default=None, type=str)
        helper.client_query_end_date = request.args.get("end_date", default=None, type=str)

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_tests_malaysia()
        elif helper.client_query_state != None:
            results = helper.get_tests_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

    if request.method == "POST":
        json_obj = request.get_json()
        helper = DataHandlerEpidemic()
        helper.client_query_state = json_obj.get("state")
        helper.client_query_start_date = json_obj.get("start_date")
        helper.client_query_end_date = json_obj.get("end_date")

        if helper.client_query_state == None or helper.client_query_state == "":
            results = helper.get_tests_malaysia()
        elif helper.client_query_state != None:
            results = helper.get_tests_state()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed", "data": results})

@api_epidemic.route("/hospital", methods=["GET", "POST"])
def hospital():
    if request.method == "GET":
        helper = DataHandlerEpidemic()
        helper.client_query_state = request.args.get("state", default=None, type=str)
        helper.client_query_start_date = request.args.get("start_date", default=None, type=str)
        helper.client_query_end_date = request.args.get("end_date", default=None, type=str)

        if helper.client_query_state != None:
            results = helper.get_hospital()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed",  "data": results})
    
    if request.method == "POST":
        json_obj = request.get_json()
        helper = DataHandlerEpidemic()
        helper.client_query_state = json_obj.get("state")
        helper.client_query_start_date = json_obj.get("start_date")
        helper.client_query_end_date = json_obj.get("end_date")

        if helper.client_query_state != None:
            results = helper.get_hospital()
        else:
            return jsonify({"status": "failed", "message": "unsupported query"})
        
        if results != None:
            return jsonify({"status": "success", "data": results})
        else:
            return jsonify({"status": "failed",  "data": results})