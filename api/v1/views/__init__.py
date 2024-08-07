#!/usr/bin/python3
"""models doc"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__)

# Import views after the Blueprint is created
from api.v1.views.index import *
from api.v1.views.states import *
