from database.db import update

id_param_name = "version_id"

def main(event):
     
    #Header
    try:
        data = event['body']
        params = {}

        # Get off the old var and replace it with a new one.
        params['id'] = event['params'].pop(id_param_name)
        
    except Exception as e:
        return f"* Para poder hacer un update, se necesita el id de la version.{e}"

    # Body 
    permitted = (
        'update_date',
        'description',
        'owner'
   
    )

    for field in  data:
        if field not in permitted:
            return {
                'status': False,
                'error_message': 'Algunos campos enviados NO pueden ser actualizados.'
            }

    result = {'status': False, 'row_count': 0}

    result['status'] = bool(update('versions', data, params))

    if not result['status']:
        return {
            'status_code': 404,
            'error_message': 'Revisa los datos enviados. La tabla, parametros o data pueden ser erroneos.'
        }

    return {'status': bool(result), 'row_count': 1}


