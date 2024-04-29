#!/usr/bin/python3
'''Testing the index route'''
import unittest
import pep8
from os import getenv
import requests
import json
from api.v1.app import *
from flask import request, jsonify
from models.amenity import Amenity
from models import storage


class TestAmenities(unittest.TestCase):
    '''Test amenity'''

    def test_lists_amenities(self):
        '''Test amenity GET route'''
        with app.test_client() as c:
            resp = c.get('/api/v1/amenities')
            self.assertEqual(resp.status_code, 200)
            resp2 = c.get('/api/v1/amenities/')
            self.assertEqual(resp.status_code, 200)

    def test_create_amenity(self):
        '''Test amenity POST route'''
        with app.test_client() as c:
            resp = c.post('/api/v1/amenities/',
                          data=json.dumps({"name": "treehouse"}),
                          content_type="application/json")
            self.assertEqual(resp.status_code, 201)

    def test_delete_amenity(self):
        '''Test amenity DELETE route'''
        with app.test_client() as c:
            new_amenity = Amenity(name="3 meals a day")
            storage.new(new_amenity)
            resp = c.get('api/v1/amenities/{}'.format(new_amenity.id))
            self.assertEqual(resp.status_code, 200)
            resp1 = c.delete('api/v1/amenities/{}'.format(new_amenity.id))
            self.assertEqual(resp1.status_code, 200)
            resp2 = c.get('api/v1/amenities/{}'.format(new_amenity.id))
            self.assertEqual(resp2.status_code, 404)

    def test_get_amenity(self):
        '''Test amenity GET by id route'''
        with app.test_client() as c:
            new_amenity = Amenity(name="3 meals a day")
            storage.new(new_amenity)
            resp = c.get('api/v1/amenities/{}'.format(new_amenity.id))
            self.assertEqual(resp.status_code, 200)

    def test_update_amenity(self):
        '''Test amenity PUT route'''
        with app.test_client() as c:
            new_amenity = Amenity(name="3 meals a day")
            storage.new(new_amenity)
            resp = c.put('api/v1/amenities/{}'.format(new_amenity.id),
                         data=json.dumps({"name": "2 meals a day"}),
                         content_type="application/json")
            self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
