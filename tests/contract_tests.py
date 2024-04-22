import requests
import pytest
import json

APP_URL = 'http://localhost:5000'

POSTS_ENDPOINT = f'{APP_URL}/posts'
COMMENTS_ENDPOINT = f'{APP_URL}/comments'
PHOTOS_ENDPOINT = f'{APP_URL}/photos'
ALBUMS_ENDPOINT = f'{APP_URL}/albums'

EXTERNAL_API_URL = 'https://jsonplaceholder.typicode.com'

def test_posts_endpoint():
    response_posts = requests.get(POSTS_ENDPOINT)
    response_external = requests.get(f'{EXTERNAL_API_URL}/posts')
    assert response_posts.status_code == 200
    assert response_external.status_code == 200
    assert b'sunt aut facere repellat provident occaecati excepturi optio reprehenderit' in response_posts.content
    external_data = response_external.json()
    html_content = response_posts.content.decode('utf-8')

    for item in external_data:
        for key, value in item.items():
            if json.dumps(value) in html_content:
                assert True
                return

    assert False, "No part of the JSON data from the external API is present in the HTML content"


def test_comments_endpoint():
    response_posts = requests.get(COMMENTS_ENDPOINT)
    assert response_posts.status_code == 200

    response_external = requests.get(f'{EXTERNAL_API_URL}/comments')
    assert response_external.status_code == 200

    external_data = response_external.json()
    html_content = response_posts.content.decode('utf-8')

    for item in external_data:
        for key, value in item.items():
            if json.dumps(value) in html_content:
                assert True
                return

    assert False, "No part of the JSON data from the external API is present in the HTML content"


def test_photos_endpoint():
    response_posts = requests.get(PHOTOS_ENDPOINT)
    assert response_posts.status_code == 200

    response_external = requests.get(f'{EXTERNAL_API_URL}/photos')
    assert response_external.status_code == 200

    external_data = response_external.json()
    html_content = response_posts.content.decode('utf-8')

    for item in external_data:
        for key, value in item.items():
            if json.dumps(value) in html_content:
                assert True
                return

    assert False, "No part of the JSON data from the external API is present in the HTML content"


def test_albums_endpoint():
    response_posts = requests.get(ALBUMS_ENDPOINT)
    assert response_posts.status_code == 200

    response_external = requests.get(f'{EXTERNAL_API_URL}/albums')
    assert response_external.status_code == 200

    external_data = response_external.json()
    html_content = response_posts.content.decode('utf-8')

    for item in external_data:
        for key, value in item.items():
            if json.dumps(value) in html_content:
                assert True
                return

    assert False, "No part of the JSON data from the external API is present in the HTML content"

if __name__ == '__main__':
    pytest.main()
