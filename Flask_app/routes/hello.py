from flask import Blueprint, request, jsonify, current_app
from Flask_app.utils.audit import log_request

hello_bp = Blueprint("hello", __name__)

@hello_bp.route("/", methods=["GET"])
def hello_world():
    if current_app.config.get("AUDIT_ENABLED"):
        log_request(endpoint="/", method="GET", payload={})
    return jsonify(message="Hello, Flask!")