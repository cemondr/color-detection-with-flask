from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html', status=None)

@app.route('/uploaded')
def  allow_click():
    return render_template('main.html',status="uploaded")

@app.route('/resulted')
def get_your_result():
    return render_template('main.html', status="resulted")



#print("eyo")