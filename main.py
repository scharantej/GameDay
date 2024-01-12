 
# Import necessary libraries
from flask import Flask, render_template, request
import requests

# Create a Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Get the user's country from the request
    country = request.args.get('country')

    # If no country is provided, default to the United States
    if not country:
        country = 'US'

    # Get the list of football games airing on TV today in the specified country
    games = get_games(country)

    # Render the home page, passing the list of games as a variable
    return render_template('index.html', games=games)

# Define the route for the game details page
@app.route('/game/<game_id>')
def game_details(game_id):
    # Get the details of the specified game
    game = get_game_details(game_id)

    # Render the game details page, passing the game details as a variable
    return render_template('game_details.html', game=game)

# Function to get the list of football games airing on TV today in the specified country
def get_games(country):
    # Make a request to the API
    response = requests.get('https://www.example.com/api/games', params={'country': country})

    # Parse the JSON response
    data = response.json()

    # Return the list of games
    return data['games']

# Function to get the details of the specified game
def get_game_details(game_id):
    # Make a request to the API
    response = requests.get('https://www.example.com/api/games/' + game_id)

    # Parse the JSON response
    data = response.json()

    # Return the game details
    return data['game']

# Run the app
if __name__ == '__main__':
    app.run()
