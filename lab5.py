from flask import Blueprint, render_template, request, session
import psycopg2
from psycopg2.extras import RealDictCursor
lab5 = Blueprint('lab5' ,__name__)

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))

def db_connect():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database = 'sofiya_prytkova_knowledge_base',
        user = 'sofiya_prytkova_knowledge_base',
        password = '123'
    )
    cur = conn.cursor( cursor_factory= RealDictCursor)

    return conn, cur

def db_close(conn,cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/login',  methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error="Заполните поля")
    
    cur, conn = db_connect()

    cur.execute(f"SELECT * FROM users WHERE login='{login}';")
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', 
                               error="Логин и/или пароль неверны")
    
    if user['password'] != password:
        db_close(conn, cur)
        return render_template('lab5/login.html', 
                               error="Логин и/или пароль неверны")
    
    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    cur, conn = db_connect()

    cur.execute(f"SELECT login FROM users WHERE login='{login}';")
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html',
                               error="Такой пользователь уже существует")
    
    cur.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password}')")
    db_close(conn, cur)
    return render_template('lab5/succes.html', login=login)

@lab5.route('/lab5/list')
def list_articles():
    return render_template('lab5/list.html')

@lab5.route('/lab5/create')
def create_article():
    return render_template('lab5/create.html')
