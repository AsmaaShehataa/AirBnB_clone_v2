#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
from models.place import Place
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class definition """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:

        @property
        def cities(self):
            """Returns the list of City instances with
            state_id equals to the current State.id
            city_list: list of cities from a state
            """ 
            from models import storage
            city_list = []
            city_dict = storage.all(City)

            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
