import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import # CHANGE ME 

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

        # CHANGE ME 
        # Add create test tables 

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