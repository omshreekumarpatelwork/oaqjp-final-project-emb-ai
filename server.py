from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotionDetector():
    """Analyze the text submitted by the user."""
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)