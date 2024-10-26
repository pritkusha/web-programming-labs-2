from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1' ,__name__)


@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/lab1")
def lab():
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


@lab1.route("/lab1/oak")
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
        <img src="''' + url_for('static', filename='lab1/oak.jpg') + '''" class="oak-image">

    </body>
</html>
'''


@lab1.route("/lab1/python")
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
        filename='lab1/python_programming.jpg') + '''" alt="Программирование 
        на Python" class="python-image">
    </body>
</html>
'''


@lab1.route("/lab1/student")
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
        filename='lab1/ngtu_logo.png') + '''" alt="Лого НГТУ" class="student-logo">
    </body>
</html>
'''


@lab1.route("/lab1/autumn")
def autumn():
    return '''
<!doctype html>
<html>
    <head>
        <title>Осень</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', 
        filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Осень</h1>
        <p>Хочется красивую и теплую весну, а не вот это все...</p>
        <img src="''' + url_for('static', 
        filename='lab1/custom_image.jpg') + '''" alt="Осень" class="custom-image">
    </body>
</html>
'''