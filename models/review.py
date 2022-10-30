#!/usr/bin/python3

"""
    Defines a class Review.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
