#store standard routes for website
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Game
from . import db
import json
import datetime

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
# @login_required
def home():
    # FIXME: currently there is HTML content in `base.html` that requires the home view
    if request.method=='POST':
        name = request.form.get('gameName')
        sportSelect = request.form.get('sportSelect')
        currNumPeople = request.form.get('currNumPeople')
        totalNumPeople = request.form.get('totalNumPeople')
        eventDateTime = request.form.get('dateTime')
        print(eventDateTime)
        eventDateTime = datetime.datetime.fromisoformat(eventDateTime)
        lat = request.form.get('lat')
        lng = request.form.get('lng')

        # Creating a game from submitted form informatio
        new_game = Game(user_id = current_user.id, name = name, game_type = sportSelect, total_number_people = totalNumPeople, initial_number_people = currNumPeople, latitude = lat, longitude = lng, event_datetime = eventDateTime)
        db.session.add(new_game)
        db.session.commit()
        flash('Game created', category='success')
    return render_template("home.html", user=current_user)

@views.route('/games', methods = ['GET', 'POST'])
def games():
    # Query database for the user's id
    user_games = Game.query.filter_by(user_id = current_user.id)

    # user_games = {key:value for key, value in user_games.__dict__.items() if not key.startswith('__') and not callable(key)}
    # Display the necessary data
    return render_template("games.html", user_games = user_games, user = current_user)

