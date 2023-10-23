from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'},
        {'first_name': 'John', 'last_name': 'Sandoval'},
    ]
    return render_template('index.html', users=users)
# @app.route('/') activates:
# def index():
#       Inside index(), there is a *list* named users. 
#       Each dictionary inside the *list* is  a user 
#       with 'first_name' and 'last_name' keys.
    # return render_template('index.html', users=users)
    # is passing the users data to HTML template

if __name__ == '__main__':
    app.run(debug=True)
