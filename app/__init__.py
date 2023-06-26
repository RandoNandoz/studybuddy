import os
import json


from flask import Flask, render_template, session, request, flash

from database_stuff import db_interaction


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # TODO: add functionality lol
    @app.route("/", methods=("GET", "POST"))
    def index():
        if len(session) > 0:
            data = db_interaction.get_all_tasks(session["username"])
        else:
            data = {
                "description": "No tasks found"
            }

        return render_template("index.html", data=data)

    from . import auth

    app.register_blueprint(auth.bp)
    return app
