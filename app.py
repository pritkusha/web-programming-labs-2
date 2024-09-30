from flask import Flask, redirect, url_for, render_template, abort
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>web-сервер на flask</h1>

        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2">Вторая лабораторная</a></li>
            </ul>
        </nav>

        <footer>
            &copy; София Прыткова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Лабораторная работа 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static',
          filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые 
            базовые возможности.
        </p>
        <p><a href="/menu">Меню</a>.</p>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/oak">Дуб</a></li>
            <li><a href="/lab1/python">Питон</a></li>
            <li><a href="/lab1/student">Студент</a></li>
            <li><a href="/lab1/autumn">Осень</a></li>
        </ul>

        <footer>
            &copy; София Прыткова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <title>Дуб</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', 
        filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', 
        filename='oak.jpg') + '''" class="oak-image">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Язык Python</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', 
        filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Python</h1>
        <p>Python — это высокоуровневый интерпретируемый язык программирования, 
        который поддерживает множество парадигм программирования, 
        включая объектно-ориентированное, структурное и функциональное. 
        Его простота и лаконичность делают его одним из самых популярных 
        языков для обучения программированию.</p>
        <p>Python часто используется в различных областях, 
        таких как веб-разработка, анализ данных, искусственный интеллект, 
        автоматизация и многое другое. Благодаря огромному количеству библиотек 
        и активному сообществу, разработчики могут легко находить решения для 
        различных задач.</p>
        <img src="''' + url_for('static', 
        filename='python_programming.jpg') + '''" alt="Программирование 
        на Python" class="python-image">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Студент</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', 
        filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Студент</h1>
        <p>Фамилия: Прыткова</p>
        <p>Имя: София</p>
        <p>Отчество: Александровна</p>
        <img src="''' + url_for('static', 
        filename='ngtu_logo.png') + '''" alt="Лого НГТУ" class="student-logo">
    </body>
</html>
'''

@app.route("/lab1/autumn")
def autumn():
    return '''
<!doctype html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', 
        filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Осень</h1>
        <p>Хочется красивую и теплую весну, а не вот это все...</p>
        <img src="''' + url_for('static', 
        filename='custom_image.jpg') + '''" alt="Осень" class="custom-image">
    </body>
</html>
'''

@app.route("/lab2/a")
def a():
    return 'ok'

@app.route("/lab2/a/")
def a2():
    return 'ok'

flower_list = ['роза','тюльпан','незабудка','ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        return 'такого цветка нет', 404
    else: 
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Цветок: {flower_list[flower_id]}</h1>
        <p>ID цветка: {flower_id}</p>
        <a href="/lab2/flowers/">Показать все цветы</a>
    </body>
</html>
'''

@app.route('/lab2/add_flower/', defaults={'name': None})
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    if name is None:
        abort(400, "Вы не задали имя цветка")
    
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветков: {len(flower_list)} </p>
    <p>Полный список: {flower_list} </p>
    </body>
</html>
'''

@app.route('/lab2/flowers/')
def list_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список всех цветов</h1>
        <p>{', '.join(flower_list)}, Всего: {len(flower_list)}</p>
        <a href="/lab2/clear_flowers/">Очистить список цветов</a>
    </body>
</html>
'''

@app.route('/lab2/clear_flowers/')
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

@app.route('/lab2/example')
def exampler():
    name,  lab_number, group, course_number = 'София Прыткова', 2, 'ФБИ-24', 3
    fruits = [ 
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('example.html',
                           name=name, lab_number=lab_number, group=group,
                           course_number=course_number, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('calc', a=1, b=1))

@app.route('/lab2/calc/<int:a>/')
def default_b_calc(a):
    return redirect(url_for('calc', a=a, b=1))


@app.route('/lab2/calc/<int:a>/<int:b>')
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

@app.route('/lab2/books')
def book_list():
    return render_template('books.html', books=books)

mushrooms = [
    {
        'name': 'Подосиновик',
        'description': 'Съедобный гриб, растущий в лиственных лесах.',
        'image': '/static/podosinovik.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Боровик',
        'description': 'Популярный съедобный гриб, также известный как белый гриб.',
        'image': '/static/borovik.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Масленок',
        'description': 'Съедобный гриб с характерной масляной шляпкой.',
        'image': '/static/maslenok.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Лисичка',
        'description': 'Съедобный гриб с ярко-желтой окраской.',
        'image': '/static/lisichka.jpg'  # Обязательно измените на ваше изображение
    },
    {
        'name': 'Шампиньон',
        'description': 'Одним из самых известных и употребляемых видов грибов.',
        'image': '/static/shampinjon.jpg'  # Обязательно измените на ваше изображение
    }
]

@app.route('/lab2/mushrooms')
def mushroom_list():
    return render_template('mushrooms.html', mushrooms=mushrooms)