#!/usr/bin/python3
"""index module"""

from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review

# Define a dictionary mapping model classes to their corresponding names
MODEL_MAPPING = {
    Amenity: 'amenities',
    City: 'cities',
    Place: 'places',
    Review: 'reviews',
    State: 'states',
    User: 'users'
}


@app_views.route('/status')
def get_status():
    """Gets the status of the API"""
    status_check = {"status": "OK"}
    return jsonify(status_check)


@app_views.route('/stats')
def retrieve_object_number():
    """Retrieves the number of each object by type"""
    object_dict = {}

    # Iterate over the model classes and count instances
    for model_cls in MODEL_MAPPING:
        object_count = storage.count(model_cls)
        object_dict[MODEL_MAPPING[model_cls]] = object_count

    return jsonify(object_dict)
