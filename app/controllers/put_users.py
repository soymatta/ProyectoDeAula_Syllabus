from database.db import update

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset


id_param_name = "user_id"

def main(event):
     
    #Header
    try:
        data = event['body']
        params = {}

        if 'params' in event:
            params = event['params']

        # Get off the old var and replace it with a new one.
        if id_param_name in params:
            params['id'] = params.pop(id_param_name)
        
    except KeyError as e:
        return f"{R}* This method requires the params.{e}{RS}"

    # Body 

    permitted = (
        'name',
        'email',
        'password',
        'subjects',
        'role',
        'status',
        'faculties',
        'image',
        'last_update'
    )

    for i in  data:
        if i not in permitted:
            return {
                'status': False,
                'error_message': 'There are unvalid fields in the data'
            }

    validation = []
    result = {'data': [], 'status': False}

    # Response
    status = result['status']

    if not status:
        result.update({
            'data': [],
            'error': "UpdateException",
            'errorMessage': "Couldnt update the client register." 
        }) 

    return {'status': bool(result), 'data': result}


