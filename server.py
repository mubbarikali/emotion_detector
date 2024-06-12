"""
Flask application for emotion detection.

This application provides a web interface for users to submit text and
receive emotion analysis results. It utilizes the `EmotionDetection`
module for emotion detection and uses Flask for routing and templating.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


def emotion_detector_route():
    """
    Route to handle emotion detection requests.

    Retrieves the text to analyze from the query parameters,
    calls the emotion_detector function, and returns a formatted response.

    Returns:
        str: A formatted string with the emotions and the dominant emotion,
             or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)
    formatted_response = f"""
    For the given statement, the system response is 
    'anger': {response['anger']}, 'disgust': {response['disgust']},
    'fear': {response['fear']}, 'joy': {response['joy']} and 
    'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}.
    """
    return formatted_response


@app.route("/")
def render_index_page():
    """
    Route to render the index page.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
