import json
import functools
from flask import (render_template, redirect, blueprints,
                   session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash

main = blueprints.Blueprint('main', __name__)

# ------------------- Structure Methods -----------------

def request_parse(request):
    
    body = {}
    params = {}

    # Params update
    for k, v in request.view_args.items():

        params.update({k : json.loads(v)})

    # Body create
    print(request.data)
    body = json.loads(request.data.decode("utf-8"))

    # Response structure
    event = {
        'body': body,
        'params': params
    }

    print(event)
    return event

def param_loads(str_params: str):

    path = []
    for i in str_params.split("&"):
        path.append(i.split("="))

    dictionary = {}
    for key, val in path:
        dictionary.update({key : val})

    return dictionary

