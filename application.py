import flask
from flask import request, jsonify, render_template
import random

application = flask.Flask(__name__)
application.config["DEBUG"] = True

# List of excuses
excuses = [
    {'id': 0,
     'title':'It works on my machine',
     'type':'Client'},
    {'id': 1,
     'title':'It seemed to be working yesterday.',
     'type':'Client'},
    {'id': 2,
     'title':'Have you tried turning it off and on again?',
     'type':'Client'},
    {'id': 3,
     'title':'Are you sure its not a hardware issue?',
     'type':'Client'},
    {'id': 4,
     'title':'Are you using the correct version?',
     'type':'Client'},
    {'id': 5,
     'title':"It's never done that before",
     'type':'Client'},
    {'id': 6,
     'title':"I can't seem to test anything",
     'type':'Client'},
    {'id': 7,
     'title':'Somebody must have changed the code',
     'type':'Client'},
    {'id': 8,
     'title':"That's weird...",
     'type':'Client'},
    {'id': 9,
     'title':"It's working on my computer",
     'type':'Client'},
    {'id': 10,
     'title':'It seemed to be working yesterday',
     'type':'Client'},
    {'id': 11,
     'title':"There are delays on the Jubilee Line. Going to be abit late",
     'type':'Job'},
    {'id': 12,
     'title':'Not going to be able to go to work today, am playing golf with a client.',
     'type':'Job'},
    {'id': 13,
     'title':"Oh didn't I mention, I'm, working from home today.",
     'type':'Job'},
    {'id': 14,
     'title':"Running abit late, washing machine is currently flooding my house.",
     'type':'Job'},
    {'id': 15,
     'title':"I don't think I'll be able to make it today, I've had an allergic reaction to my neighbour's new cat.",
     'type':'Job'},
    {'id': 16,
     'title':'My dog was sick last night, waiting at the vet now. Will not be able to make it in today.',
     'type':'Job'},
    {'id': 17,
     'title':"Not going to be able to come into work today, I've got food poisioning.",
     'type':'Job'},
    {'id': 18,
     'title':"Don't think I'll be able to come into work today, I've come down with the flu.",
     'type':'Job'}
]

@application.route('/', methods=['GET'])
def home():
    return render_template('index.html', rand_excuse =random.choice(excuses)['title'])


@application.route('/api/v1/resources/excuses/all', methods=['GET'])
def api_all():
    return jsonify(excuses)

@application.route('/api/v1/resources/excuses/random', methods=['GET'])
def api_random():
    return jsonify(random.choice(excuses))



@application.route('/api/v1/resources/excuses', methods=['GET'])
def api():
    if 'id' in request.args:
        string = int(request.args['id'])
    elif 'type' in request.args:
    	string = str(request.args['type'])
    else:
    	raise TypeError("Error: Invalid Parameters pvoid")


    # Create an empty list for our results
    results = []


    # Loop through the data and match results that fit the requested ID.
    for excuse in excuses:
        if excuse['id'] == string:
            results.append(excuse)
        elif excuse['type'] == string:
        	results.append(excuse)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

application.run(port=5050)
