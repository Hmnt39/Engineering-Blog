from flask import request, render_template, make_response
from flask import current_app as app
from .models import db


@app.route("/", methods=["GET"])
def user_records():
    return "Done"
