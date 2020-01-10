import requests
from application import app
from application.functions import add_or_delete_parts
from json import dumps
@app.route("/",methods = ["GET", "POST"])
def final_recipe_parts():
    ingredients_service = requests.get("http://2-ingredient-generator:5002/")
    spare_ingredients_service = requests.get("http://2-ingredient-generator:5002/")
    method_service = requests.get("http://3-method-generator:5003/")
    ingredients_service = ingredients_service.text.split(",")
    print ("TEST PRINT ")
    print (ingredients_service)
    print (spare_ingredients_service.text)
    spare_ingredients_service = spare_ingredients_service.text.split(",")
    print (spare_ingredients_service)
    method_service = method_service.text.split(",")
    post = add_or_delete_parts(ingredients_service, method_service, spare_ingredients_service)
    #post = np.asarray(post) # converts to array for json transfer
    post = dumps(post)
    return post

print (final_recipe_parts())
print (dumps(final_recipe_parts))