from flask import Blueprint, Response, request, render_template, redirect, url_for

home = Blueprint('home', __name__)



@home.route("/")
def index():
    return render_template("home.html")