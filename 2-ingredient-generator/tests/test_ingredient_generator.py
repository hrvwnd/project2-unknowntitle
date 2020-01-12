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
        ingredients = routes.generate_recipe_ingredients()
        ingredients = eval(ingredients)
        print (ingredients)
        for i in ingredients:
            print(i)
        self.assertTrue(3 <= len(ingredients) <7)


class TestServiceFunction(TestBase):

    # test_random_list_item requires a csv to test with

    # test_random_number_generator() not possible without statistical analysis
    def test_random_number_generator_range():
        random_number = routes.random_number_generator()
        self.assertTrue(3 <= random_number <7)

    def test_vegetarian():
        assert.assert routes.vegetarian() == True or routes.vegetarian() == False
    



        