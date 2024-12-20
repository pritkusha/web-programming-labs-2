from flask import Flask, redirect, url_for, render_template, abort, request
from lab1 import lab1 
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab4 import lab5

app = Flask(__name__)

app.secret_key = 'секретно-секретный секрет'

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

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
                <li><a href="/lab3">Третья лабораторная</a></li>
                <li><a href="/lab4">Четвертая лабораторная</a></li>
                <li><a href="/lab5">Пятая лабораторная</a></li>
                <li><a href="/lab6">Шестая лабораторная</a></li>
            </ul>
        </nav>

        <footer>
            &copy; София Прыткова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


# Обработчик ошибки 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404  # Укажите ваш шаблон для страницы 404

# Обработчик ошибки 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500  # Укажите ваш шаблон для страницы 500
