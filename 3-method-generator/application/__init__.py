from flask import Flask
from os import getenv
import requests

app = Flask(__name__)

from application import routes