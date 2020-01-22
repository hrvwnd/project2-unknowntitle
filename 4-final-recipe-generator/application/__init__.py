from flask import Flask
from os import getenv
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
import requests

app = Flask(__name__)


xray_recorder.configure(service='4-final-recipe-generator', dynamic_naming='*18.130.174.90*')
XRayMiddleware(app, xray_recorder)

from application import routes