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
    # else:
    #     @property
    #     def cities(self):
    #         """Getter for cities"""
    #         from models import storage
    #         return [ct for ct in storage.all(City).values()
    #                 if ct.state_id == self.id]
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for cities"""
            from models import storage
            from models.city import City
            city_list = []
            all_cities = models.storage.all(City)
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list


