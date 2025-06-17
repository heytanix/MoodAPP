# src/services/gemini_service.py

import google.generativeai as genai
import os
import json

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def get_suggestions(self, mood):
        prompt = f"""Given the mood '{mood}', provide suggestions in the following JSON format exactly:
        {{
            "songs": [
                "Song 1 - Artist",
                "Song 2 - Artist",
                "Song 3 - Artist"
            ],
            "quote": "An inspirational quote",
            "joke": "A mood-appropriate joke"
        }}"""

        try:
            response = self.model.generate_content(prompt)
            # Extract the JSON string from the response
            response_text = response.text
            # Remove any markdown formatting if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0]
            elif "```" in response_text:
                response_text = response_text.split("```")[1]
            
            # Parse the JSON string
            return json.loads(response_text.strip())
        except Exception as e:
            return {
                "error": str(e),
                "songs": ["No songs found"],
                "quote": "Could not generate quote",
                "joke": "Could not generate joke"
            }