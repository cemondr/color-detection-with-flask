from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_World():
    return "This is going to be a web program"

#print("eyo")