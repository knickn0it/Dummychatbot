from flask import Flask, request, jsonify, send_from_directory
import os
from model.chatbot_model import get_response

app = Flask(__name__, static_folder="../frontend")

# Route for the chatbot endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    chatbot_response = get_response(user_input)
    return jsonify({"response": chatbot_response})

# Route to serve index.html for the root path
@app.route("/", methods=["GET"])
def index():
    return send_from_directory(os.path.join(app.root_path, '../frontend'), 'index.html')

# Explicitly handle requests for static files like CSS and JS
@app.route("/<path:filename>", methods=["GET"])
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, '../frontend'), filename)

if __name__ == "__main__":
    app.run(debug=True)
