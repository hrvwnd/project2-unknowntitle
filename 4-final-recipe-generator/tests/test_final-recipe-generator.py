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
        self.assertTrue(3 <= len(functions.add_or_delete_parts(ingredients,method,spare_ingredients)) <=8 )

    def test_join_list(self):
        ingredients = ["Beef", "Tomatoes", "Onions", "Cabbage"]
        method = "test"
        self.assertEqual(functions.join_list(ingredients, method), ["Beef", "Tomatoes", "Onions", "Cabbage", "test"])

    def test_find_different_ingredients(self):
        list_of_ingredients_and_method = ["Beef", "Tomatoes", "Onions", "Cabbage"]
        spare_ingredients = ["Beef", "Tomatoes", "Onions", "test"]
        self.assertEqual(functions.find_different_ingredients(list_of_ingredients_and_method,spare_ingredients),["test"])
    
    def test_random_remove_remove(self):
        list_of_ingredients_and_method = ["Beef", "Tomatoes", "Onions", "Cabbage"]
        length = len(list_of_ingredients_and_method)
        remove = True
        spare_ingredients = ["test"]
        removed_list = functions.random_remove(list_of_ingredients_and_method, remove, spare_ingredients)
        len_removed_list = len(removed_list)

        self.assertTrue(length - len_removed_list == 1)

    def test_random_remove_add(self):
        list_of_ingredients_and_method = ["Beef", "Tomatoes", "Onions", "Cabbage"]
        length = len(list_of_ingredients_and_method)
        remove = False
        spare_ingredients = ["test"]
        added_list = functions.random_remove(list_of_ingredients_and_method, remove, spare_ingredients)
        len_added_list = len(added_list)

        self.assertTrue(length - len_added_list == -1) and self.assertTrue(added_list,["Beef", "Tomatoes", "Onions", "Cabbage", "test"])

    def test_random_remove_replace(self):
        list_of_ingredients_and_method = ["Beef", "Tomatoes", "Onions", "Cabbage"]
        length = len(list_of_ingredients_and_method)
        remove = "replace"
        spare_ingredients = ["test"]
        added_list = functions.random_remove(list_of_ingredients_and_method, remove, spare_ingredients)
        len_added_list = len(added_list)

        self.assertTrue(length - len_added_list == 0)

    def test_count_letters(self):
        list_of_ingredients_and_method = ["one","two","three"]
        self.assertEqual(functions.count_letters(list_of_ingredients_and_method),11)

    def test_add_or_delete_parts_morethan40(self):
        ingredients = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","b"]
        method = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        spare_ingredients = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
        self.assertTrue(len(routes.add_or_delete_parts(ingredients, method, spare_ingredients)),1)

    def test_add_or_delete_parts_30_40(self):
        ingredients = ["aaaaaaaaaaaaaaaaaaaaaaaaaaa","bbbbbbbbbb"]
        method = "aaaaaa"
        spare_ingredients = ["a"]
        self.assertTrue(len(routes.add_or_delete_parts(ingredients, method, spare_ingredients)),2)


    def test_add_or_delete_parts_20_40(self):
        ingredients = ["aaaaaaaaaa","bbbbbb"]
        method = "aaaaaa"
        spare_ingredients = ["c"]
        self.assertTrue(len(routes.add_or_delete_parts(ingredients, method, spare_ingredients)),2)

    def test_add_or_delete_parts_lessthan20(self):
        ingredients = ["aaaa","bbbb"]
        method = "cccc"
        spare_ingredients = ["dddd"]
        self.assertTrue(len(routes.add_or_delete_parts(ingredients, method, spare_ingredients)),3) and self.assertTrue(routes.add_or_delete_parts(ingredients, method, spare_ingredients),["aaaa","bbbb","cccc","dddd"])