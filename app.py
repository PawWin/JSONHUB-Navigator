from flask import Flask, render_template
import requests

app = Flask(__name__,  template_folder='./templates')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/posts')
def posts():
    r_p = requests.get('https://jsonplaceholder.typicode.com/posts')
    r_k = requests.get('https://jsonplaceholder.typicode.com/comments')
    data_posts = r_p.json()
    data_kom = r_k.json()
    return render_template('posts.html',data_posts = data_posts,data_kom = data_kom, get_comments=get_comments)

def get_comments(post_id):
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    return len(r.json())
if __name__ == '__main__':
    app.run()
