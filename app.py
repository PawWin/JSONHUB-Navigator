from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
import requests
import logging
import os

app = Flask(__name__, template_folder='./templates')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

logging.basicConfig(filename='errors.log', level=logging.ERROR)


def get_data(endpoint):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/{endpoint}')
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f'Error while fetching data from API: {e}')
        return None
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    data_posts = get_data('posts')
    return render_template('posts.html', data_posts=data_posts)


@app.route('/comments')
def comments():
    data_comments = get_data('comments')
    return render_template('comments.html', data_comments=data_comments)


@app.route('/photos')
def photos():
    data_photos = get_data('photos')
    return render_template('photos.html', data_photos=data_photos)


@app.route('/albums')
def albums():
    data_albums = get_data('albums')
    return render_template('albums.html', data_albums=data_albums)


def get_comments(post_id):
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    return len(r.json())


def search(bottom, top, posts):
    foundposts = []
    for post in posts:
        if bottom < len(post) < top:
            foundposts.append(post)
    return foundposts


if __name__ == '__main__':
    app.run()
