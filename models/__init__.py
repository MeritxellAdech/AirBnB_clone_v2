"""This file will handle the conditional import and instantiation
based on the HBNB_TYPE_STORAGE environment variable"""
#!/usr/bin/python3
from os import getenv

# Check the value of the environment variable
storage_type = getenv('HBNB_TYPE_STORAGE')
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

