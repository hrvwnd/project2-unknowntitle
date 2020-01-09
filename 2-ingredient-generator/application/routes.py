from applicaiton import app 
from application.functions import random_list_item, random_number_generator, \
    vegetarian, list_of_ingredients

@app.route('/', method=["GET", "POST"])
def generate_recipe_ingredients():
    post = list_of_ingredients()
    return post

#print (generate_recipe_ingredients())