from flask import Flask, request, render_template, redirect, url_for, jsonify

# Building url Dynamically
# Variable Rule
# Jinja 2 Template Engine

'''
    {{ }} expressions to print output in html
    {% %} conditions, for loops
    {# #} this is for comments
'''

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello you are at home !!'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    else:
        return render_template('form.html')


# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f'Hello {name}'
#     else:
#         return render_template('form.html')

# variable rule

@app.route('/success/<int:score>', methods=['GET', 'POST'])
def success(score):
    res = ''
    if score >= 50:
        res = f'Passed'
    elif score < 0:
        res = f'{score} marks is not a valid score'
    else:
        res = f'Failed'

    return render_template('result.html', results=res)

@app.route('/successres/<int:score>', methods=['GET', 'POST'])
def successres(score):
    res = ''
    if score >= 50:
        res = f'Passed'
    elif score < 0:
        res = f'{score} marks is not a valid score'
    else:
        res = f'Failed'

    exp = {'score': score, 'res': res}

    return render_template('result1.html', results=exp)


@app.route('/successif/<int:score>', methods=['GET', 'POST'])
def successif(score):
    res = 'Your results are as follows !'

    exp = {'score': score, 'res': res}

    return render_template('result2.html', results=exp)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        math = float(request.form['maths'])
        science = float(request.form['science'])
        ml = float(request.form['ml'])

        total_avg_score = (math+science+ml)/3

        return redirect(url_for('score_card',name=name, avg=total_avg_score))
        # return redirect(url_for('successif', score = total_avg_score))
    else:
        return render_template('scores.html')

@app.route('/score_card', methods=['GET'])
def score_card():
    name=request.args.get('name')
    avg = float(request.args.get('avg'))
    result = {'name': name, 'avg': avg}
    return render_template('score_card.html', results = result)

if __name__ == '__main__':
    app.run(debug=True)
