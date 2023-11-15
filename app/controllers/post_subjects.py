from database.db import insert
import datetime

def main(event):

    try:

        data = event['body']
        table = event['table']
        user = event['user']

        # User info (necessary)
        name = user['name']
        email = user['email']
        password = user['password']

    except Exception as e:
        return {
            'status': False,
            'error_message': f"Datos insuficientes, revise la data enviada. {e}"
        }
    
    # Body
    result = {'status': False, 'data': {} }

    defaults = {
        'status': 1,
        'role': 'teacher',
        'image': 'image.png',
        'last_update': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }

    frontend = data.copy()
    data.update(**defaults)
    data.update(**frontend)

    inserted = insert('users', data)

    result['status'] = bool(inserted)

    if not result['status']:
        return {
            'status_code': 404,
            'error_message': 'Algo pasó con el metodo de inserción, revise la tabla o data enviadas. 404'
        }
    
    return {
        'status_code': 200,
        'body': result['data']
    }
