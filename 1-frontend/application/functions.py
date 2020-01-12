from math import ceil #needed to round decimals to the next number
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Recipes, Ingredients, Methods

# Calculator for number of ingredients required for the
# number of people the recipe needs to serve
# Not used right now but useful for future feature of app 
def ingredient_quanity(number_of_people_to_serve, default_quantity_of_food):
    # by default the number of people a meal will serve is 2
    if number_of_people_to_serve == 2: # if people to serve is 2: return the defauly quantity
        return default_quantity_of_food
    # if the required amount of ingredients is a whole number return the amount 
    elif (number_of_people_to_serve * default_quantity_of_food /2).is_integer(): 
        return number_of_people_to_serve * default_quantity_of_food / 2
    #if the amount of ingredients is not a whole number, round up to nearest amount 
    else: 
        return ceil(number_of_people_to_serve * default_quantity_of_food / 2)

def remake_db():
    #creates and drops database
    # Will be called for every test 

    db.session.commit()
    db.drop_all()
    db.create_all()

    recipe_1 = Recipes(name = "Tomato Pasta", item1 = "Onions", item2 = "Carrots", item3 = "Cellary", item4 = "Tomatoes", item5 ="fried", item6 = " ", item7 = " ")

    db.session.add(recipe_1)
    db.session.commit()