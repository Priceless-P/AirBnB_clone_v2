#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv

from sqlalchemy import MetaData, create_engine
from models.base_model import Base, BaseModel
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new DBStorage object"""
        self.__engine = create_engine("mysql+pymysql://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all available cls objects"""
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.city import City
        from console import HBNBCommand
        from models.base_model import BaseModel
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id):
                obj for obj in objects}

    def new(self, obj):
        """Adds new object to database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.city import City

        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_f)
        self.__session = Session()

    def close(self):
        """Close session."""
        self.__session.close()
