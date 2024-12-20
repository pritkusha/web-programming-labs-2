from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for

lab6 = Blueprint('lab6', __name__)

offices = []
for i in range(1, 11):
    offices.append({"number": i, "tenant": ""})

@lab6.route('/lab6/')
def main():
    # Проверяем, авторизован ли пользователь
    if 'login' not in session:
        return redirect(url_for('lab6.login_page'))  # Перенаправляем на страницу авторизации

    return render_template('lab6/lab6.html')

@lab6.route('/lab6/login')
def login_page():
    return render_template('lab6/login.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data.get('id')
    method = data.get('method')

    print(f"Session data: {session}")  # Отладочный вывод

    if method == 'info':
        return jsonify({
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        })

    login = session.get('login')
    if not login:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }), 401

    if method == 'booking':
        office_number = data.get('params')
        if not office_number:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': -32602,
                    'message': 'Invalid params'
                },
                'id': id
            }), 400

        for office in offices:
            if office['number'] == office_number:
                if office['tenant']:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }), 400

                office['tenant'] = login
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })

        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': -32602,
                'message': 'Office not found'
            },
            'id': id
        }), 400

    if method == 'cancellation':
        office_number = data.get('params')
        if not office_number:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': -32602,
                    'message': 'Invalid params'
                },
                'id': id
            }), 400

        for office in offices:
            if office['number'] == office_number:
                if not office['tenant']:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 3,
                            'message': 'Office is not booked'
                        },
                        'id': id
                    }), 400

                if office['tenant'] != login:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 4,
                            'message': 'You are not the tenant of this office'
                        },
                        'id': id
                    }), 400

                office['tenant'] = ''
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })

        return jsonify({
            'jsonrpc': '2.0',
            'error': {
                'code': -32602,
                'message': 'Office not found'
            },
            'id': id
        }), 400

    return jsonify({
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }), 404

@lab6.route('/lab6/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password':
        session['login'] = username
        return jsonify({'message': 'Logged in successfully'}), 200
    else:
        return jsonify({'error': {'code': 1, 'message': 'Invalid credentials'}}), 401