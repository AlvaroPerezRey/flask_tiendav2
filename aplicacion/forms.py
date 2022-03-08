from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import Required


class formProducto(FlaskForm):                      
    nombre=StringField("nombre:",validators=[Required("Tienes que introducir el dato")])
    marca=StringField("marca:",validators=[Required("Tienes que introducir el dato")])
    stock=IntegerField("stock:",default=10,validators=[Required("Tienes que introducir el dato")])
    precio_unidad=IntegerField("precio_unidad:",default=15,validators=[Required("Tienes que introducir el dato")])
    categoria=StringField("categoria:",validators=[Required("Tienes que introducir el dato")])
    proveedor_id=IntegerField("poveedor_id:",validators=[Required("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')
