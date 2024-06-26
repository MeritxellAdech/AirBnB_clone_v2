""" This module instantiates an object of class DBStorage """

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Defines the class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passw = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        url = f"mysql+mysqldb://{user}:{passw}@{host}/{db}"
        # Create the engine
        self.__engine = create_engine(url, pool_pre_ping=True)
        # Check if environment = test
        if getenv("HBNB_ENV ") == "test":
            from models.base_model import Base

            # ORM way to delete all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on current db session all objects
        depending of the class name
        Args
            cls: the class name
        Return
            a dictionary"""

        objects = {}
        all_models = [cls]
        if cls is None:
            # if no class is provided, return all objects from all classes
            from console import HBNBCommand
            from models.base_model import BaseModel
            cls_values = HBNBCommand.classes.values()
            all_models = [i for i in cls_values if i != BaseModel]

        # When a class is provided, return all objects from it
        for model in all_models:
            query_obj = self.__session.query(model).all()
            for obj in query_obj:
                objects[f"{cls.__name__}.{obj.id}"] = obj
        return objects

    def new(self, obj):
        """Adds a new object to the current database session
        Args
            obj: an instance of a class"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        # ORM way to create all tables
        Base.metadata.create_all(self.__engine)
        # Creating an object of session
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Ensuring that all sessions are thread-safe
        self.__session = scoped_session(session_fac)
