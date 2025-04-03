from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import yt_dlp
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auralyx.db'
db = SQLAlchemy(app)

# Model Definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Function to Search YouTube Videos
def search_youtube(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'noplaylist': True,
        'quiet': True,
        'default_search': 'ytsearch10',  # Search for the top 10 results
        'cookiefile': 'cookies.txt',  # Use cookie file
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f'ytsearch10:{query}', download=False)
            return [{
                'title': video.get('title', ''),
                'url': video.get('webpage_url', ''),
                'thumbnail': video.get('thumbnail', ''),
                'channelName': video.get('uploader', 'Unknown Channel')  # Extract channel name
            } for video in info['entries']]
        except Exception as e:
            print(f"Error in searching: {e}")
            return []

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_youtube(query)
    return jsonify(results)

@app.route('/get_audio_info', methods=['POST'])
def get_audio_info():
    url = request.form['url']
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'noplaylist': True,
        'cookiefile': 'cookies.txt',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return jsonify({
            'url': info_dict.get('url', ''),
            'title': info_dict.get('title', '')
        })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)