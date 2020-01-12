import unittest, pytest, json
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, functions, routes

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app 

'''
# Cant test without faking responses
class TestServiceRoutes(TestBase):

    def test_final_recipe_parts(self):
        ingredients= routes.final_recipe_parts()

        ingredients = eval(ingredients)
        print (ingredients)
        for i in ingredients:
            print(i)
        self.assertTrue(3 <= len(ingredients) <=8)
'''    

class TestServiceFunctions(TestBase):

    def test_add_or_delete_parts(self):
        ingredients = ["Beef", "Tomatoes", "Onions", "Cabbage"]
        method = "Grilled"
        spare_ingredients = ["Beef","Onions","Olives","Pork","Red Cabbage","Brussels"]
        self.assertTrue(3 <= functions.add_or_delete_parts(ingredients,method,spare_ingredients) <=8 )
        