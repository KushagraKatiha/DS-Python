from flask import Flask, redirect, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello this is my Flask home page</h1>'

@app.route('/index', methods=['GET'])
def index():
    return '<h2>Hello this is my Flask index page</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
