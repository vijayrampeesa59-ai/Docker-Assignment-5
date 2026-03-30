from flask import Flask, jsonify, request
from flask_cors import CORS  # Add CORS support
import pymongo
import json
import os

app = Flask(__name__)
CORS(app) 
# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://dummy:1234@tram.uzwi1fl.mongodb.net/?appName=tram"
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client['DockerData']
users_collection = db['users']

@app.route('/api', methods=['GET'])
def get_api_data():
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'backend_data.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.json
        result = users_collection.insert_one(data)
        return jsonify({"success": True, "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')