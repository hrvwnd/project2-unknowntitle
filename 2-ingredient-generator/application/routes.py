from application import app 
from application.functions import random_list_item, random_number_generator, \
    vegetarian, list_of_ingredients
import numpy as np

@app.route('/', methods=["GET", "POST"])
def generate_recipe_ingredients():
    post = list_of_ingredients()
    post = np.asarray(mylist)
    return post

#print (generate_recipe_ingredients())