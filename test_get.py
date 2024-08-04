#!/usr/bin/python3
from models import storage 
from models.state import State

state = storage.get(State, "421a55f4-7d82-47d9-b54c-a76916479545")
print(state.name)