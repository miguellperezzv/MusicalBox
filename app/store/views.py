
#from app.store.forms import CreateUsuarioForm, LoginUsuarioForm, newArtistForm, newReleaseForm
from store.forms import CreateUsuarioForm, LoginUsuarioForm,  newReleaseForm, newProductForm, newCat_Genre_Artist, newAdmin
from flask import Blueprint, Response, flash, session, request, g, render_template, redirect, url_for, jsonify
#from app.store.models import create_new_user, get_all_artists, get_user_by_email, create_new_artist
from store.models import create_new_user, get_all_artists, get_user_by_email, create_new_artist, get_k_artist_by_name, create_new_release, get_release_by_name, get_releases_with_artists, get_categories, create_new_product, get_k_release_by_name_artista, create_new_category, create_new_genre, create_release_genre, new_admin, get_all_releases, get_artist_by_release, get_categories_by_release, get_release_by_id, get_genres_by_release, get_products_by_release, get_product_by_id

home = Blueprint('home', __name__)
dashboard = Blueprint('dashboard', __name__, url_prefix=  '/dashboard')
releases = Blueprint('releases', __name__, url_prefix=  '/releases')
artists = Blueprint("artists", __name__, url_prefix=  '/artists')
purchase = Blueprint("purchase", __name__, url_prefix=  '/artists' )

cart = []

@home.before_request
@purchase.before_request
@releases.before_request
@artists.before_request
@dashboard.before_request
def before_request():
    if "user" in session:
        g.user = session["user"]
    else:
        g.user = None
    
    if "purchase" in session:
        g.purchase = session["purchase"]
        print("PURCHASE CART IS: ")
        print(g.purchase)
        print("lenght "+ str(len(g.purchase)))
    else:
        g.purchase = None

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
            return redirect(url_for('home.index', user=g.user, purchase_cart = g.purchase))
    
    return render_template('login.html', form=form_login)


@home.route("/signup", methods=["GET", 'POST'])
def signup():
    print("g.user "+ str(g.user))
    if not g.user:
        form_signup= CreateUsuarioForm()

        if request.method == 'POST' :
            email = form_signup.email_usuario.data
            pwd = form_signup.pwd_usuario.data
            name = form_signup.name.data
            apellido = form_signup.lastname.data
            result : create_new_user(name,apellido, email, pwd)
            if result:
                flash("Usuario creado!")
            else:
                flash("No se creo el Usuario!")
            return redirect(url_for('home.index',user=g.user))
        return render_template('signup.html', form=form_signup)
    
    flash("You're already logged in.", "alert-primary")
    return redirect(url_for('home.index', user = g.user))

@home.route("/logout", methods=["GET", 'POST'])
def logout():
    session.pop("user", None)
    session.pop("purchase", None)
    flash("You're logged out.", "alert-secondary")

    return redirect(url_for("home.index", user=g.user))

@home.route("/account", methods=["GET", "POST"])
def account():
    return "Mi cuenta"

@home.route("/dashboard", methods=["GET", "POST"])
def admin():
    return render_template("adminDashboard.html", user=g.user, purchase_cart = g.purchase)


#routes del panel de administración

@dashboard.route( "/newrelease" ,methods=["GET", "POST"])
def newrelease():
    

    form_new_release=newReleaseForm()

    if request.method == 'POST':
        n_lanzamiento = form_new_release.n_lanzamiento.data
        i_lanzamiento = form_new_release.i_lanzamiento.data
        k_artista =  get_k_artist_by_name(form_new_release.k_artista.data)
        f_lanzamiento = form_new_release.f_lanzamiento.data
        k_genero = form_new_release.k_genero.data
        print(k_genero)
        k_lanzamiento= create_new_release(k_artista, n_lanzamiento, i_lanzamiento, f_lanzamiento, k_genero)
        print("EL LANZAMIENTO ES: "+str(k_lanzamiento)+" , "+ n_lanzamiento)
        if k_lanzamiento :
            release_genre = create_release_genre(k_lanzamiento,  k_genero)
            if release_genre:
                flash("Lanzamiento Registrado! "+ str(n_lanzamiento) +" - "+ str(k_genero))
                return redirect(url_for('home.admin'))
        else:
            flash("No se pudo registrar")
        return redirect(url_for('home.admin'))
    return render_template("newRelease.html", form = form_new_release )

@dashboard.route("/newrelease_artists")
def newrelease_artists():
    artists= get_all_artists()
    selectfieldartist =[]
    for artist in artists:
        #selectfieldartist.append((artist['k_artista'], artist['n_artista']))
        selectfieldartist.append((artist['n_artista']))
    return jsonify(selectfieldartist)

@dashboard.route("/newproduct", methods=["GET", "POST"])
def newproduct():
    categories =  get_categories()
    form_new_product = newProductForm(categories_choices=categories)
    if request.method=="POST":
        n_lanzamiento = form_new_product.n_lanzamiento.data.split(" - ")[-1]
        n_artista = form_new_product.n_lanzamiento.data.split(" - ")[0].upper()
        n_producto = form_new_product.n_producto.data
        p_producto  =form_new_product.p_producto.data
        d_producto = form_new_product.d_producto.data
        stock = form_new_product.stock.data
        i_producto = form_new_product.i_producto.data
        k_categoria = dict(form_new_product.k_category.choices).get(form_new_product.k_category.data)
        k_lanzamiento = get_k_release_by_name_artista(n_lanzamiento,n_artista)
        product = create_new_product(k_lanzamiento, n_producto, p_producto, d_producto, stock, i_producto, k_categoria)
        if product:
            print("Producto creado exitosamente!!! ")
            return redirect(url_for('home.admin'))
        else:
            flash("No se pudo registrar")
        return redirect(url_for('home.admin'))
    return render_template("newProduct.html", form=form_new_product)

@dashboard.route("/newproduct_releases")
def newproduct_releases():
    release_artist = get_releases_with_artists()
    return jsonify(release_artist)

@dashboard.route("/newproduct_categories")
def newproduct_categories():
    categories = get_categories()
    return jsonify(categories)

@dashboard.route("/newgenre_category_artist", methods=["GET", "POST"])
def newgenre_category_artist():
    form_cat_genre = newCat_Genre_Artist()
    if request.method=='POST':
        return "Soy el Post de esta vista"
    return render_template("newCatGenreArtist.html", form = form_cat_genre) 

@dashboard.route("/newgenre", methods=["GET", "POST"])
def newgenre():
    if request.method =='POST':
        form_cat_genre = newCat_Genre_Artist()
        genre = form_cat_genre.genre.data.upper()
        result = create_new_genre(genre)
        if result:
            flash("Genero registrado!")
            return url_for('home.admin')
        flash("No se agregó el género! Posiblemente ya exista ;)")
        return url_for('home.admin')

@dashboard.route("/newcategory", methods=["GET", "POST"])
def newcategory():
    if request.method =='POST':
        form_cat_genre = newCat_Genre_Artist()
        category = form_cat_genre.category.data.upper()
        result = create_new_category(category)
        if result:
            flash("Cateogría registrada!")
            return url_for('home.admin')
        flash("No se agregó la categoría! Posiblemente ya exista ;)")
        return url_for('home.admin')

@dashboard.route("/newartist", methods=["GET", "POST"])
def newartist():
    if request.method=='POST':
        form_cat_genre = newCat_Genre_Artist()
        artist = form_cat_genre.n_artist.data.upper()
        country = form_cat_genre.country.data
        print(country)
        result = create_new_artist(artist, country)
        if result:
            flash("Artista registrado!: " + artist)
            return url_for('home.admin')
        flash("No se agregó el artista! Posiblemente ya exista ;)")
        return url_for('home.admin')

@dashboard.route("/newadmin", methods=['GET', 'POST'])
def newadmin():
    form_new_admin= newAdmin()
    if request.method=='POST':
        
        email = form_new_admin.email.data
        pwd = form_new_admin.pwd.data
        result = new_admin(email, pwd, session["user"])
        print("result "+ str(result))
        if result:
            flash("Nuevo administrador con el correo "+ email)
            return redirect(url_for("home.admin"))
        else:
            flash("Contraseña o email incorrectos! ")
            return redirect(url_for("home.admin"))
        
    return render_template("newAdmin.html", form = form_new_admin)

    

@releases.route('/', methods=["GET", "POST"])
def home_releases():
    if request.method == "POST":
        None
    if request.method == 'GET':
        return render_template("releases.html", user=g.user, purchase_cart = g.purchase, releases = get_all_releases(), get_artist_by_release = get_artist_by_release, get_categories_by_release = get_categories_by_release )

@releases.route("/<int:k_lanzamiento>", methods=["GET", "POST"])
def release(k_lanzamiento):
    if request.method == 'GET':
        artista = get_artist_by_release(k_lanzamiento)
        lanzamiento = get_release_by_id(k_lanzamiento)
        generos = get_genres_by_release(k_lanzamiento)
        productos = get_products_by_release(k_lanzamiento)
        return render_template("singleRelease.html", artista=artista, lanzamiento=lanzamiento, generos = generos, productos=productos, user=g.user, addtocart=addtocart, purchase_cart = g.purchase)


@artists.route("/<int:k_artista>", methods=["GET", "POST"])
def artist(k_artista):
    if request.method == 'GET':
        return "Pagona artista" + str(k_artista)

@purchase.route("/", methods=["GET", "POST"])
def summary():
    if request.method == 'GET':
        return render_template("purchase.html", user=g.user, purchase_cart=g.purchase, get_product_by_id = get_product_by_id, total=0, get_release_by_id = get_release_by_id)
    if request.method == 'POST':
        None


def addtocart(k_product):
        print(k_product)
        print("CODIGO DEL PRODUCTO")
        cart.append(k_product)
        session['purchase']= cart
        
    