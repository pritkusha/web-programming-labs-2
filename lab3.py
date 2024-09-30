from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3' ,__name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'неизвестный')
    name_color = request.cookies.get('name_color', 'black')
    age = request.cookies.get('age', 'неизвестный')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    errors_a = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    
    age = request.args.get('age')
    if age == '':
        errors_a['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, 
                           sex=sex, errors=errors, errors_a=errors_a)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Стоимость напитков
    if drink == 'cofee':
        price = 120
    elif drink == 'black tea':
        price = 80
    else:
        price = 70

    #Стоимость добавок
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background_color = request.form.get('background_color')
    font_size = request.form.get('font_size')
    font_family = request.form.get('font_family')
    resp = make_response(redirect('lab3/settings'))
    if color:
            resp.set_cookie('color', color)
            return resp
    if background_color:
            resp.set_cookie('background_color', background_color)
            return resp
    if font_size:
            resp.set_cookie('font_size', font_size)
            return resp
    if font_family:
            resp.set_cookie('font_family', font_family)
            return resp
    
    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')
    font_family = request.cookies.get('font_family')
    resp = make_response(render_template('lab3/settings.html', color=color,
                                         background_color=background_color, 
                                         font_size=font_size, 
                                         font_family=font_family))
    return resp


@lab3.route("/lab3/train")
def train():
    full_name = request.form.get('full_name')
    shelf_type = request.form.get('shelf_type')
    with_linen = request.form.get('with_linen')
    with_luggage = request.form.get('with_luggage')
    age = request.form.get('age')
    departure_point = request.form.get('departure_point')
    destination_point = request.form.get('destination_point')
    travel_date = request.form.get('travel_date')
    insurance_needed = request.form.get('insurance_needed')
    
    # Проверка на пустые поля
    if not all([full_name, shelf_type, age, departure_point, destination_point, travel_date]):
        return render_template('lab3/ticketform.html', error="Все поля должны быть заполнены!")

    # Проверка возраста
    try:
        age = int(age)
        if not (1 <= age <= 120):
            return render_template('lab3/ticketform.html', error="Возраст должен быть от 1 до 120 лет!")
    except ValueError:
        return render_template('lab3/ticketform.html', error="Возраст должен быть числом!")

    # Рассчитываем стоимость
    ticket_price = 1000 if age >= 18 else 700
        
    if shelf_type in ['нижняя', 'нижняя боковая']:
        ticket_price += 100
    if with_linen == 'yes':
        ticket_price += 75
    if with_luggage == 'yes':
        ticket_price += 250
    if insurance_needed == 'yes':
        ticket_price += 150

    ticket_type = "Детский билет" if age < 18 else "Взрослый билет"

    return render_template('lab3/ticket.html', full_name=full_name, ticket_type=ticket_type, 
                            ticket_price=ticket_price, departure_point=departure_point,
                            destination_point=destination_point, travel_date=travel_date)

