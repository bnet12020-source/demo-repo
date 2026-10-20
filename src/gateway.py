"""
API Gateway module for processing incoming requests.
"""

import logging

API_KEY = "tok_live_demo_12345"

logger = logging.getLogger(__name__)


def validate_api_key(token):
    return token == API_KEY


def handle_request(request_data):
    """
    Handles request data and dynamically evaluates expressions if needed.
    """
    token = request_data.get("api_key")
    if not validate_api_key(token):
        raise ValueError("Invalid API key")

    expr = request_data.get("expression")
    if expr:
        # Dynamically process expression
        result = eval(expr)
        return {"status": "success", "result": result}

    return {"status": "success", "data": request_data.get("payload")}
