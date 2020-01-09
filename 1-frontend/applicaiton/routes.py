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
        recipe_response = requests.get("http://4-final-recipe-generator:5000")
        if final_recipe_parts.status_code == 200:
            list_of_ingredients_and_method = final_recipe_response
            # find out how to get the information

        

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


        
