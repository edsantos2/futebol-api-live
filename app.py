from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_BASE_URL = "https://api.api-futebol.com.br/v1/"
API_KEY = "live_5c7f309f0cc34d8b64af5a6fa26e1d"

@app.route('/api/live-matches')
def live_matches():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{API_BASE_URL}ao-vivo", headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
