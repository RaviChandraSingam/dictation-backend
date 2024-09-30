from flask import Flask, request, jsonify
import pyttsx3
from flask_cors import CORS


app = Flask(__name__)
CORS(app, automatic_options=True)

def pronounce(word):
    engine = pyttsx3.init()    
    rate = engine.getProperty('rate')  # Get the current speech rate
    engine.setProperty('rate', rate - 50)  # Decrease the speech rate by 50 (you can adjust this value)
    engine.say(word)
    engine.runAndWait()

@app.route('/api/pronounce', methods=['POST'])
def pronounce_word():
    data = request.json
    word = data.get('word', '')
    if word:
        pronounce(word)
        return jsonify({'message': 'Pronounced successfully'}), 200
    return jsonify({'error': 'No word provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)

def main(request):
    with app.app_context():
        return app.full_dispatch_request()
