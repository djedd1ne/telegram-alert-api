from flask import Flask, request, jsonify
from app.services import send_to_telegram
from app.config import Config
from app.utils import is_valid_input

app = Flask(__name__)

notifications = []

@app.route('/notify', methods=['POST'])
def create_notifications():
    data = request.json
    if not data or not is_valid_input(data):
        return jsonify({"error": "Bad Request"}), 400
    
    #if valid, store data in notifications
    notifications.append(data)

    #if Type is "Warning" send forward the message
    if data['Type'] == "Warning":
        message = f"WARNING: {data['Name']} - {data['Description']}"
        send_to_telegram(message)

    return jsonify({data['Description']: "OK"}), 200


@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications), 200