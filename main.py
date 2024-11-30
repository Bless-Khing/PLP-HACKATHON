# Import necessary libraries
from flask import Flask, jsonify, request
import random

# Initialize the Flask application
app = Flask(__name__)

# Sample responses for the chatbot
responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! What’s on your mind?",
        "Welcome! How can I help you?"
    ],
    "help": [
        "It's okay to feel overwhelmed. I'm here to help you.",
        "Remember, you're not alone. Let's talk about what's bothering you."
    ],
    "goodbye": [
        "Take care! Remember to reach out if you need support.",
        "Goodbye! Stay safe and take care of yourself."
    ],
    "default": [
        "I'm sorry, I didn't quite understand that. Can you tell me more?",
        "Could you please elaborate on that?"
    ]
}

# Home route
@app.route('/')
def home():
    return "Welcome to the Mental Health Support Chatbot!"

# Resources route
@app.route('/resources')
def resources():
    return jsonify({
        "resources": [
            {"name": "Mental Health Hotline", "contact": "123-456-7890"},
            {"name": "Crisis Text Line", "contact": "Text 'HELLO' to 741741"},
            {"name": "Local Counseling Services", "link": "www.example.com"}
        ]
    })

# Chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
