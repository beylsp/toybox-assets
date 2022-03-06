from flask import Blueprint

from webapp.views import (
    create_token,
    delete_token,
    get_token,
    get_tokens,
)


api_blueprint = Blueprint("api_blueprint", __name__, url_prefix="/api/v1")


# API Routes
# ===

# Tokens
api_blueprint.add_url_rule("/tokens", view_func=get_tokens)
api_blueprint.add_url_rule("/tokens/<string:name>", view_func=get_token)
api_blueprint.add_url_rule(
    "/tokens/<string:name>", view_func=create_token, methods=["POST"])
api_blueprint.add_url_rule(
    "/tokens/<string:name>", view_func=delete_token, methods=["DELETE"])