import click
import flask
import os
import uuid

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


from flask_migrate import Migrate, upgrade

from webapp.app import create_app, db
from webapp.models import Token


app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Token=Token)


token_group = flask.cli.AppGroup("token")

@token_group.command("create")
@click.argument("name")
def create_token(name):
    """Create API token"""
    if Token.query.filter(Token.name == name).one_or_none():
        print(f"Token exists: {name}")
    else:
        token = Token(name=name, token=uuid.uuid4().hex)
        db.session.add(token)
        db.session.commit()
        print(f"Token created: {token.name} - {token.token}")


@token_group.command("view")
@click.argument("name")
def view_token(name):
    """View API token"""
    token = Token.query.filter(Token.name == name).one_or_none()

    if not token:
        print(f"No token named '{name}'")
    else:
        print(f"Token: {token.name} - {token.token}")


app.cli.add_command(token_group)


@app.cli.command()
def deploy():
    """Run deployment tasks"""
    # migrate database to latest revision
    upgrade()