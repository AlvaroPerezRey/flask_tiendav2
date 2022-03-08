from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models import *

manager = Manager(app)
app.config['DEBUG'] = True

@manager.command
def create_tables():
    "Crear las tablas de la db"
    db.create_all()

@manager.command
def drop_tables():
    "Eliminar tablas de la db"
    db.drop_all()

@manager.command
def add_data_tables():
    db.create_all()
    
    clientes = ("Pedro","Juan","Alberto","Pepe","Susana","Raquel")

    for cli in clientes:
        cliente=Cliente(nombre=cli)
        db.session.add(cliente)
        db.session.commit()

    productos=[
        {"nombre":"Sudadera burdeos v3","marca":"OGs","stock":50,"precio_unidad":50,"categoria":"Sudaderas"},
        {"nombre":"Sudadera roja v3","marca":"Nike","stock":50,"precio_unidad":60,"categoria":"Sudaderas"},
        {"nombre":"Sudadera azul v3","marca":"Adidas","stock":50,"precio_unidad":75,"categoria":"Sudaderas"},
        {"nombre":"Sudadera gris v3","marca":"Ripcurl","stock":50,"precio_unidad":80,"categoria":"Sudaderas"},
        {"nombre":"Sudadera verde v3","marca":"Element","stock":50,"precio_unidad":70,"categoria":"Sudaderas"},
        {"nombre":"Sudadera rosa v3","marca":"Asics","stock":50,"precio_unidad":90,"categoria":"Sudaderas"},
    ]

    for pro in productos:
        producto=Producto(**pro)
        db.session.add(producto)
        db.session.commit()

if __name__ == '__main__':
    manager.run()