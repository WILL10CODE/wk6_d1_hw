from app import app
from flask import Blueprint, render_template, url_for, request
from flask.json import jsonify
from app.models import Pokemon
from app.models import db
import requests as r

@app.route('/')

@app.route('/base')
def index():
    return "Hello, Pokemon API!"

@app.route('/search/pokemon', methods = ['POST'])
def searchPokemon():
    if request.method == "POST":
        my_pokemon = request.form['poke']
        data = r.get(f'https://pokeapi.co/api/v2/pokemon/{my_pokemon}')
        if data.status_code == 200:
            my_data = data.json()
            pokemon = {
                'name': '',
                'image': '',
                'abilities': []
            }
            for ability in my_data['abilities']:
                pokemon['abilities'].append(ability['ability']['name'])
            pokemon['name'] = my_data['name']
            pokemon['image'] = my_data['sprites']['front_default']
            id = my_data['id']
            my_pokemon = Pokemon.query.filter_by(id=id)
            if not my_pokemon:
                my_pokemon = Pokemon(id, pokemon['name'], pokemon['image'], pokemon['ability'])
                db.session.add(my_pokemon)
                if len(pokemon['abilities']) == 2:
                    ability1 = pokemon['abilities'][0], id
                    ability2 = pokemon['abilities'][1], id
                    db.session.add(ability1)
                    db.session.add(ability2)
                elif len(pokemon['abilities']) == 1:
                    ability1 = pokemon['abilities'][1], id
                    db.session.add(ability1)
                db.session.commit()
            return render_template('pokemon.html', pokemon = pokemon)
        else:
            pokemon = ''
            return render_template('pokemon.html', pokemon = pokemon)
    return {'hi': 'there'}