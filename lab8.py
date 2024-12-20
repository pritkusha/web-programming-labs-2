from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for, abort
from datetime import datetime

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/lab8.html', username="anonymous")

@lab8.route('/lab8/login')
def login():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/register')
def registern():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/articles')
def articles():
    return render_template('lab8/lab8.html')

@lab8.route('/lab8/create')
def create():
    return render_template('lab8/lab8.html')