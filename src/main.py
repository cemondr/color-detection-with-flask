from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_World():
    return "home page that allows uploads"

@app.route('/uploaded')
def  allow_click():
    return "page with uploaded photo"

@app.route('/result')
def get_your_result():
    return "page that returns your RGB value"



#print("eyo")