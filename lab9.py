from flask import Blueprint, render_template, request, session, redirect, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('lab9.age'))
    return render_template('lab9/lab9.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('lab9.gender'))
    return render_template('lab9/age.html')

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')
        return redirect(url_for('lab9.preference'))
    return render_template('lab9/gender.html')

@lab9.route('/lab9/preference', methods=['GET', 'POST'])
def preference():
    if request.method == 'POST':
        session['preference'] = request.form.get('preference')
        return redirect(url_for('lab9.taste'))
    return render_template('lab9/preference.html')

@lab9.route('/lab9/taste', methods=['GET', 'POST'])
def taste():
    if request.method == 'POST':
        session['taste'] = request.form.get('taste')
        return redirect(url_for('lab9.congratulations'))
    return render_template('lab9/taste.html')

@lab9.route('/lab9/congratulations')
def congratulations():
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference = session.get('preference')
    taste = session.get('taste')

    # Определяем текст поздравления и картинку
    if gender == 'male':
        greeting = f"Поздравляю тебя, {name}! Желаю, чтобы ты быстро вырос, был умным и успешным."
    else:
        greeting = f"Поздравляю тебя, {name}! Желаю, чтобы ты быстро выросла, была умной и успешной."

    if preference == 'delicious':
        if taste == 'sweet':
            gift = "мешочек конфет"
            image = "lab9/candy.jpg"
        else:
            gift = "вкусный торт"
            image = "lab9/cake.jpg"
    else:
        if taste == 'sweet':
            gift = "красивую картину"
            image = "lab9/art.jpg"
        else:
            gift = "уютный плед"
            image = "lab9/blanket.jpg"

    return render_template('lab9/congratulations.html', greeting=greeting, gift=gift, image=image)