from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def checkerboard_colorschanges(x, y, color1, color2):
    return render_template("checkerboard.html", rows=x, columns=y, color1=color1, color2=color2)
# x: The number of rows in the checkerboard from the URL
# y: The number of columns in the checkerboard from the URL
# color1: The (bg)color for even cells
# color2: The color for odd cells
# renders "checkerboard.html" template with these *parameters*

if __name__ == "__main__":
    app.run(debug=True)
