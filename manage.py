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
        {"nombre":"Feel Special","marca":"Twice","stock":50,"precio_unidad":50,"categoria":"Sudaderas","proveedor_id":1},
        {"nombre":"Butter","marca":"BTS","stock":50,"precio_unidad":60,"categoria":"Sudaderas","proveedor_id":2},
        {"nombre":"Fight or Escape","marca":"TXT","stock":50,"precio_unidad":75,"categoria":"Sudaderas","proveedor_id":3},
        {"nombre":"Young Luv","marca":"Stayc","stock":50,"precio_unidad":80,"categoria":"Sudaderas","proveedor_id":4},
        {"nombre":"Miroh","marca":"Stray Kids","stock":50,"precio_unidad":70,"categoria":"Sudaderas","proveedor_id":5},
        {"nombre":"Formula of Love","marca":"Twice","stock":50,"precio_unidad":90,"categoria":"Sudaderas","proveedor_id":6},
    ]

    for pro in productos:
        producto=Producto(**pro)
        db.session.add(producto)
        db.session.commit()

if __name__ == '__main__':
    manager.run()