# Import necessary modules
from flask import Flask, render_template, request, redirect, session
import random
import datetime

# Create a Flask web application
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define a function to update the user's gold and log their activities
def update_gold(activity):
    # Check if 'gold' and 'activities' are not in the session, initialize if not
    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = []

    # Dictionary to map activities to earnings
    activity_earnings = {
        'farm': random.randint(10, 20),
        'cave': random.randint(10, 20),
        'house': random.randint(10, 20),
        'casino': random.randint(-50, 50)
    }

    # Update the user's gold based on the selected activity
    earnings = activity_earnings.get(activity, 0)
    session['gold'] += earnings

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the activity and color-code based on earnings/losses
    if earnings >= 0:
        log_entry = f'Earned {earnings} gold from the {activity}! ({timestamp})'
        session['activities'].insert(0, {'message': log_entry, 'class': 'text-success'})
    else:
        log_entry = f'Lost {abs(earnings)} gold from the {activity}! ({timestamp})'
        session['activities'].insert(0, {'message': log_entry, 'class': 'text-danger'})

    # Increment 'moves'
    if 'moves' not in session:
        session['moves'] = 0
    session['moves'] += 1

    # Check for win/loss conditions
    if session['gold'] >= 200:
        session['game_result'] = 'win'
    elif session['moves'] >= 15:
        session['game_result'] = 'lose'

# Define the root route to render the main game page
@app.route('/')
def index():
    if 'moves' not in session:
        session['moves'] = 0
    if 'game_result' not in session:
        session['game_result'] = None
    return render_template('index.html')

# Define the '/process_money' POST route to process user actions
@app.route('/process_money', methods=['POST'])
def process_money():
    # Get the selected activity from the form
    activity = request.form['activity']

    # Check if the game has already been won or lost
    if session['game_result'] == 'win' or session['game_result'] == 'lose':
        return redirect('/')

    # Update the user's gold and log the activity
    update_gold(activity)

    # Check for win/loss conditions after updating
    if session['gold'] >= 200:
        session['game_result'] = 'win'
    elif session['moves'] >= 15:
        session['game_result'] = 'lose'

    # Redirect back to the main game page
    return redirect('/')

# Define the '/reset' route to reset the game
@app.route('/reset')
def reset():
    # Clear the session data to reset the game
    session.clear()

    # Redirect back to the main game page
    return redirect('/')

# Start the Flask app if this script is run
if __name__ == '__main__':
    app.run(debug=True)
