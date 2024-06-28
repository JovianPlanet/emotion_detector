""" Server code for emotion detection web app
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    """ Performs emotion analysis on a given text
    """
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)
    print(res['anger'])

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again"
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
    app.run(host="localhost", port=5000)
