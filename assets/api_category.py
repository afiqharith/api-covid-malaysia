from .utils import Documentation
from flask import Blueprint
from flask import request
from flask import jsonify

api_category = Blueprint("api_category", __name__)

@api_category.route("", methods=["GET", "POST"])
def category():
    if request.method == "GET" or request.method == "POST":
        helper = Documentation()
        return jsonify({
            "epidemic": { 
                helper.epidemic_fields[0]: helper.cases_param,
                helper.epidemic_fields[1]: helper.deaths_param,
                helper.epidemic_fields[2]: helper.tests_param,
                helper.epidemic_fields[3]: helper.hospital_param,
            },
            "vaccination": {
                helper.vaccination_fields[0]: helper.vaccination_param
            },
            "available_states": helper.available_states
        })