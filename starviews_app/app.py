
from flask import Flask, render_template, abort
import json, os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'movies.json')

def load_movies():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    movies = load_movies()
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movies = load_movies()
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if not movie:
        abort(404)
    return render_template('movie.html', movie=movie)

if __name__ == '__main__':
    # For development only. Use a proper WSGI server for production.
    app.run(debug=True, host='0.0.0.0', port=5000)
