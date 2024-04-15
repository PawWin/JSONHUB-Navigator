from flask import Flask, render_template, redirect, url_for, request
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

data_posts_searched = []


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

@app.route('/posts',methods=['GET','POST'])
def posts():
    global data_posts_searched

    if not data_posts_searched:
        data_posts = get_data('posts')
    else:
        data_posts = deepcopy(data_posts_searched)

    data_posts_searched = []


    if forms.SearchNumberForm().search1.data and forms.SearchNumberForm().validate():
        top_field = forms.SearchNumberForm().top
        top = int(top_field.data)
        print(top)
        bottom_field = forms.SearchNumberForm().bottom
        bottom = int(bottom_field.data)
        print(bottom)
        data_posts_searched = numberSearch(bottom, top, data_posts)
        return redirect(url_for('posts'))

    if forms.SearchWordForm().search2.data and forms.SearchWordForm().validate():
        word_field = forms.SearchWordForm().word
        word = str(word_field.data)
        print(word)
        data_posts_searched = wordSearch(word, data_posts)
        return redirect(url_for('posts'))

    if forms.SelectForm().select_field.data and forms.SelectForm().validate():
        selected_value = request.form['select_field']
        data_posts_searched = get_specific_number_posts(data_posts, int(selected_value))
        return redirect(url_for('posts'))

    return render_template('posts.html', data_posts=data_posts, search_number_form=forms.SearchNumberForm(), search_word_form=forms.SearchWordForm(),select_form=forms.SelectForm())


@app.route('/comments')
def comments():
    data_comments = get_data('comments')
    return render_template('comments.html', data_comments=data_comments)


@app.route('/photos')
def photos():
    data_photos = get_data('photos')
    return render_template('photos.html', data_photos=data_photos)


@app.route('/albums',methods=['GET','POST'])
def albums():
    data_albums = get_data('albums')
    return render_template('albums.html', data_albums=data_albums)



def numberSearch(bottom, top, posts):
    foundposts = []
    for post in posts:
        postlen = len(post["body"])
        if bottom <= postlen <= top:
            foundposts.append(post)
    return foundposts



def wordSearch(word, posts):
    foundposts = []
    for post in posts:
        if word in (post["body"] or post["title"]):
            foundposts.append(post)
    return foundposts

def get_specific_number_posts(posts, num):
    num_posts = posts[:num]
    return num_posts

if __name__ == '__main__':
    app.run(debug=True)
