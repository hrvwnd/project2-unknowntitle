from application import db

class Recipes(db.mode):
        id = db.Column(db.Integer, primary_key=True, unique = True)
        name = db.Column(db.String(100), nullable=False, unique= True)
        ingredient...
