#Imported functions 
from math import ceil #needed to round decimals to the next number 
from applicaiton import app, db
from flask import Flask, request, render_template, url_for
from application.forms import GenerateIngredientsForm, RecipeName, SearchForRecipe 
import requests
#Routes and other functions for application

@app.route('/', methods = ["GET", "POST"])
def random_generator():
    GIform = GenerateIngredientsForm()
    if GIform.is_submitted():
        ingredient_response = requests.get("http://") # CHANGE ME
        method_response = requests.get("http://") # CHAMGE ME 
        if ingredient_response.status_code == 200 and method_response.status_code == 200:
            ingredients = ingredient_response.json()
            method = method_response.json()

            # CHANGE ME 
            # Figure out how to display ingredients

            return render_template("home.html", title = "home")
        else:
            return "404"


@app.route('/recipes',methods=["GET","POST"])
def recipes():
    response = requests.get("http://") # CHANGE ME 
    form = SearchForRecipe
    if form.validate_on_submit():
        
        # CHANGE ME 
        # Add display table
        if # CHANGE ME 
         return render_template("recipes.html", title = "recipes")
        else:
            return "404"


        

# Calculator for number of ingredients required for the
# number of people the recipe needs to serve
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

