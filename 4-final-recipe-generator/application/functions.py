#import requests


def join_list(list_of_ingredients, method_of_cooking):
    list_of_ingredients.append(method_of_cooking)
    return list_of_ingredients

def count_letters(list_of_ingredients_and_method):
    pass
    # CHANGE ME 
    # make function to count the number of letters in a list



def add_or_delete_parts(ingredients, method):
    list_of_ingredients_and_method = join_list(ingredients, method)
    number_of_letters = count_letters(list_of_ingredients_and_method)
    # CHANGE ME 
    # Add code for logic on either adding, removing or changing one ingredients based on 
    # length of the string


ingredients = ['Green Beans', 'Peppers', 'Potatoes', 'Avocado', 'Mushrooms']
print (ingredients[1])
ingredients.append('stewed')
print (ingredients)