from flask import Flask, redirect, url_for, render_template
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
    if flower_id >= len(flower_list):
        return 'такого цветка нет', 404
    else: 
        return 'цветок: ' + flower_list[flower_id]
    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
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
@app.route('/lab2/example')
def exampler():
    name = 'София Прыткова'
    lab_number = '2'
    group = 'ФБИ-24'
    course_number = '3'
    return render_template('example.html', name=name, 
    lab_number=lab_number, group=group, course_number=course_number)