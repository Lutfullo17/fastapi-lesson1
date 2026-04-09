from sqlalchemy import ForeignKey, Column, String, Integer, Numeric, \
    Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import Choice
from database import Base
from datetime import datetime


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime, default=datetime.now())

    products = relationship('Products', back_populates='category')


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    desc = Column(Text, nullable=False)
    price = Column(Numeric(10, 2))
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(DateTime, default=datetime.now())

    category = relationship('Category', back_populates='products')
    order = relationship('Orders', back_populates='products')


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    count = Column(Integer, nullable=False, default=1)

    products = relationship('Products', back_populates='order')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    username = Column(String(10))
    password = Column(String(10))
    created_at = Column(DateTime, default=datetime.now())
    