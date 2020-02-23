#Imported functions 
from math import ceil #needed to round decimals to the next number 
from application import app, db
from flask import Flask, request, render_template, url_for, flash, redirect
from application.forms import GenerateIngredientsForm, RecipeNameForm, SearchForRecipe, UpdateForm, DeleteForm
from application.models import Recipes, Users
import requests
#Routes and other functions for application


#--------------------------- Generator --------------------------- 
#---------------------------------------------------------------
@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])
def home():
    GIform = GenerateIngredientsForm()
    recipe_name_form = RecipeNameForm()
    list_of_ingredients_and_method = ["Press Generate button to create a potential recipe"]
    
    if GIform.is_submitted():
        recipe_response = requests.get("http://4-final-recipe-generator:5004/") 
        if recipe_response.status_code == 200:
            recipe_response = recipe_response.text
            recipe_response = eval(recipe_response)
            list_of_ingredients_and_method = recipe_response
            print (list_of_ingredients_and_method)

            if recipe_name_form.validate_on_submit():

                if list_of_ingredients_and_method == ["Press Generate button to create a potential recipe"] \
                    or list_of_ingredients_and_method == ["You need to generate recipes first"]: 
                    return render_template("home.html", title = "home", GIform = GIform, recipe_name_form = recipe_name_form, \
                        list_of_ingredients_and_method = ["You need to generate recipes first"])

                while len(list_of_ingredients_and_method) < 7: # adds empty elements to the list if not at max length
                    list_of_ingredients_and_method.append(" ")
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
                return redirect(url_for('recipes'))

            return render_template("home.html", title = "Recipe Generator", GIform = GIform, recipe_name_form = recipe_name_form, \
                list_of_ingredients_and_method = list_of_ingredients_and_method)   

        else:
            return "404- ingredients not found"

        return render_template("home.html", title = "Recipe Generator", GIform=GIform, recipe_name_form = recipe_name_form, \
            list_of_ingredients_and_method = list_of_ingredients_and_method) 

    return render_template("home.html", title = "Recipe Generator", GIform = GIform, recipe_name_form = recipe_name_form, \
        list_of_ingredients_and_method = list_of_ingredients_and_method)


#--------------------------- Recipes --------------------------- 
#---------------------------------------------------------------
###### Search for Recipes ######
@app.route('/recipes',methods=["GET","POST"])
def recipes():
    form = SearchForRecipe()
    RecipeData = Recipes.query.all()

    if form.validate_on_submit():
        name = form.recipe_name.data
        query = Recipes.query.filter_by(name = name).all()
        print (query)
            
        return render_template("recipes.html", title= "Recipes", form = form, \
            results = query)

    return render_template("recipes.html", title = "Recipes", form=form, results = RecipeData) 

###### Update Method ######
@app.route('/update', methods = ['GET', 'POST'])
def updaterecipe():
    updateform = UpdateForm()
    info = "Search for a recipe to rename"

    if updateform.validate_on_submit():
        name = updateform.oldrecipe_name.data
        newname = updateform.recipe_name.data
        recipe = Recipes.query.filter_by(name = name).first()
        recipe.name = newname
        db.session.commit()
        info = str(name) + " has been renamed to: " + str(newname)

        return render_template("update.html", title= "Update Recipe Name", updateform = updateform, info = info)

    return render_template("update.html", title= "Update Recipe Name", updateform = updateform, info = info)

###### Delete Recipe ######
# You might need to add name to the render_template. Test it first to see if it works.
@app.route('/delete', methods = ['GET', 'POST'])
def deleterecipe():
    deleteform = DeleteForm()
    info = "Enter a Recipe to Delete"

    if deleteform.validate_on_submit():
        name = deleteform.deleterecipe.data
        confirm  = deleteform.confirmdelete.data

        if confirm == 1 or confirm == "Confirm":
            recipe = Recipes.query.filter_by(name = name).delete()
            db.session.commit()
            info = str(name) + " has been deleted"
            return render_template("delete.html", title= "Delete Recipe", deleteform = deleteform, info = info)
        
        else:
            info = "You must select 'Confirm' to delete " + str(name)
            return render_template("delete.html", title= "Delete Recipe", deleteform = deleteform, info = info)
    
    return render_template("delete.html", title= "Delete Recipe", deleteform = deleteform, info = info)


#--------------------------- Account (will add in future update) --------------------------- 
#---------------------------------------------------------------
"""
@app.route('/register', methods = ["GET","POST"])
def register():
    form = RegistrationForm
    """
"""
@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm
   """     
