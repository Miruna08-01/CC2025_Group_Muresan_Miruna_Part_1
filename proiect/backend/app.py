from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow all origins for demo

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [
        {"id" : 1, "service": "Azure App Service", "category": "PaaS"},
        {"id" : 2, "service": "GitHub Actions", "category": "CI/CD"},
        {"id": 3, "service": "Flask API", "category": "Backend"},
        {"id": 4, "service": "HTML+JS", "category": "Frontend"}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
