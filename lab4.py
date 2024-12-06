from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4' ,__name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', 
                               error='Оба поля должны быть заполнены!')
    if x2 == 0:
        return render_template('lab4/div.html', 
                               error2='На нуль делить нельзя!')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, 
                           result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 0
    else:
        x1 = int(x1)
    if x2 == '':
        x2 = 0
    else:
        x2 = int(x2)

    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, 
                           result=result)

@lab4.route('/lab4/multiply-form')
def multiply_form():
    return render_template('lab4/multiply-form.html')

@lab4.route('/lab4/multiply', methods = ['POST'])
def multiply():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = 1
    else:
        x1 = int(x1)
    if x2 == '':
        x2 = 1
    else:
        x2 = int(x2)

    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/multiply.html', x1=x1, x2=x2, 
                           result=result)

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods = ['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', 
                               error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, 
                           result=result)

@lab4.route('/lab4/expon-form')
def expon_form():
    return render_template('lab4/expon-form.html')

@lab4.route('/lab4/expon', methods = ['POST'])
def expon():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/expon.html', 
                               error='Оба поля должны быть заполнены!')
    if x1 == 0 and x2 == 0:
        return render_template('lab4/expon.html', 
                               error2='Оба поля не должны быть нулевые!')

    x1 = int(x1)
    x2 = int(x2)
    result = x1 ** x2
    return render_template('lab4/expon.html', x1=x1, x2=x2, 
                           result=result)

tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        tree_count += 1
    
    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Алексей', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Дмитрий', 'gender': 'male'},
    {'login': 'sofi', 'password': '000', 'name': 'София', 'gender': 'female'}
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            user_data = next((user for user in users if user['login'] == login), None)
            name = user_data['name'] if user_data else ''

        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    error = None
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')

    if not login and not password:
        error = 'Не введен логин и пароль'
    elif not login:
        error = 'Не введен логин'
    elif not password:
        error = 'Не введен пароль'
    else:
        error = 'Неверные логин и/или пароль'

    return render_template('lab4/login.html', error=error, login=login, authorized=False)


@lab4.route('/lab4/logout', methods=['GET', 'POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/refrigerator', methods=['GET', 'POST'])
def refrigerator():
    temperature = None
    message = None
    snowflakes = 0

    if request.method == 'POST':
        try:
            temperature = float(request.form.get('temperature'))
            if temperature is None:
                message = "Ошибка: не задана температура"
            elif temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С"
                snowflakes = 3
            elif -9 < temperature <= -5:
                message = f"Установлена температура: {temperature}°С"
                snowflakes = 2
            elif -5 < temperature <= -1:
                message = f"Установлена температура: {temperature}°С"
                snowflakes = 1

        except ValueError:
            message = "Ошибка: введите числовое значение температуры"


    return render_template('lab4/refrigerator.html', temperature=temperature, message=message, snowflakes=snowflakes)


prices = {
    'ячмень': 12345,
    'овёс': 8522,
    'пшеница': 8722,
    'рожь': 14111
}

@lab4.route('/lab4/grain_order', methods=['GET', 'POST'])
def grain_order():
    grain_type = None
    weight = None
    total_price = None
    message = None
    discount = 0
    discount_message = ""

    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        try:
            weight = float(request.form.get('weight'))
            if weight <= 0:
                message = "Ошибка: вес должен быть больше 0"
            elif weight > 500:
                message = "Извините, такого объема зерна сейчас нет в наличии."
            else:
                price_per_ton = prices.get(grain_type)
                if price_per_ton is None:
                    message = "Ошибка: выберите тип зерна"
                else:
                    total_price = price_per_ton * weight
                    if weight > 50:
                        discount = 0.10
                        discount_amount = total_price * discount
                        total_price -= discount_amount
                        discount_message = f"Применена скидка за большой объем: {discount*100:.0f}% ({discount_amount:.2f} руб)"


        except ValueError:
            message = "Ошибка: введите числовое значение веса"


    return render_template('lab4/grain_order.html', grain_type=grain_type, weight=weight,
                           total_price=total_price, message=message, discount_message=discount_message, prices=prices)
