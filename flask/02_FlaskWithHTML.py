from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello this is my Flask home page</h1>'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index1', methods=['GET'])
def index1():
    return render_template('index01.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug = True)