from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/uploaded')
def  allow_click():
    return "page with uploaded photo"

@app.route('/result')
def get_your_result():
    return "page that returns your RGB value"



#print("eyo")