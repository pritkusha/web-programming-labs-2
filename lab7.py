from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for, abort
from datetime import datetime

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "Shrek",
        "title_ru": "Шрэк",
        "year": 2001,
        "description": "Жил да был в сказочном государстве большой зеленый великан по имени Шрэк..."
    },
    {
        "title": "How to Train Your Dragon",
        "title_ru": "Как приручить дракона",
        "year": 2010,
        "description": "Подростку Иккингу не слишком близки традиции его героического племени..."
    },
    {
        "title": "Brave",
        "title_ru": "Храбрая сердцем",
        "year": 2012,
        "description": "Испокон веков мифы и легенды окутывают загадочной пеленой живописные отроги Шотландских гор..."
    },
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404, description="Film not found")
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404, description="Film not found")
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404, description="Film not found")
    
    film = request.get_json()
    
    # Проверки для всех полей
    errors = {}
    
    # Проверка русского названия
    if not film.get('title_ru'):
        errors['title_ru'] = 'Русское название не должно быть пустым'
    
    # Проверка оригинального названия
    if not film.get('title') and not film.get('title_ru'):
        errors['title'] = 'Оригинальное название не должно быть пустым, если русское название пустое'
    
    # Проверка года
    year = film.get('year')
    if not year or not isinstance(year, int) or year < 1895 or year > datetime.now().year:
        errors['year'] = f'Год должен быть от 1895 до {datetime.now().year}'
    
    # Проверка описания
    description = film.get('description')
    if not description:
        errors['description'] = 'Описание не должно быть пустым'
    elif len(description) > 2000:
        errors['description'] = 'Описание не должно превышать 2000 символов'
    
    # Если есть ошибки, возвращаем их
    if errors:
        return jsonify(errors), 400
    
    # Если оригинальное название пустое, используем русское название
    if not film.get('title'):
        film['title'] = film.get('title_ru', '')
    
    films[id] = film
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    new_film = request.get_json()
    
    # Проверки для всех полей
    errors = {}
    
    # Проверка русского названия
    if not new_film.get('title_ru'):
        errors['title_ru'] = 'Русское название не должно быть пустым'
    
    # Проверка оригинального названия
    if not new_film.get('title') and not new_film.get('title_ru'):
        errors['title'] = 'Оригинальное название не должно быть пустым, если русское название пустое'
    
    # Проверка года
    year = new_film.get('year')
    if not year or not isinstance(year, int) or year < 1895 or year > datetime.now().year:
        errors['year'] = f'Год должен быть от 1895 до {datetime.now().year}'
    
    # Проверка описания
    description = new_film.get('description')
    if not description:
        errors['description'] = 'Описание не должно быть пустым'
    elif len(description) > 2000:
        errors['description'] = 'Описание не должно превышать 2000 символов'
    
    # Если есть ошибки, возвращаем их
    if errors:
        return jsonify(errors), 400
    
    # Если оригинальное название пустое, используем русское название
    if not new_film.get('title'):
        new_film['title'] = new_film.get('title_ru', '')
    
    films.append(new_film)
    new_film_index = len(films) - 1
    return jsonify({"index": new_film_index}), 201