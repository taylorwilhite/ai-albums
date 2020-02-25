from flask import Flask, render_template, jsonify
import requests
import os
from generator import genBand, genAlbum

app = Flask(__name__)

unsplash_key = os.getenv('UNSPLASH_KEY')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/album')
def get_album():
    albumcover = requests.get(f'https://api.unsplash.com/photos/random?client_id={unsplash_key}&orientation=squarish')
    band_name = genBand()
    album_name = genAlbum()
    return jsonify(bandname=band_name,
                   image=albumcover.json(),
                   title=album_name)
