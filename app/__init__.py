import os
import json


from flask import Flask, render_template, session, request, flash

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # TODO: add functionality lol
    @app.route('/', methods=('GET', 'POST'))
    def index():
        with open('app/static/data/data.json') as f:
            data = json.load(f)
        # if request.method == 'POST':
            # if request.form.get('')
                
        return render_template('index.html', data=data)
    
    from . import auth
    app.register_blueprint(auth.bp)
    return app
 