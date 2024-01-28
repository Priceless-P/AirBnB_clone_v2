#!/usr/bin/python3
"""
Place Module for HBNB project
"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey(
                          "places.id"), nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """Represet a Place Table
    conatins, city_id, user_id, name, description
    and other room descriptions field"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", backref="place_amenity",
                                 secondary="place_amenity", cascade="delete")
    else:
        @property
        def reviews(self):
            """ Getter method for reviews"""
            from models.review import Review
            import models
            reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """ Getter method for amenities"""
            from models.amenity import Amenity
            import models
            amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.amenity_ids == self.id:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """Appends Amenity.id to the attribute amenity_ids"""
            from models.amenity import Amenity
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
