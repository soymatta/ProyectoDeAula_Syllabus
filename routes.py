import json
import functools
from flask import (render_template, redirect, blueprints,
                   session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash
from app.controllers import *

main = blueprints.Blueprint('main', __name__)


# ------------------------ Template Rendering ------------------------

# Menu / Home
@main.route('/menu', methods=['GET'])
def menu():
    return render_template('/menu.html')

# Login 
@main.route('/login', methods=['GET'])
def login():
    return render_template('/login.html')

# Admin option panel
@main.route('/admin/options', methods=['GET'])
def admin():
    return render_template('/adminPanel.html')

# Admin panel
@main.route('/admin/denied')
def admin_denied():
    return render_template('/adminDenegado.html')

# Editor online
@main.route('/editor', methods=['GET'])
def editor():
    return render_template('/editor.html')

# Cerrar sesión
@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('menu'))

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

# ------------------- Methods Routes -------------------------

# -------------------- POST --------------------
@main.route('/users', methods=['POST'])
def api_post_users():
    
    event = request_parse(request)
    response = post_users.main(event)

    return response

@main.route('/subjects', methods=['POST'])
def api_post_subjects():

    event = request_parse(request)
    response = post_subjects.main(event)

    return response


@main.route('/faculties', methods=['POST'])
def api_post_faculties():

    event = request_parse(request)
    
    response = post_faculties.main(event)

    return response

@main.route('/syllabus', methods=['POST'])
def api_post_syllabus():
    
    event = request_parse(request)
    response = post_syllabus.main(event)

    return response

@main.route('/versions', methods=['POST'])
def api_post_versions():
    
    event = request_parse(request)
    response = post_version.main(event)

    return response

# -------------------- GET --------------------
@main.route('/users/<user_id>', methods=['GET'])
def api_get_users(user_id):

    event = request_parse(request)
    response = get_users.main(event)

    return response


@main.route('/subjects/<subject_id>', methods=['GET'])
def api_get_subjects(subject_id):

    event = request_parse(request)
    response = get_subjects.main(event)

    return response


@main.route('/faculties/<faculty_id>/', methods=['GET'])
def api_get_faculties(faculty_id):

    event = request_parse(request)
    response = get_faculties.main(event)

    return response


@main.route('/syllabus/<syllabus_id>/', methods=['GET'])
def api_get_syllabus(syllabus_id):

    event = request_parse(request)
    response = get_syllabus.main(event)

    return response


@main.route('/versions/<version_id>/', methods=['GET'])
def api_get_versions(version_id):

    event = request_parse(request)
    response = get_version.main(event)

    return response


# -------------------- PUT --------------------
@main.route('/users/<user_id>', methods=['PUT'])
def api_put_users():
    
    event = request_parse(request)
    response = put_users.main(event)

    return response


@main.route('/subjects/<subject_id>', methods=['PUT'])
def api_put_subjects(subject_id):

    event = request_parse(request)
    response = put_subjects.main(event)

    return response


@main.route('/faculties/<faculty_id>', methods=['PUT'])
def api_put_faculties(faculty_id):

    event = request_parse(request)
    response = put_faculties.main(event)

    return response


@main.route('/syllabus/<syllabus_id>', methods=['PUT'])
def api_put_syllabus(syllabus_id):

    event = request_parse(request)
    response = put_syllabus.main(event)

    return response


@main.route('/versions/<version_id>', methods=['PUT'])
def api_put_versions(version_id):

    event = request_parse(request)
    response = put_version.main(event)

    return response


# -------------------- DELETE -------------------- 
@main.route('/users/<user_id>', methods=['DELETE'])
def api_delete_users(user_id):

    event = request_parse(request)
    response = delete_users.main(event)

    return response


@main.route('/subjects/<subject_id>', methods=['DELETE'])
def api_delete_subjects(subject_id):

    event = request_parse(request)
    response = delete_subjects.main(event)

    return response


@main.route('/faculties/<faculty_id>', methods=['DELETE'])
def api_delete_faculties(faculty_id):

    event = request_parse(request)
    response = delete_faculties.main(event)

    return response


@main.route('/syllabus/<syllabus_id>', methods=['DELETE'])
def api_delete_syllabus(syllabus_id):

    event = request_parse(request)
    response = delete_syllabus.main(event)

    return response


@main.route('/versions/<version_id>', methods=['DELETE'])
def api_delete_versions(version_id):

    event = request_parse(request)
    response = delete_syllabus.main(event)

    return response
