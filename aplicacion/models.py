from sqlalchemy import Column , ForeignKey
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import relationship
from aplicacion.app import db


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    apellidos = Column(String(50))
    email = Column(String(50))
    telefono = Column(Integer)
    password = Column(String(80))
    dni = Column(String(9))
    direcciones = relationship("Direccion", backref="Cliente", lazy='dynamic')
    pedidos = relationship("Pedido", backref="Cliente", lazy='dynamic')

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Direccion(db.Model):
    __tablename__ = 'direccion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    via = Column(String(100))
    nombre = Column(String(50))
    numero = Column(Integer)
    cod_postal = Column(Integer)
    ciudad = Column(String(50))
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))


class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cif = Column(String(9))
    nombre = Column(String(50))
    direccion = Column(String(100))
    email = Column(String(50))
    telefono = Column(Integer)
    productos = relationship("Producto", backref="Producto", lazy='dynamic')

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Producto(db.Model):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    marca = Column(String(50))
    stock = Column(Integer)
    precio_unidad = Column(Integer)
    categoria = Column(String(20))
    proveedor_id = Column(Integer, ForeignKey('proveedor.id'), nullable=False)
    proveedores = relationship("Proveedor", backref="Producto")
    pedidos = relationship("Pedido", backref="Producto", lazy='dynamic')


    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    cantidad = Column(Integer)
    total = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('producto.id'), nullable=False)
    productos = relationship("Producto", backref="Pedido")

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Factura(db.Model):
    __tablename__ = 'factura'    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    importe_total = Column(Integer)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Pago(db.Model):
    __tablename__ = 'pago'    
    id = Column(Integer, primary_key=True, autoincrement=True)
    factura_id = Column(Integer, ForeignKey('factura.id'))

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'    
    num_tarjeta = Column(Integer, primary_key=True, autoincrement=True)
    titular = Column(String(100))
    caducidad = Column(String(5))
    cliente_id = Column(Integer, ForeignKey('cliente.id'))

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.num_tarjeta}>'.format(self=self))

class Cuenta_Bancaria(db.Model):
    __tablename__ = 'cuenta_bancaria'
    num_cuenta = Column(Integer, primary_key=True, autoincrement=True)
    titular = Column(String(100))
    entidad = Column(String(100))
    cliente_id = Column(Integer, ForeignKey('cliente.id'))

    def __repr__(self):
	    return (u'<{self.__class__.__name__}: {self.num_cuenta}>'.format(self=self))