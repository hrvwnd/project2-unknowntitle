from application import app
from application.functions import add_or_delete_parts

@app.route("/",methods = ["GET", "POST"])
def final_recipe_parts():
    ingredients_service = "http://2-ingredient-generator:5000/"
    method_service = "http://3-method-generator:5000/"
    post = add_or_delete_parts(ingredients_service, method_service)
    return post