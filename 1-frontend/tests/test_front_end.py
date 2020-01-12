import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Recipes

class UnitBase(TestCase):
    def create_app(self):
        config_name = "testing"
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':' \
                +str(getenv('MYSQL_PASSWORD'))+'@'+str(getenv('MYSQL_HOST'))+'/'+str(getenv('MYSQL_DB_TEST')))
        return app 


    def setup(self):
        #creates and drops database
        # Will be called for every test 
        db.session.commit()
        db.drop_all()
        db.create_all()

        recipe1 = Recipes(name = "Tomato Pasta", item1 = "Onions", item2 = "Carrots", item3 = "Cellary",\
             item4 = "Tomatoes", item5 ="fried", item6 = " ", item7 = " ")

        recipe2 = Recipes(name = "beef stew", item1 = "beef", item2 = "Carrots", item3 = "Cellary",\
             item4 = "Tomatoes", item5 ="Onions", item6 = "stewed", item7 = " ")
        
        recipe3 = Recipes(name = "something weird", item1 = "Peas", item2 = "Limes", item3 = "Kale",\
             item4 = "Turnip", item5 ="Boiled", item6 = " ", item7 = " ")

        db.session.add(recipe1)
        db.session.add(recipe2)
        db.session.add(recipe3)
        db.session.commit()

    def TearDown(self):
        # drops all created databases 
        print ("TESTING")
        db.session.remove()
        

        db.drop_all()

class UnitTest(UnitBase):
    # Tests for http access

    def test_home_url(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_url(self):
        response = self.client.get(url_for("recipes"))
        self.assertEqual(response.status_code, 200)