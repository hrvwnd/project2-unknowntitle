import unittest, pytest, json
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, functions, routes

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app 

class TestServiceRoutes(TestBase):

    def test_ingredients_generate(self):
        pass 


        
        