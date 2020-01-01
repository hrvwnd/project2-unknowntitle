from random import choice, randint
import csv
import pandas as pd 
import os 

# -- Ingredients picked generator --
# Pick a random item from a list 
def random_list_item(csv_name):
    script_dir = os.path.dirname(__file__) # finds the root file path
    abs_file_path = os.path.join(script_dir, csv_name) # gives value for os to use 
    with open(abs_file_path) as f:
        reader = csv.reader(f)
        chosen_row = choice(list(reader)) # gives a random item from list
        chosen_row = str(chosen_row)[1:-1] # strips the [] from list item
        return chosen_row

#print (random_list_item("fruit_veg.csv"))

# -- Number of ingredients generator --
#  Generates a random number between 3 and 6
def random_number_generator():
    return randint(3,6)

# -- Ingredients list generator -- 
# creates a list of ingredients to be returned in a list
def list_of_ingredients():
    list_of_ingredients = []
    number_of_ingredients = random_number_generator()
    vegetarian = randint(0,1)    
    if vegetarian:
        for i in range(number_of_ingredients + 1):
            list_of_ingredients.append(random_list_item("fruit_veg.csv"))
    else: 
        list_of_ingredients.append(random_list_item("meat_fish.csv"))
        for i in range(number_of_ingredients):
            list_of_ingredients.append(random_list_item("fruit_veg.csv"))
