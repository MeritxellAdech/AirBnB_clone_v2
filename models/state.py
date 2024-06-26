#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
from models.base_model import BaseModel, Base
from models.engine.db_storage import DBStorage


class State(BaseModel, Base):
    """ The state class, contains state name"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(City, backref="states", cascade="all")
    else:
        @property
        def cities(self):
            """ The getter attribute for city """
            city_list = []
            city_obj = DBStorage.all(City).values()
            for city in city_obj:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
