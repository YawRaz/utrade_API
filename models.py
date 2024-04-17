from sqlalchemy import Boolean, String, Integer, Float, Column, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Brand(Base):
    '''defines the brand table'''
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    product = relationship("Product")

    class Config:
        orm_mode = True


class Category(Base):
    '''defines the category table'''
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    product = relationship('Product')
    
    class Config:
        orm_mode = True


class Product(Base):
    '''defines the product table'''
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    price = Column(Float)
    model_name = Column(String)
    brand_id = Column(Integer, ForeignKey("brand.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    brand = relationship("Brand", back_populates='product')
    category = relationship('Category', back_populates='product')