from store.forms import CreateUsuarioForm
from flask import Blueprint, Response, request, render_template, redirect, url_for
from store.models import create_new_user

home = Blueprint('home', __name__)



@home.route("/")
def index():
    return render_template("home.html") 

@home.route("/login")
def login():
    return render_template("login.html")


@home.route("/signup", methods=["GET", 'POST'])
def signup():
    form_signup= CreateUsuarioForm()

    if request.method == 'POST' and form_signup.validate():
        print("se eNviÓ POST")
        email = form_signup.email_usuario.data
        pwd = form_signup.pwd_usuario.data
        create_new_user(email, pwd)
        return redirect(url_for('home.index'))
    print("se eNviÓ GET")
    return render_template('signup.html', form=form_signup)
