from routes import main, request_parse, request
from controllers import post_faculties, get_faculties, put_faculties, delete_faculties

# POST
@main.route('/faculties', methods=['POST'])
def api_post_faculties():

    event = request_parse(request)
    
    response = post_faculties.main(event)

    return response

# GET
@main.route('/faculties/<faculty_id>/', methods=['GET'])
def api_get_faculties(faculty_id):

    event = request_parse(request)
    response = get_faculties.main(event)

    return response

# PUT
@main.route('/faculties/<faculty_id>', methods=['PUT'])
def api_put_faculties(faculty_id):

    event = request_parse(request)
    response = put_faculties.main(event)

    return response

# DELETE
@main.route('/faculties/<faculty_id>', methods=['DELETE'])
def api_delete_faculties(faculty_id):

    event = request_parse(request)
    response = delete_faculties.main(event)

    return response