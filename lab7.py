from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for, abort

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "Shrek",
        "title_ru": "Шрэк",
        "year": 2001,
        "description": "Жил да был в сказочном государстве большой зеленый\
            великан по имени Шрэк. Жил он в гордом одиночестве в лесу, на\
            болоте, которое считал своим. Но однажды злобный коротышка\
             — лорд Фаркуад, правитель волшебного королевства,безжалостно\
             согнал на Шрэково болото всех сказочных обитателей. И беспечной\
             жизни зеленого великана пришел конец. Но лорд Фаркуад пообещал\
             вернуть Шрэку болото, если великан добудет ему прекрасную\
             принцессу Фиону, которая томится в неприступной башне,\
             охраняемой огнедышащим драконом."
    },
    {
        "title": "How to Train Your Dragon",
        "title_ru": "Как приручить дракона",
        "year": 2010,
        "description": "Подростку Иккингу не слишком близки традиции\
            его героического племени, много лет ведущего войну\
             с драконами. Парень неожиданно заводит дружбу с драконом\
             Беззубиком, который поможет ему и другим викингам увидеть\
             мир с совершенно другой стороны."
    },
    {
        "title": "Brave",
        "title_ru": "Храбрая сердцем",
        "year": 2012,
        "description": "Испокон веков мифы и легенды окутывают загадочной\
             пеленой живописные отроги Шотландских гор. Искусной лучнице\
             Мериде приходится выбирать свой путь в жизни самостоятельно,\
             и однажды она отказывается следовать древним традициям\
             королевства, бросая вызов могущественным шотландским\
             кланам и их предводителям: нескладному лорду МакГаффину,\
             угрюмому лорду Макинтошу и сварливому лорду Дингволлу.\
             Неосторожные поступки Мериды грозят повергнуть королевство\
             в хаос, и тогда она отправляется за советом к эксцентричной\
             отшельнице, которая вместо помощи накладывает на Мериду\
             опасное заклятье. Юной принцессе предстоит полагаться\
             только на собственную храбрость, чтобы преодолеть\
             могущественное волшебство и победить самого страшного\
             зверя из тех, что водятся в горных долинах."
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
    films[id] = film
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    new_film = request.get_json() 
    films.append(new_film)  
    new_film_index = len(films) - 1  
    return jsonify({"index": new_film_index}), 201 