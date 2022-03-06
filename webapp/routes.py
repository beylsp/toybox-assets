from flask import Blueprint

from webapp.views import (
    get_tokens,
)


api_blueprint = Blueprint("api_blueprint", __name__, url_prefix="/api/v1")


# API Routes
# ===

# Tokens
api_blueprint.add_url_rule("/tokens", view_func=get_tokens)