from urllib import response
import datetime
from flask import Flask, jsonify, request, render_template

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

@app.get("/greet")
def index():

    """
    TODO :
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided:
    respond with "Hello Mr. <second-name>!"
    4. If first name is provided but second name is not provided:
    respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question,
    "Is your name <fist-name> <second-name>
    """

    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if not fname and not lname:
        return jsonify({"status": "error"})
    elif fname and not lname:
        response = {"data": f"Hello, {fname}!"}
    elif not fname and lname:
        response = {"data": f"Hello, {lname}!"}
    else:
        response = {"data": f"Is your name {fname} {lname}?"}

    return render_template('greet.html', response = response)
