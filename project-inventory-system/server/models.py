from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import DateTime
from sqlalchemy.ext.associationproxy import association_proxy
import datetime

from config import db

# Models go here!

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description  = db.Column(db.String)
    price = db.Column(db.String)
    supplier_id = db.Column(db.Integer)
    date = db.Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Products {self.id}, {self.name}, {self.description}, {self.price}, {self.supplier_id}>'
