from math import ceil #needed to round decimals to the next number


# Calculator for number of ingredients required for the
# number of people the recipe needs to serve
def ingredient_quanity(number_of_people_to_serve, default_quantity_of_food):
    # by default the number of people a meal will serve is 2
    if number_of_people_to_serve == 2: # if people to serve is 2: return the defauly quantity
        return default_quantity_of_food
    # if the required amount of ingredients is a whole number return the amount 
    elif (number_of_people_to_serve * default_quantity_of_food /2).is_integer(): 
        return number_of_people_to_serve * default_quantity_of_food / 2
    #if the amount of ingredients is not a whole number, round up to nearest amount 
    else: 
        return ceil(number_of_people_to_serve * default_quantity_of_food / 2)

