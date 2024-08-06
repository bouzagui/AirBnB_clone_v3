#!/usr/bin/python3
"""models doc"""
from flask import Flask
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place


@app_views.route("/status", strict_slashes="False", methods=["GET"])
def status():
    return {
        "status": "OK"
    }


app_views.route("/api/v1/stats", strict_slashes=False, methods=["GET"])


def state():
    """return stats about each class"""
    amenities = storage.count(Amenity)
    cities = storage.count(City)
    places = storage.count(Place)
    reviews = storage.count(Review)
    states = storage.count(State)
    users = storage.count(User)
    return {
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
    }
