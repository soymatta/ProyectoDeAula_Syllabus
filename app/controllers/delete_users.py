from database.db import delete


R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

id_param_name = 'user_id'

def main(event):
    
    # Header
    try:
        params = event['params']

        if id_param_name in params:
            params['id'] = params.pop(id_param_name)

    except KeyError as e:
        return f"{R}* This method requires the parameters.{e}{RS}"
    
    # Body
    result = {'status': False, 'row_count': 0}

    result['status'] = bool(delete('users', params))

    if result['status']:
        result['row_count'] = 1

    # Response
    return {'status': bool(result), 'data': result}

