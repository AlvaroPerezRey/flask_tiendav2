from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config


app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)	
db = SQLAlchemy(app)

from aplicacion.models import Producto, Cliente

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/productos/')
def producto():
    productos=Producto.query.all()
    return render_template("productos.html", productos=productos)

@app.route('/productos/<id>')
def producto_id(id):
    productos=Producto.query.filter_by(id=id)
    return render_template("productos_id.html", productos=productos)

@app.route('/clientes/')
def cliente():
    clientes=Cliente.query.all()
    return render_template("clientes.html", clientes=clientes)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html",error="Pagina no encontrada..."), 404