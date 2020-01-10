#from application import app
#from application.functions import method_generator
from functions import method_generator
#@app.route("/",methods = ["GET", "POST"])

def method_generate():
    post = method_generator()
    return post

#print (method_generate())