from flask import Flask, jsonify, request

#initialize the app
app = Flask(__name__)

#define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. capture first name and last name
    2. if either is not provided: respond with an error
    3. if first name is not provided and second name is provided:
    respond with "Hello Mt. <second-name>!"
    4.If first name is provided but second name is not provided:
    respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question,
    "Is your name <fist-name> <second-name>
    """
    response = {"data": "Hello, world"}
    return jsonify(response)