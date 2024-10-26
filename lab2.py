from flask import Blueprint, redirect, url_for, render_template, abort, request
lab2 = Blueprint('lab2' ,__name__)

@lab2.route("/lab2/a")
def a():
    return 'ok'

@lab2.route("/lab2/a/")
def a2():
    return 'ok'

flower_list = [
    {"name": "Роза", "price": 100},
    {"name": "Тюльпан", "price": 50},
    {"name": "Лилия", "price": 70},
]

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        return 'Такого цветка нет', 404
    
    flower = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Цветок: {flower['name']}</h1>
        <p>Цена: {flower['price']} руб.</p>
        <p>ID цветка: {flower_id}</p>
        <a href="/lab2/flowers/">Показать все цветы</a>
        <form action="/lab2/flowers/delete/{flower_id}/" method="POST" 
        style="display:inline;">
            <button type="submit">Удалить цветок</button>
        </form>
    </body>
</html>
'''

@lab2.route('/lab2/add_flower/', methods=['POST'])
def add_flower():
    flower_name = request.form.get('name')
    flower_price = request.form.get('price')
    
    if not flower_name or not flower_price:
        return 'Вы не задали имя и цену цветка', 400
    
    flower_list.lab2end({"name": flower_name, "price": float(flower_price)})
    return redirect(url_for('list_flowers'))


@lab2.route('/lab2/flowers/')
def list_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список всех цветов</h1>
        <ul>
        {"".join(f"<li>{flower['name']} - {flower['price']} руб. <a href='/lab2/flowers/{i}'>Посмотреть</a></li>" for i, flower in enumerate(flower_list))}
        </ul>
        <h2>Добавить новый цветок</h2>
        <form action="/lab2/add_flower/" method="POST">
            <input type="text" name="name" placeholder="Имя цветка" required>
            <input type="number" name="price" placeholder="Цена" required>
            <button type="submit">Добавить</button>
        </form>
        <a href="/lab2/clear_flowers/">Очистить список цветов</a>
    </body>
</html>
'''

@lab2.route('/lab2/flowers/delete/<int:flower_id>/', methods=['POST'])
def delete_flower(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        return 'Такого цветка нет', 404
    flower_list.pop(flower_id)
    return redirect(url_for('list_flowers'))

@lab2.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear()
    return '''
<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен.</h1>
        <a href="/lab2/flowers/">Показать все цветы</a>
    </body>
</html>
'''

@lab2.route('/lab2/example')
def exampler():
    name,  lab_number, group, course_number = 'София Прыткова', 2, 'ФБИ-24', 3
    fruits = [ 
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('lab2/example.html',
                           name=name, lab_number=lab_number, group=group,
                           course_number=course_number, fruits=fruits)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)

@lab2.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('calc', a=1, b=1))

@lab2.route('/lab2/calc/<int:a>/')
def default_b_calc(a):
    return redirect(url_for('calc', a=a, b=1))


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    operations = {
        'Сложение': f"{a} + {b} = {a + b}",
        'Вычитание': f"{a} - {b} = {a - b}",
        'Умножение': f"{a} * {b} = {a * b}",
        'Деление': f"{a} / {b} = {a / b if b != 0 else 'Ошибка: Деление на ноль'}",
        'Возведение в степень': f"{a}<sup>{b}</sup> = {a ** b}"
    }
    
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Результаты вычислений</h1>
        <p>A = {a}, B = {b}</p>
        <ul>
            {"".join(f"<li>{op}: {result}</li>" for op, 
            result in operations.items())}
        </ul>
        <a href="/lab2/calc/">Сбросить</a>
    </body>
</html>
'''

# Список книг
books = [
    {'title': 'Война и мир', 'author': 'Лев Толстой', 'genre': 'Эпопея', 'pages': 1225},
    {'title': 'Анна Каренина', 'author': 'Лев Толстой', 'genre': 'Роман', 'pages': 864},
    {'title': 'Преступление и наказание', 'author': 'Фёдор Достоевский', 'genre': 'Роман', 'pages': 430},
    {'title': 'Герой нашего времени', 'author': 'Михаил Лермонтов', 'genre': 'Роман', 'pages': 224},
    {'title': 'Убить пересмешника', 'author': 'Харпер Ли', 'genre': 'Драма', 'pages': 281},
    {'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'genre': 'Фантастика', 'pages': 448},
    {'title': '451 градус по Фаренгейту', 'author': 'Рэй Брэдбери', 'genre': 'Антиутопия', 'pages': 158},
    {'title': 'Собачье сердце', 'author': 'Михаил Булгаков', 'genre': 'Сатира', 'pages': 192},
    {'title': 'Гарри Поттер и философский камень', 'author': 'Дж. К. Роулинг', 'genre': 'Фэнтези', 'pages': 223},
    {'title': 'На дне', 'author': 'Максим Горький', 'genre': 'Драма', 'pages': 144},
]

@lab2.route('/lab2/books')
def book_list():
    return render_template('lab2/books.html', books=books)

mushrooms = [
    {
        'name': 'Подосиновик',
        'description': 'Съедобный гриб, растущий в лиственных лесах.',
        'image': '/static/lab2/podosinovik.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Боровик',
        'description': 'Популярный съедобный гриб, также известный как белый гриб.',
        'image': '/static/lab2/borovik.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Масленок',
        'description': 'Съедобный гриб с характерной масляной шляпкой.',
        'image': '/static/lab2/maslenok.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Лисичка',
        'description': 'Съедобный гриб с ярко-желтой окраской.',
        'image': '/static/lab2/lisichka.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Шампиньон',
        'description': 'Одним из самых известных и употребляемых видов грибов.',
        'image': '/static/lab2/shampinjon.jpg'  # Обязательно измените на ваше изображение
    }
]

@lab2.route('/lab2/mushrooms')
def mushroom_list():
    return render_template('lab2/mushrooms.html', mushrooms=mushrooms)