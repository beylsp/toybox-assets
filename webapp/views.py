import uuid
from flask import abort, jsonify

from webapp.app import db
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


@token_required
def get_token(name):
    token = Token.query.filter(Token.name == name).one_or_none()

    if not token:
        abort(404)

    return jsonify({"name": token.name, "token": token.token})


@token_required
def create_token(name):
    if not name:
        abort(400, "Missing required field 'name'")

    if Token.query.filter(Token.name == name).one_or_none():
        abort(400, "A token with this name already exists")

    token = Token(name=name, token=uuid.uuid4().hex)
    db.session.add(token)
    db.session.commit()

    return jsonify({"name": token.name, "token": token.token}), 201


@token_required
def delete_token(name):
    token = Token.query.filter(Token.name == name).one_or_none()

    if not token:
        abort(400, f"No token named '{name}'")

    db.session.delete(token)
    db.session.commit()

    return jsonify({}), 204