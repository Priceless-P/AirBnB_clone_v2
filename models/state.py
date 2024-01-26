#!/usr/bin/python3
"""
State Module for HBNB project
"""
from os import getenv
from sqlalchemy import String, Column
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class represent the states
     table
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")

    else:
        @property
        def cities(self):
            """Gets list of all related cities"""
            from models.city import City
            cities = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
