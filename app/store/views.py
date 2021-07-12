
from app.store.forms import CreateUsuarioForm, LoginUsuarioForm, newArtistForm, newReleaseForm
from flask import Blueprint, Response, flash, session, request, g, render_template, redirect, url_for, jsonify
from app.store.models import create_new_user, get_all_artists, get_user_by_email, create_new_artist


home = Blueprint('home', __name__)
dashboard = Blueprint('dashboard', __name__, url_prefix=  '/dashboard')


@home.before_request
def before_request():
    if "user" in session:
        g.user = session["user"]
    else:
        g.user = None

@home.route("/")
def index():
    return render_template("home.html", user = g.user) 

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
            session["user"] = user
            return redirect(url_for('home.index', user=g.user))
    
    return render_template('login.html', form=form_login)


@home.route("/signup", methods=["GET", 'POST'])
def signup():
    print("g.user "+ str(g.user))
    if not g.user:
        form_signup= CreateUsuarioForm()

        if request.method == 'POST' :
            email = form_signup.email_usuario.data
            pwd = form_signup.pwd_usuario.data

            create_new_user('Miguel','Pérez', email, pwd)
            return redirect(url_for('home.index',user=g.user))
    
        return render_template('signup.html', form=form_signup)
    
    flash("You're already logged in.", "alert-primary")
    return redirect(url_for('home.index', user = g.user))

@home.route("/logout", methods=["GET", 'POST'])
def logout():
    session.pop("user", None)
    flash("You're logged out.", "alert-secondary")

    return redirect(url_for("home.index", user=g.user))

@home.route("/account", methods=["GET", "POST"])
def account():
    return "Mi cuenta"

@home.route("/dashboard", methods=["GET", "POST"])
def admin():
    
    return render_template("adminDashboard.html", user=g.user)


#routes del pandel de administración
@dashboard.route("/newartist", methods=["GET", "POST"])
def newartist():
    form_login = newArtistForm()
    if request.method=='POST':
        n_artista = form_login.n_artista.data
        create_new_artist(n_artista)
        return redirect(url_for('home.admin'))
    return render_template("newArtist.html", form=form_login)

@dashboard.route( "/newrelease" ,methods=["GET", "POST"])
def newrelease():
    artists= get_all_artists()
    selectfieldartist =[]
    for artist in artists:
        selectfieldartist.append((artist['k_artista'], artist['n_artista']))
        
    #print(selectfieldartist)
    #form_new_release = newReleaseForm()
    form_new_release=newReleaseForm()

    if request.method == 'POST':
        n_lanzamiento = form_new_release.n_lanzamiento.data
        i_lanzamiento = form_new_release.i_lanzamiento.data
        k_artista = form_new_release.k_artista.data
        print(n_lanzamiento)
        print(i_lanzamiento)
        print(k_artista)
    
    return render_template("newRelease.html", form = form_new_release )

@dashboard.route("/newrelease_artists")
def newrelease_artists():
    artists= get_all_artists()
    selectfieldartist =[]
    for artist in artists:
        #selectfieldartist.append((artist['k_artista'], artist['n_artista']))
        selectfieldartist.append((artist['n_artista']))
    return jsonify(selectfieldartist)