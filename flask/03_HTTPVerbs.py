from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<body style='background-color:#000000'><h1 style='color:#ffffff'>hello</h1></body>"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}'
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)