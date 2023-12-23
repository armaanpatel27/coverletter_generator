from flask import Flask, render_template, request, jsonify
from backend_gpt import gpt
import openai
import os

#initializes the app
app = Flask(__name__)
app.static_folder = 'static'
#main route --> first page that app navigates to
@app.route('/')
def hello():
    #call index page
    return render_template('index.html')


#handles processing of incoming user data and returns processed return
#used to connect HTML to functions in python using Flask
@app.route('/update', methods=['POST'])
def update_content():
    user_input = request.form['userInput']
    gptResult = gpt(user_input)
    # Process user input here
    # For this example, we'll simply return the input.
    return jsonify(result=gptResult)