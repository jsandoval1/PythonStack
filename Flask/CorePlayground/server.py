from flask import Flask, render_template
# Imports the Flask class and  render_template function from flask.
# The Flask class is used to create Flask application (below)
# render_template is used to give access to connected HTML templates

app = Flask(__name__)

@app.route('/play/<int:x>/<color>')
# The <int:x> part captures an integer (MUST BE INT BECAUSE OF <int>) parameter named "x"
# <color> captures a parameter named "color"
def play(x, color):
    return render_template('CorePlayground.html', num_boxes=x, box_color=color)
# Passes two variables to the template 'CorePlayground.html' : 
# "num_boxes" with the value of x
# "box_color" with the value of color

if __name__ == '__main__':
    app.run(debug=True)
# Enables debug mode

