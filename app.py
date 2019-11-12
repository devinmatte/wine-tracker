import os

from flask import Flask, render_template, request, redirect
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)


class Wines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    vintage = db.Column(db.Integer)
    color = db.Column(db.String)
    country = db.Column(db.String)

    def __init__(self, wine_id, name, vintage, color, country):
        self.id = wine_id
        self.name = name
        self.vintage = vintage
        self.color = color
        self.country = country


db.create_all()


@app.route('/')
def home():
    wines = Wines.query.all()

    return render_template('index.html', wines=wines)


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

    headers = {'Authorization': 'Token ' + os.environ.get('token')}
    response = requests.get('https://api.globalwinescore.com/globalwinescores/latest/', headers=headers, params=params)

    searched_wine = []
    wines = set(wine.id for wine in Wines.query.all())
    print(wines)

    for wine in response.json()['results']:
        searched_wine.append({
            'id': wine['wine_id'],
            'name': wine['wine'],
            'vintage': wine['vintage'],
            'color': wine['color'],
            'country': wine['country']
        })

    return render_template('search.html', searched_wine=searched_wine, wines=wines)


@app.route('/save', methods=['POST'])
def save():
    if request.get_json():
        data = request.get_json()
        new_wine = Wines(data[0], data[1], data[2], data[4], data[3])
        db.session.add(new_wine)
        db.session.commit()
        db.session.flush()

    return {'success': True}


@app.route('/notes', methods=['POST'])
def notes():
    if request.get_json():
        # TODO Get form data
        # TODO Get wine object
        # TODO Update Wine object with notes
        db.session.add(wine)
        db.session.commit()
        db.session.flush()

    return {'success': True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
