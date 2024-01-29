# #!/usr/bin/python3
# """ State Module for HBNB project """
# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
# from os import getenv


# class Amenity(BaseModel, Base):
#     """
#     Amenity class represents a feature or service provided by a property.
#     """
#     if getenv('HBNB_TYPE_STORAGE') == 'db':
#         __tablename__ = "amenities"
#         name = Column(String(128), nullable=False)
#     else:
#         name = ""

#     def __init__(self, *args, **kwargs):
#         """initializes Amenity"""
#         super().__init__(*args, **kwargs)


#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')
from models import storage

class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    if STORAGE_TYPE == "db":
        tablename = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('PlaceAmenity',
                                       backref='amenities',
                                       cascade='delete')
    else:
        name = ''
