from database.db import delete

id_param_name = 'version_id'

def main(event):
    
    # Header
    try:
        params = event['params']

        params['id'] = event['params'].pop(id_param_name)

    except Exception as e:
        return f"* Debe enviar el id de version.{e}"
    
    # Body
    result = {'status': False, 'row_count': 0}

    result['status'] = bool(delete('versions', params))
    
    if not result['status']:
        return {
            'status_code': 404,
            'error_message': 'Revisa los datos enviados. La tabla o los parametros son erroneos.'
        }
    
    # Response
    return {'status': bool(result), 'row_count': 1}