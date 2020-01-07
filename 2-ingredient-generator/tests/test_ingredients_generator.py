import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db, functions

class TestBase(TeastCase):

    def create_app(self):
        config_name = "testing"
        return app 

class TestServiceFunction(TestBase):

    def test_ingredients_generate(self):
        # CHANGE ME 
        