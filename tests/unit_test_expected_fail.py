import pytest
import pytest
from app import app, numberSearch, wordSearch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data  # Assuming this text is unique to your index page

def test_posts_route(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert b'Witam na tym charytatywnym eventcie' in response.data

def test_comments_route(client):
    response = client.get('/comments')
    assert response.status_code == 200
    assert b'slay girl slay' in response.data

def test_photos_route(client):
    response = client.get('/photos')
    assert response.status_code == 200
    assert b'kowalski.hanek@podlasie.com' in response.data

def test_albums_route(client):
    response = client.get('/albums')
    assert response.status_code == 200
    assert b'albooooooooooms' in response.data
def test_number_search():
    posts = [
        {"body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
        {"body": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
        {"body": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."}
    ]
    top = 30
    bottom = 29
    result = numberSearch(bottom, top, posts)
    assert len(result) == 2  # Expected number of posts within the range

def test_word_search():
    posts = [
        {"title": "Post 1", "body": "This is the first post."},
        {"title": "Post 2", "body": "This post talks about Python programming."},
        {"title": "Post 3", "body": "Flask is a micro web framework for Python."}
    ]
    word = "Django"
    result = wordSearch(word, posts)
    assert len(result) == 2  # Expect only one post containing the word "Python"



if __name__ == '__main__':
    pytest.main()
