from routes import main, request_parse, request
from controllers import post_subjects, get_subjects, put_subjects, delete_subjects

# POST
@main.route('/subjects', methods=['POST'])
def api_post_subjects():

    event = request_parse(request)
    response = post_subjects.main(event)

    return response

# GET
@main.route('/subjects/<subject_id>', methods=['GET'])
def api_get_subjects(subject_id):

    event = request_parse(request)
    response = get_subjects.main(event)

    return response


# PUT
@main.route('/subjects/<subject_id>', methods=['PUT'])
def api_put_subjects(subject_id):

    event = request_parse(request)
    response = put_subjects.main(event)

    return response

# DELETE
@main.route('/subjects/<subject_id>', methods=['DELETE'])
def api_delete_subjects(subject_id):

    event = request_parse(request)
    response = delete_subjects.main(event)

    return response