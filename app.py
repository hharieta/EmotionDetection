'''
This is the main file that runs the Flask server. 
It is responsible for handling the requests and responses from the client.
The server is responsible for rendering the index.html page 
and also for handling the requests from the client.
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

# @app.route("/emotionDetector")
# def sent_analyzer():
#     '''
#     This function is responsible for handling the requests from the client.
#     It takes the text to analyze from the client and returns the response from the server.
#     '''
#     text_to_analyze = request.args.get("textToAnalyze")
#     response = emotion_detector(text=text_to_analyze)

#     if response['dominant_emotion'] is None:
#         return "<h5> Invalid text! Please try again!</h5>"

#     return f"{' '.join([f'{key}: {value} ' for key, value in response.items()])}"

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    This function is responsible for handling the requests from the client.
    It takes the text to analyze from the client and returns the response from the server.
    '''

    
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text=text_to_analyze)
    print(response)

    if response is None:
        return "Invalid text! Please try again!"
    
    return jsonify(response)
 

@app.route("/")
def render_index_page():
    '''
    This function is responsible for rendering the index.html page.
    serves as the home page for the application.
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
