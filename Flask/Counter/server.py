from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Get the visit count from cookies or set it to 0 if not present, removing the zero
    # does not allow us to start the page.
    visit_count = int(request.cookies.get('visit_count', 0))
    # Increment the visit count by 1 on every open (or refresh) of the page
    visit_count += 1
    # Create a response with an HTML template, passing the visit count as a variable
    response = make_response(render_template('index.html', visit_count=visit_count))
    # Set the updated visit count in cookies !!! Very important, NEW !!!
    response.set_cookie('visit_count', str(visit_count))
    # Return the response to the client
    return response

# Resetting the visit count
@app.route('/destroy_session')
# Have the reset button follow the same "def reset()" function as /destroy_session
@app.route('/reset')
def reset():
    # Delete the visit count cookie 
    response = make_response(redirect('/'))
    response.delete_cookie('visit_count')
    # Redirect the client back to the root URL 
    return response

# Increment the visit count by 2
@app.route('/add_2')
def add_2():
    # Get the visit count from prior cookies or set it to 0 if not present as before
    visit_count = int(request.cookies.get('visit_count', 0))
    # Increment the visit count by 2 ( I said "+= 1" 
    # accounting for the automatic +1 due to refresh, both of these make for +2)
    visit_count += 1
    # Create a response that redirects to the root URL
    response = make_response(redirect('/'))
    # Set the updated visit count in cookies
    response.set_cookie('visit_count', str(visit_count))
    # Return the response to the client
    return response

# Increment the visit count via input box
@app.route('/increment', methods=['GET'])
def increment():
    # Get the increment value from the form input or use 1 as the default
    increment_value = int(request.args.get('increment_value', 1))
    # Get the visit count from cookies or set it to 0 if not present
    visit_count = int(request.cookies.get('visit_count', 0))
    # Increment the total in visit count by the specified 
    # increment value (minus 1 to account for automatic +1, similair to 
    # the increment +2 feature)
    visit_count += increment_value - 1
    # Create a response that redirects to the root URL
    response = make_response(redirect('/'))
    # Set the updated visit count in cookies
    response.set_cookie('visit_count', str(visit_count))
    # Return the response to the client
    return response

if __name__ == '__main__':
    app.run(debug=True)

