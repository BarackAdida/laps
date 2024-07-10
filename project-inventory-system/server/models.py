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
    supplier_id = db.Column(db.Integer ForeignKey('suppliers.id'))
    date = db.Column(DateTime, default=datetime.datetime.utcnow)

    products = db.relationship('Product', back_populates='supplier')

    def __repr__(self):
        return f'<Products {self.id}, {self.name}, {self.description}, {self.price}, {self.supplier_id}, {self.date}>'
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    products_id = db.Column(db.Integer ForeignKey('products.id'))
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)

    product = db.relationship('Product', back_populates = 'transactions')

    def __repr__(self):
        return f'<Transactions {self.id}, {self.quantity}, {self.products_id}, {self.created_at}>'
