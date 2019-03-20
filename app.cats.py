import requests

from flask import Flask, render_template, request

app = Flask(__name__)
key = 'd6d3df10-5689-454d-9c97-a356f5bf3a6d'

@app.route('/')
def index():
    response = requests.get(
        'https://api.thecatapi.com/v1/images/search',
        headers={'x-api-key': key}
    )
    data = response.json()[0]
    print(data)
    url = data['url']
    image_id = data['id']
    return render_template('index_cats.html', picture=url, image_id=image_id)

@app.route('/save')
def add_favourite():
    image_id = request.args.get('image_id')

    response = requests.post(
        'https://api.thecatapi.com/v1/favourites',
        headers={'x-api-key': key},
        json={
            'image_id': image_id,
            'sub_id': 'x1be4a'
        }
    )
    data = response.json()
    print(data)
    return '{}! Go back!'.format(data['message'])

@app.route('/fav')
def see_favourites():
    response = requests.get(
        'https://api.thecatapi.com/v1/favourites?limit=3',
        headers={'x-api-key': key}
    )
    data = response.json()
    print(data)
    return render_template('favourites.html', data=data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)