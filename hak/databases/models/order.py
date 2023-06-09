from sqlalchemy import Column, Integer

from hak.databases.base_class import Base


class Order(Base):
    id = Column(Integer, primary_key=True)
