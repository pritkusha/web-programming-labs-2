from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')