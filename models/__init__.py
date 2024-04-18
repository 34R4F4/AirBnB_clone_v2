#!/usr/bin/python3
"""Instantiate a storage object based on environment variable."""

import os

storage_type = os.environ.get("HBNB_TYPE_STORAGE")

# Select storage type based on environment variable
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload storage data
storage.reload()
