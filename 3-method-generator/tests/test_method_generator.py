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

    def test_method_generate(self):
        list_of_methods = ["Fried", "Roasted", "Boiled", "Steamed", "Grilled", "Baked", "Stewed"]
        method = routes.method_generate()

        self.assertIn(method, list_of_methods)


        