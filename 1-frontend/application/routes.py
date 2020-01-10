#Imported functions 
from math import ceil #needed to round decimals to the next number 
from application import app, db
from flask import Flask, request, render_template, url_for, flash
from application.forms import GenerateIngredientsForm, RecipeNameForm, SearchForRecipe 
from application.models import Recipes
import requests
#Routes and other functions for application

@app.route("/")
@app.route("/home", methods = ["GET", "POST"])
def home():
    GIform = GenerateIngredientsForm()
    recipe_name_form = RecipeNameForm()
    if GIform.is_submitted():
        recipe_response = requests.get("http://4-final-recipe-generator:5004")
        
        if recipe_response.status_code == 200:
            list_of_ingredients_and_method = recipe_response
            return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, \
                list_of_ingredients_and_method = list_of_ingredients_and_method)
        else:
            return "404- ingredients not found"

    if recipe_name_form.validate_on_submit():
        new_recipe = Recipes(
            name = recipe_name_form.recipe_name.data
            # CHANGE ME
            # SAVE INGREDIENTS AND METHOD TO DATABASE
        )
        #db.session.add(new_recipe)
        #db.session.commit()
        flash ("Recipe saved" + str(name))
        return render_template(url_for('recipes'))

    return render_template("home.html", title = "home", GIform = GIform, recipe_name_form= recipe_name_form)


@app.route('/recipes',methods=["GET","POST"])
def recipes():
    #response = requests.get("http://") # CHANGE ME 
    form = SearchForRecipe()
    if form.validate_on_submit():
        recipe_name = recipe_name.data
        query = Recipes.query.filter_by(name = recipe_name).all()
        return render_template("recipes.html", title= "recipes", form = form, \
            results = query)
    return render_template("recipes.html", title = "recipes", form=form) 


        
