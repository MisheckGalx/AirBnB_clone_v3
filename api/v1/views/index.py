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

@app_views.route('/stats', methods=['GET'])
def retrieve_object_number():
    """Retrieves the number of each object by type"""
    object_list = [Amenity, City, Place, Review, State, User]
    name_list = ['amenities', 'cities', 'places', 'reviews', 'states', 'users']

    object_dict = {}
    for index, object in enumerate(object_list):
        object_count = storage.count(object)
        object_dict[name_list[index]] = object_count

    return jsonify(object_dict)
