from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for, abort
from db import db
from db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html', username="anonymous")

@lab8.route('/lab8/login')
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form or not password_form:
        return render_template('lab8/login.html', error='Логин и пароль не могут быть пустыми')

    user = users.query.filter_by(login = login_form).first()

    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember= False)
            return redirect('/lab8/')
    
    return render_template('lab8/login.html',
                           error = 'Ошибка входа: логин и/или пароль неверны')

@lab8.route('/lab8/register') 
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form or not password_form:
        return render_template('lab8/register.html', error='Логин и пароль не могут быть пустыми')

    login_exists = users.query.filter_by(login = login_form).first()
    if login_exists:
        return render_template('lab8/register.html',
                               error='Такой пользователь уже существует')
    
    password_hash = users(login = login_form, password = password_hash)
    new_user = users(login = login_form, password = password_form)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/lab8/')

@lab8.route('/lab8/articles')
@login_required
def articles():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/create')
def create():
    return render_template('lab8/lab8.html')
