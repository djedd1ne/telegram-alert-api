from flask import Flask, request, jsonify


app = Flask(__name__)

notifications = []

@app.route('/notify', methods=['POST'])
def create_notifications():
    data = request.json
    if not data or "Type" not in data or "Name" not in data or "Description" not in data:
        return jsonify({"error": "Bad Request"}), 400
    
    #if valid, store data in notifications
    notifications.append(data)

    return jsonify({data['Description']: "OK"}), 200
