from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'JohnSandoval'

# This must be a GET because it will not allowed us to revisit our 
# empty form.html when we click "return to form" from results
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Store form data in session
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['language'] = request.form['language']
        # Checkbox, this was a headache to get set up. 
        session['having_fun'] = 'Yes' if 'having_fun' in request.form else 'No'
        # Radio buttons
        session['color'] = request.form.get('color', 'No choice')
        return redirect(url_for('result'))
    return render_template('form.html')

@app.route('/result')
def result():
    # "GET" the form data from session OR the default values
    name = session.get('name', 'No data')
    email = session.get('email', 'No data')
    language = session.get('language', 'No data')
    having_fun = session.get('having_fun', 'User is not having fun')
    color = session.get('color', 'No choice')
    return render_template('result.html', name=name, email=email, language=language, having_fun=having_fun, color=color)

if __name__ == '__main__':
    app.run(debug=True)

