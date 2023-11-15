from database.db import insert
import datetime
   
def main(event):

    try:

        data = event['body']

        # User info (necessary)
        name = data['name']
        email = data['email']
        password = data['password']

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

    result['data'].update(**defaults)
    result['data'].update(**data)

    # inserted = insert('users', data)

    result['status'] = True

    if not result['status']:
        return {
            'status_code': 404,
            'error_message': 'Algo pasó con el metodo de inserción, revise la tabla o data enviadas.'
        }

    return {
        'status_code': 200,
        'body': result['data']
    }

