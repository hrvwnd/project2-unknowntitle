#Imported functions 
from math import ceil #needed to round decimals to the next number 
from applicaiton import app, db
from flask import Flask, request, render_template, url_for, flash
from application.forms import GenerateIngredientsForm, RecipeNameForm, SearchForRecipe 
from application.models import Recipes
import requests
#Routes and other functions for application

@app.route("/")
@app.route("/home", methods = ["GET", "POST"])
def random_generator():
    GIform = GenerateIngredientsForm()
    recipe_name_form = RecipeNameForm()
    if GIform.is_submitted():
        recipe_response = requests.get("http://4-final-recipe-generator:5000")
        if final_recipe_parts.status_code == 200:
            list_of_ingredients_and_method = final_recipe_response
            # find out how to get the information

        

            # CHANGE ME 
            # Figure out how to display ingredients

            return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, \
                list_of_ingredients_and_method = list_of_ingredients_and_method, 
        else:
            return "404- ingredients not found"
    if recipe_name_form.validate_on_submit():
        new_recipe = Recipes(
            name = recipe_name_form.recipe_name.data
            # CHANGE ME
            # SAVE INGREDIENTS AND METHOD TO DATABASE
        )
        db.session.add(new_recipe)
        db.session.commit()
        flash ("Recipe saved")
        return render_template(url_for('recipes'))
    return render_template("home.html", title = "home", GIform = GIform)

@app.route('/recipes',methods=["GET","POST"])
def recipes():
    response = requests.get("http://") # CHANGE ME 
    form = SearchForRecipe()
    if form.validate_on_submit():
        recipe_name = recipe_name.data
        
        
        # CHANGE ME 
        # Add display table
        if # CHANGE ME 
         return render_template("recipes.html", title = "recipes")
        else:
            return "404"
    return render_template("recipes.html", title = "recipes") 


        
