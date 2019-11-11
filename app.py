from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # TODO: Get Saved Wines

    return render_template('index.html')


@app.route('/search')
def search():
    params = {'limit': 1000}
    if request.args:
        if request.args.get('search-vintage'):
            params['vintage'] = request.args.get('search-vintage')
        if request.args.get('search-country'):
            params['country'] = request.args.get('search-country').capitalize()
        if request.args.get('search-color'):
            params['color'] = request.args.get('search-color').lower()

    headers = {'Authorization': 'Token 8ba0959720d6a66ac34878b29d9b124f4640b919'}
    response = requests.get('https://api.globalwinescore.com/globalwinescores/latest/', headers=headers, params=params)

    searched_wine = []

    for wine in response.json()['results']:
        print(wine)
        searched_wine.append({
            'id': wine['wine_id'],
            'name': wine['wine'],
            'vintage': wine['vintage'],
            'color': wine['color'],
            'country': wine['country']
        })

    print(searched_wine)

    return render_template('search.html', searched_wine=searched_wine)


@app.route('/save', methods=['POST'])
def save():
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
