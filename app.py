from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf.csrf import CSRFProtect
import requests
import logging
import forms
import os
from copy import deepcopy

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

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if 'data_posts_searched' not in session:
        session['data_posts_searched'] = []

    data_posts_searched = session['data_posts_searched']

    if not data_posts_searched:
        data_posts = get_data('posts')
    else:
        data_posts = deepcopy(data_posts_searched)

    session['data_posts_searched'] = []

    search_number_form = forms.SearchNumberForm()
    search_word_form = forms.SearchWordForm()
    select_form = forms.SelectForm()

    if search_number_form.search1.data and search_number_form.validate_on_submit():
        top = int(search_number_form.top.data)
        bottom = int(search_number_form.bottom.data)
        session['data_posts_searched'] = numberSearch(bottom, top, data_posts)
        return redirect(url_for('posts'))

    if search_word_form.search2.data and search_word_form.validate_on_submit():
        word = str(search_word_form.word.data)
        session['data_posts_searched'] = wordSearch(word, data_posts)
        return redirect(url_for('posts'))

    if select_form.select_field.data and select_form.validate_on_submit():
        selected_value = int(select_form.select_field.data)
        session['data_posts_searched'] = get_specific_number_posts(data_posts, selected_value)
        return redirect(url_for('posts'))

    return render_template('posts.html', data_posts=data_posts, search_number_form=search_number_form, search_word_form=search_word_form, select_form=select_form)

@app.route('/comments')
def comments():
    data_comments = get_data('comments')
    return render_template('comments.html', data_comments=data_comments)

@app.route('/photos')
def photos():
    data_photos = get_data('photos')
    return render_template('photos.html', data_photos=data_photos)

@app.route('/albums', methods=['GET', 'POST'])
def albums():
    data_albums = get_data('albums')
    return render_template('albums.html', data_albums=data_albums)

def numberSearch(bottom, top, posts):
    found_posts = []
    for post in posts:
        post_len = len(post["body"])
        if bottom <= post_len <= top:
            found_posts.append(post)
    return found_posts

def wordSearch(word, posts):
    found_posts = []
    for post in posts:
        if word in (post["body"] or post["title"]):
            found_posts.append(post)
    return found_posts

def get_specific_number_posts(posts, num):
    num_posts = posts[:num]
    return num_posts

if __name__ == '__main__':
    app.run(debug=True)