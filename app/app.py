from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({
        'application': 'devops-cicd-lab',
        'message': 'CI/CD deployment successful',
        'version': os.getenv('APP_VERSION', 'local')
    })

@app.get('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
