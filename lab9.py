from flask import Blueprint, render_template

lab9 = Blueprint('lab8', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/lab9.html')