#!/usr/bin/python3
"""Engine for Database Storage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """db storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """ creates connection to db"""
        dilect = 'mysql'
        driver = 'mysqldb'
        usr = getenv('HBNB_MYSQL_USER', 'hbnb_dev')
        pwd = getenv('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}".format(
            dilect, driver, usr, pwd, host, db))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """query on current db"""
        if cls:
            result = self.__session.query(cls).all()
        else:
            result = self.__session.query(User).all()
            result += self.__session.query(State).all()
            result += self.__session.query(City).all()
            result += self.__session.query(Amenity).all()
            result += self.__session.query(Place).all()
            result += self.__session.query(Review).all()

        obj_dict = {}
        for obj in result:
            obj_dict["{0.__class__.__name__}.{0.id}".format(obj)] = obj
        return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """load all tables"""
        Base.metadata.create_all(self.__engine)
        scoped = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(scoped)  # make thread safe

    def close(self):
        """
        `session.remove()` will dispose the current Session if present
        which will first call `session.close()`, transactions are rolled back
        look up -> `scoped_session.remove` for refresher
        """
        self.__session.remove()
