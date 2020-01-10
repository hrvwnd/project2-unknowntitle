from random import randint

# Random method of cooking generator 
def method_generator():
    list_of_methods = ["Fried", "Roasted", "Boiled", "Steamed", "Grilled", "Baked", "Stewed"]
    random_number = randint(0,len(list_of_methods)-1)
    #print (random_number)
    #print (random_number)
    method = list_of_methods[random_number]
    return method
#print (method_generator())