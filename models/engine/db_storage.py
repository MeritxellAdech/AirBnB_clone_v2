""" This module instantiates an object of class DBStorage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """ Defines the class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        url = f"mysql+mysqldb://{user}:{passw}@{host}/{db}"
        # Create the engine
        self.__engine = create_engine(url, pool_pre_ping=True)
        # Check if environment = test
        if getenv('HBNB_ENV ') == 'test':
            # ORM way to delete all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries on current db session all objects
        depending of the class name
        Args
            cls: the class name
        Return
            a dictionary"""

        if cls is None:
            # if no class is provided, return all objects from all classes
            return self.__session.query(cls).all()

        # When a class is provided, return all objects from it
        query_obj = self.__session.query(cls).all()
        objects = {}
        for obj in query_obj:
            objects[obj.id] = obj
        return objects

    def new(self, obj):
        """ Adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        # ORM way to create all tables
        Base.metadata.create_all(self.__engine)
        # Creating an object of session
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Ensuring that all sessions are thread-safe
        self.__session = scoped_session(session_fac)
