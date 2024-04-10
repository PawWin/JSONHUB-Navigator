from flask import Flask, render_template
import requests

app = Flask(__name__,  template_folder='./templates')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/posts')
def posts():
    r_p = requests.get('https://jsonplaceholder.typicode.com/posts')
    data_posts = r_p.json()
    return render_template('posts.html',data_posts = data_posts)

@app.route('/comments')
def comments():
    r_c = requests.get('https://jsonplaceholder.typicode.com/comments')
    data_comments = r_c.json()
    print(data_comments)
    return render_template('comments.html',data_comments = data_comments)
@app.route('/photos')
def photos():
    r_p = requests.get('https://jsonplaceholder.typicode.com/photos')
    data_photos = r_p.json()
    return render_template('photos.html',data_photos = data_photos)
@app.route('/albums')
def albums():
    r_a = requests.get('https://jsonplaceholder.typicode.com/albums')
    data_albums = r_a.json()
    return render_template('albums.html',data_albums = data_albums)


def get_comments(post_id):
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    return len(r.json())

if __name__ == '__main__':
    app.run()
