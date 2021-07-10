from store.forms import CreateUsuarioForm, LoginUsuarioForm
from flask import Blueprint, Response, flash, session, request, render_template, redirect, url_for
from store.models import create_new_user, get_user_by_email

home = Blueprint('home', __name__)



@home.route("/")
def index():
    return render_template("home.html") 

@home.route("/login", methods=["GET", 'POST'])
def login():
    form_login = LoginUsuarioForm()

    if request.method == 'POST':
        email = form_login.email_usuario.data
        pwd = form_login.pwd_usuario.data

        user = get_user_by_email(email)
        print(user)
        if not user:
            print("no existe el usuario")
            flash("No existe el usuario")
            return redirect(url_for('home.index'))
        elif user['pwd_usuario'] == pwd:
            flash("Bienvenido")
            session["usuario"] = user
            return redirect(url_for('home.index'))
    
    return render_template('login.html', form=form_login)


@home.route("/signup", methods=["GET", 'POST'])
def signup():
    form_signup= CreateUsuarioForm()

    if request.method == 'POST' :
        email = form_signup.email_usuario.data
        pwd = form_signup.pwd_usuario.data

        create_new_user('Miguel','Pérez', email, pwd)
        return redirect(url_for('home.index'))
    
    return render_template('signup.html', form=form_signup)
