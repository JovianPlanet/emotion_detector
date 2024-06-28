""" Server code for emotion detection web app
"""

import requests
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)
    print(res['anger'])

    return f"For the given statement, the system response is \
    'anger': {res['anger']}, \
    'disgust': {res['disgust']}, \
    'fear': {res['fear']}, \
    'joy': {res['joy']}, \
    'sadness': {res['sadness']}. \
    The dominant emotion is {res['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """ Renders index page
    """
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="localhost", port=5000)