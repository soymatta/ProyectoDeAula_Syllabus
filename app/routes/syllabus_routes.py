from routes import main, request_parse, request
from controllers import post_syllabus, get_syllabus, put_syllabus, delete_syllabus

# POST
@main.route('/syllabus', methods=['POST'])
def api_post_syllabus():
    
    event = request_parse(request)
    response = post_syllabus.main(event)

    return response

# GET
@main.route('/syllabus/<syllabus_id>/', methods=['GET'])
def api_get_syllabus(syllabus_id):

    event = request_parse(request)
    response = get_syllabus.main(event)

    return response

# PUT
@main.route('/syllabus/<syllabus_id>', methods=['PUT'])
def api_put_syllabus(syllabus_id):

    event = request_parse(request)
    response = put_syllabus.main(event)

    return response

# DELETE
@main.route('/syllabus/<syllabus_id>', methods=['DELETE'])
def api_delete_syllabus(syllabus_id):

    event = request_parse(request)
    response = delete_syllabus.main(event)

    return response