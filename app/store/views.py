from flask import Blueprint, Response, request, render_template, redirect, url_for

home = Blueprint('home', __name__)


@home.route("/")
def index():
    return "<h1> Hola mundo!!! inicio de Musical Box!! <h1>"
