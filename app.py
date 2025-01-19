import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static/react', static_url_path='/')
CORS(app)

# API Route Example
@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

# React App Route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    # Serve React static files in production
    if os.getenv('FLASK_ENV') == 'production':
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')
    else:
        # Development environment: Forward to React dev server
        return jsonify({"message": "Use the React dev server for development!"})

if __name__ == '__main__':
    app.run(debug=True)
