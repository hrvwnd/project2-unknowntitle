from application import app
from application.functions import method_generator
import requests

@app.route("/",methods = ["GET", "POST"])
def method_generate():
    post = method_generator()
    post = post.text
    return post

#print (method_generate())