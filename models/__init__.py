#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


storage = DBStorage() if getenv('HBNB_TYPE_STORAGE') == 'db' else FileStorage()
storage.reload()
