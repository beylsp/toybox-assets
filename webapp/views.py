from flask import jsonify

from webapp.decorators import token_required
from webapp.models import Token


# Tokens
# ===
@token_required
def get_tokens():
    tokens = Token.query.all()
    return (
        jsonify(
            [{"name": token.name, "token": token.token} for token in tokens]
        ),
        200,
    )