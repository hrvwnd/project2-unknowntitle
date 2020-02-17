from application import app, db

def findmethodfromdb(recipe):
    methods = ["Fried", "Roasted", "Boiled", "Steamed", "Grilled", "Baked", "Stewed"] 
    for i in range(len(methods)):
        recipe = Recipes.query.filter_by()
        