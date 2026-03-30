from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        
        # Process form data
        name = data.get('name', '')
        email = data.get('email', '')
        course = data.get('course', '')
        grade = data.get('grade', 0)
        comments = data.get('comments', '')
        
        # Simple validation
        if not all([name, email, course]):
            return jsonify({
                'error': 'Name, email, and course are required'
            }), 400
        
        if not (0 <= float(grade) <= 100):
            return jsonify({
                'error': 'Grade must be between 0 and 100'
            }), 400
        
        # Simulate processing
        timestamp = datetime.datetime.now().isoformat()
        processed_data = {
            'name': name,
            'email': email,
            'course': course,
            'grade': grade,
            'comments': comments,
            'status': 'processed',
            'timestamp': timestamp
        }
        
        print(f"Received submission: {processed_data}")
        
        return jsonify({
            'message': 'Form submitted successfully!',
            'data': processed_data
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)