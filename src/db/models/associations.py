from db.conection import Base
from sqlalchemy import Column, Integer, Table, ForeignKey

basket_smartphone_association = Table('basket_smartphone_association', Base.metadata,
    Column('basket_id', Integer, ForeignKey('baskets.id')),
    Column('smartphone_id', Integer, ForeignKey('smartphones.id'))
)