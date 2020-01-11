#Imported functions 
from math import ceil #needed to round decimals to the next number 
from application import app, db
from flask import Flask, request, render_template, url_for, flash, redirect
from application.forms import GenerateIngredientsForm, RecipeNameForm, SearchForRecipe 
from application.models import Recipes
import requests
#Routes and other functions for application

@app.route("/")
@app.route("/home", methods = ["GET", "POST"])
def home():
    GIform = GenerateIngredientsForm()
    recipe_name_form = RecipeNameForm()
    list_of_ingredients_and_method = ["Press Generate button to create a potential recipe"]
    if GIform.is_submitted():
        recipe_response = requests.get("http://4-final-recipe-generator:5004/") 

        if recipe_response.status_code == 200:
            recipe_response = recipe_response.text
            recipe_response = eval(str(recipe_response))
            list_of_ingredients_and_method = recipe_response
            return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, list_of_ingredients_and_method = list_of_ingredients_and_method)
            
        else:
            return "404- ingredients not found"
        """
        if request.method == "GET":
           return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, \
           list_of_ingredients_and_method = list_of_ingredients_and_method) 
           
        """

    if recipe_name_form.validate_on_submit():
        print ("-----------------------------------------READ ME --------------------------")
        print (list_of_ingredients_and_method)
        if list_of_ingredients_and_method == ["Press Generate button to create a potential recipe"]:
            return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, list_of_ingredients_and_method = ["You need to generate recipes first"])

        while len(list_of_ingredients_and_method) < 7: # adds empty elements to the list if not at max length
            list_of_ingredients_and_method.append(" ")
        print ("------------------------------READ ME ---------------------------------")
        print ("making sure theres 7 items in list")
        print (len(list_of_ingredients_and_method))
        print (list_of_ingredients_and_method)
        new_recipe = Recipes(
            name = recipe_name_form.recipe_name.data,
            item1 = list_of_ingredients_and_method[0],
            item2 = list_of_ingredients_and_method[1],
            item3 = list_of_ingredients_and_method[2],
            item4 = list_of_ingredients_and_method[3],
            item5 = list_of_ingredients_and_method[4],
            item6 = list_of_ingredients_and_method[5],
            item7 = list_of_ingredients_and_method[6]
        )
        db.session.add(new_recipe)
        db.session.commit()
        flash ("Recipe saved" + str(recipe_name_form.recipe_name.data))
        return render_template(url_for('recipes'))

    return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, \
        list_of_ingredients_and_method = list_of_ingredients_and_method)

@app.route('/recipes',methods=["GET","POST"])
def recipes():
    form = SearchForRecipe()
    if form.validate_on_submit():
        recipe_name = recipe_name.data
        query = Recipes.query.filter_by(name = recipe_name).all()
        return render_template("recipes.html", title= "recipes", form = form, \
            results = query)
    return render_template("recipes.html", title = "recipes", form=form) 


        
