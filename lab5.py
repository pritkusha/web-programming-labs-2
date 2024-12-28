from flask import Blueprint, render_template, request, session, redirect, url_for, current_app, flash
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='sofiya_prytkova_knowledge_base',
            user='sofiya_prytkova_knowledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login').strip()
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error="Заполните поля")
    
    conn, cur = db_connect()

    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
        else:
            cur.execute("SELECT * FROM users WHERE LOWER(login)=LOWER(?);", (login,))
        
        user = cur.fetchone()
        if user is None:
            db_close(conn, cur)
            return render_template('lab5/login.html', error="Логин и/или пароль неверны")
        
        if not check_password_hash(user['password'], password):
            db_close(conn, cur)
            return render_template('lab5/login.html', error="Логин и/или пароль неверны")
        
        session['login'] = login
        db_close(conn, cur)
        return redirect(url_for('lab5.lab'))
    except Exception as e:
        db_close(conn, cur)
        return render_template('500.html'), 500

@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('lab5.lab'))

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login').strip()
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/register.html', error='Заполните все поля')
    
    conn, cur = db_connect()

    try:
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
        else:
            cur.execute("SELECT login FROM users WHERE login=?;", (login,))
        
        if cur.fetchone():
            db_close(conn, cur)
            return render_template('lab5/register.html', error="Такой пользователь уже существует")
        
        password_hash = generate_password_hash(password)
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))
        else:
            cur.execute("INSERT INTO users (login, password) VALUES (?, ?);", (login, password_hash))
        
        db_close(conn, cur)
        return redirect(url_for('lab5.login'))
    except Exception as e:
        db_close(conn, cur)
        return render_template('500.html'), 500

@lab5.route('/lab5/list')
def list_articles():
    login = session.get('login')
    if not login:
        return redirect(url_for('lab5.login'))
    
    conn, cur = db_connect()

    try:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
        user = cur.fetchone()
        if not user:
            db_close(conn, cur)
            return redirect(url_for('lab5.login'))
        
        user_id = user['id']
        cur.execute("SELECT * FROM articles WHERE user_id=?;", (user_id,))
        articles = cur.fetchall()
        
        db_close(conn, cur)
        return render_template('lab5/list.html', articles=articles, login=login)
    except Exception as e:
        db_close(conn, cur)
        return render_template('500.html'), 500

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect(url_for('lab5.login', next=url_for('lab5.create')))
    
    if request.method == 'GET':
        return render_template('lab5/create.html')
    
    title = request.form.get('title').strip()
    article_text = request.form.get('article_text').strip()

    if not (title and article_text):
        flash("Тема и текст статьи не могут быть пустыми", "error")
        return render_template('lab5/create.html')
    
    conn, cur = db_connect()

    try:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
        user = cur.fetchone()
        if not user:
            db_close(conn, cur)
            return redirect(url_for('lab5.login'))
        
        user_id = user['id']
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s);", (user_id, title, article_text))
        else:
            cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (?, ?, ?);", (user_id, title, article_text))
        
        db_close(conn, cur)
        return redirect(url_for('lab5.list'))
    except Exception as e:
        db_close(conn, cur)
        return render_template('500.html'), 500

@lab5.route('/lab5/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    login = session.get('login')
    if not login:
        return redirect(url_for('lab5.login'))
    
    conn, cur = db_connect()

    try:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
        user = cur.fetchone()
        if not user:
            db_close(conn, cur)
            return redirect(url_for('lab5.login'))
        
        user_id = user['id']
        cur.execute("SELECT * FROM articles WHERE id=? AND user_id=?;", (article_id, user_id))
        article = cur.fetchone()
        if not article:
            db_close(conn, cur)
            return redirect(url_for('lab5.list'))
        
        if request.method == 'GET':
            db_close(conn, cur)
            return render_template('lab5/edit.html', article=article)
        
        title = request.form.get('title').strip()
        article_text = request.form.get('article_text').strip()

        if not (title and article_text):
            flash("Тема и текст статьи не могут быть пустыми", "error")
            return render_template('lab5/edit.html', article=article)
        
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("UPDATE articles SET title=%s, article_text=%s WHERE id=%s;", (title, article_text, article_id))
        else:
            cur.execute("UPDATE articles SET title=?, article_text=? WHERE id=?;", (title, article_text, article_id))
        
        db_close(conn, cur)
        return redirect(url_for('lab5.list'))
    except Exception as e:
        db_close(conn, cur)
        return render_template('500.html'), 500

@lab5.route('/lab5/delete/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    login = session.get('login')
    if not login:
        return redirect(url_for('lab5.login'))
    
    conn, cur = db_connect()

    try:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
        user = cur.fetchone()
        if not user:
            db_close(conn, cur)
            return redirect(url_for('lab5.login'))
        
        user_id = user['id']
        cur.execute("DELETE FROM articles WHERE id=? AND user_id=?;", (article_id, user_id))
        db_close(conn, cur)
        return redirect(url_for('lab5.list'))
    except Exception as e:
        db_close(conn, cur)
        return render_template('500.html'), 500

@lab5.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500