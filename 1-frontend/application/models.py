from application import db

class Recipes(db.Model):
        id = db.Column(db.Integer, primary_key=True, unique = True)
        name = db.Column(db.String(30), nullable=False, unique= True)
        item1 = db.Column(db.String(15), nullable=True, unique= True)
        item2 = db.Column(db.String(15), nullable=True, unique= True)
        item3 = db.Column(db.String(15), nullable=True, unique= True)
        item4 = db.Column(db.String(15), nullable=True, unique= True)
        item5 = db.Column(db.String(15), nullable=True, unique= True)
        item6 = db.Column(db.String(15), nullable=True, unique= True)
        item7 = db.Column(db.String(15), nullable=True, unique= True)
        item8 = db.Column(db.String(15), nullable=True, unique= True)

class Ingredients(db.Model):

        id = db.Column(db.Integer, primary_key=True, unique = True)
        ingredient = db.Column(db.String(15), nullable=False, unique= True)

class Methods(db.Model):
        
        id = db.Column(db.Integer, primary_key=True, unique = True)
        method = db.Column(db.String(15), nullable=False, unique= True)