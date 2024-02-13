#!/usr/bin/python3
"""User calsss that stor user information"""
from models.base_model import BaseModel


class User(BaseModel):
    """class declaration"""

    """User class that defines User information

    Attributes:
        email (str) - Email of the user
        password (str) - Password of the user
        first_name (str) - First name of the user
        last_name (str) - Last name of the user
        """

    password = ""
    first_name = ""
    last_name = ""

