from flask import Flask, render_template, request, jsonify
from services.gemini_service import GeminiService
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
gemini_service = GeminiService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    mood = request.json.get('mood')
    suggestions = gemini_service.get_suggestions(mood)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)