#!/usr/bin/python3
"""user that holeds state of users"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines the State class

    Attributes:
        name (str) - The name of the state
    """
    name = ""
