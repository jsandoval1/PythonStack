from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'John'  # Change this to a strong, unique key

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = 89
        session['attempts'] = 0
        session['message'] = ''
        session['message_class'] = ''  # Initialize message_class

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        if guess < session['number']:
            session['message'] = 'Too low'
            session['message_class'] = 'too-low'  # Set the appropriate message class
        elif guess > session['number']:
            session['message'] = 'Too high'
            session['message_class'] = 'too-high'  # Set the appropriate message class
        else:
            session['message'] = 'Correct!'
            session['message_class'] = 'correct'  # Set the appropriate message class

    if session['attempts'] >= 5:
        session['message'] = 'You Lose'

    return render_template('index.html', message=session['message'], message_class=session['message_class'], attempts=session['attempts'])  # Pass attempts to the template

@app.route('/reset', methods=['GET', 'POST'])  # Allow GET requests for resetting
def reset():
    session.pop('number', None)
    session.pop('attempts', None)
    session.pop('message', None)
    session.pop('message_class', None)  # Remove the message_class from the session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

