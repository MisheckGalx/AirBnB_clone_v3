#!/usr/bin/python3
"""View for State objects that handles all default RESTFul API actions"""

from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states_list():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    states_list = [state.to_dict() for state in states]
    return jsonify(states_list)


@app_views.route('/states/<string:id>', methods=['GET'], strict_slashes=False)
def get_a_state(id):
    """Retrieves a State object"""
    state = storage.get(State, id)
    if state:
        return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<string:id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_a_state(id):
    """Deletes a State object"""
    state = storage.get(State, id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    request_data = request.get_json()
    if not request_data:
        return "Not a JSON", 400

    name = request_data.get("name")
    if not name:
        return "Missing name", 400

    state = State(name=name)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<string:id>', methods=['PUT'], strict_slashes=False)
def update_state(id):
    """Updates a State"""
    state = storage.get(State, id)
    if not state:
        abort(404)

    request_data = request.get_json()
    if not request_data:
        return "Not a JSON", 400

    ignore = ['id', 'created_at', 'updated_at']
    for key, value in request_data.items():
        if key not in ignore:
            setattr(state, key, value)

    storage.save()
    return jsonify(state.to_dict()), 200
