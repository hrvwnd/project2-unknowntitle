from application import db

class Recipes(db.Model):
        id = db.Column(db.Integer, primary_key=True, unique = True)
        name = db.Column(db.String(30), nullable=False, unique= True)
        item1 = db.Column(db.String(30), nullable=True, unique= False)
        item2 = db.Column(db.String(30), nullable=True, unique= False)
        item3 = db.Column(db.String(30), nullable=True, unique= False)
        item4 = db.Column(db.String(30), nullable=True, unique= False)
        item5 = db.Column(db.String(30), nullable=True, unique= False)
        item6 = db.Column(db.String(30), nullable=True, unique= False)
        item7 = db.Column(db.String(30), nullable=True, unique= False)