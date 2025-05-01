from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/api/steam/')
def steam_avatar():

    url = request.args.get('steam-url')

    if not url or not url.startswith('http'):
        return jsonify({"image": None, "error": "invalid-url"})
    try:
        result = requests.get(url, timeout=5)
    except requests.RequestException:
        return jsonify({"image": None, "error": "fetch-failed"})
    soup = BeautifulSoup(result.text, 'html.parser')
    avatar = soup.find('div', class_='playerAvatarAutoSizeInner')
    images = avatar.find_all('img') if avatar else []
    try:
        image = images[1]['src']
    except IndexError:
        return jsonify({"image": None, "error": "not-found"})
    return jsonify({"image": image, "error": "none"})
