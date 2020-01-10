import requests
from random import randint

# testing purposes
ingredients = ['Green Beans', 'Peppers', 'Potatoes', 'Avocado', 'Mushrooms']
ingredients2 = ['Green Beans', 'Peppers', 'Bacon', 'food']


def join_list(ingredients, method)
    print (ingredients)
    print (method)
    ingredients.append(method)
    return ingredients

# A function to find different ingredients so that the same ingredients aren't added to the list twice
def find_different_ingredients(list_of_ingredients_and_method, spare_ingredients):
    different_ingredients = list(set(spare_ingredients).difference(list_of_ingredients_and_method))
    if different_ingredients == []:
        return False
    else:
        return different_ingredients
#print (find_different_ingredients(ingredients, ingredients2))


def random_number_function(maximum):
    return randint(0,maximum-1)


# A function to remove or add a random ingredient from the ingredients list
def random_remove(list_of_ingredients_and_method, remove, spare_ingredients):
    method = list_of_ingredients_and_method[-1] # saves method before temporary removal
    list_of_ingredients_and_method.remove(list_of_ingredients_and_method[-1]) # removes method so random ingredient can be removed
    random_number = random_number_function(len(list_of_ingredients_and_method)) # randomizes a number
    if remove and remove != "replace":
        list_of_ingredients_and_method.remove(list_of_ingredients_and_method[random_number]) # removes ingredient
        list_of_ingredients_and_method.append(method) # Adds method back on to list in same position
        return list_of_ingredients_and_method

    elif not remove:
        different_ingredients = find_different_ingredients(list_of_ingredients_and_method, spare_ingredients) # ensures no repeat ingredients
        if not different_ingredients:
            return list_of_ingredients_and_method # catches unlikely event where both lists of ingredients contain the same elements
        random_number = random_number_function(len(different_ingredients))
        list_of_ingredients_and_method.append(different_ingredients[random_number])
        list_of_ingredients_and_method.append(method) # Adds method back on to the list
        return list_of_ingredients_and_method

    elif remove == "replace":
        different_ingredients = find_different_ingredients(list_of_ingredients_and_method, spare_ingredients)
        if not different_ingredients:
            return list_of_ingredients_and_method
        list_of_ingredients_and_method.remove (list_of_ingredients_and_method[random_number])
        random_number = random_number_function(len(different_ingredients))
        list_of_ingredients_and_method.append(different_ingredients[random_number])
        list_of_ingredients_and_method.append(method) # Adds method back on to the list
        return list_of_ingredients_and_method

#print (random_remove(ingredients, "replace", ingredients2))


def count_letters(list_of_ingredients_and_method):
    count = 0
    for item in list_of_ingredients_and_method:
        count += len(item)
    return count

# print (count_letters(ingredients))


# A function that factors in how long the list of ingredients is based on the length of the combined letters in all ingredients
def add_or_delete_parts(ingredients, method, spare_ingredients):
    #turns strings back into lists
    list_of_ingredients_and_method = join_list(ingredients, method)
    count = count_letters(list_of_ingredients_and_method)
    if count >=40: # If over 40 characters, remvoe an ingredient at random
        return random_remove(list_of_ingredients_and_method, True, spare_ingredients)

    elif 30 <= count < 40: # Between 30-40 keep ingredients list the same
        return list_of_ingredients_and_method

    elif 20 < count < 30: # Between 20-30, replace an ingredient in the list
        return random_remove(list_of_ingredients_and_method, "replace", spare_ingredients)

    elif count <= 20: # lower than 20, add an ingredient to the list
        return random_remove(list_of_ingredients_and_method, False, spare_ingredients)
        