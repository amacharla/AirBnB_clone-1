#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State

all_states = storage.all(State)
for state in all_states.values():
    print(state.id, state.name)
