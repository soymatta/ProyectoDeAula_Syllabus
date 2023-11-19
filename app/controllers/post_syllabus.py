from database.db import insert
import datetime
   
def main(event):

    try:

        data = event['body']

        # Subjects info (necessary)
        
        bibliography = data['bibliography']
        subject_id  = data['subject_id']
        faculty_id  = data['faculty_id']


    except Exception as e:
        return {
            'status': False,
            'error_message': f"Datos insuficientes, revise la data enviada. {e}"
        }
    
    # Body
    result = {'status': False, 'data': {} }

    defaults = {
       
    }

    result['data'].update(**defaults)
    result['data'].update(**data)

    result['status'] = bool(insert('syllabus', data))
 
    if not result['status']:
        return {
            'status_code': 404,
            'error_message': 'Algo pasó con el metodo de inserción, revise la tabla o data enviadas.'
        }

    return {
        'status_code': 200,
        'body': result['data']
    }