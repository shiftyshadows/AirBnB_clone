#!/usr/bin/python3
""" This module defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel """
    email = None
    password = None
    first_name = None
    last_name = None

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
