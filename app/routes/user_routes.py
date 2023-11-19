from routes import main, request_parse, request
from controllers import post_users, get_users, put_users, delete_users


# POST
@main.route('/users', methods=['POST'])
def api_post_users():
    
    event = request_parse(request)
    response = post_users.main(event)

    return response

#GET
@main.route('/users/<user_id>', methods=['GET'])
def api_get_users(user_id):

    event = request_parse(request)
    response = get_users.main(event)

    return response

# PUT
@main.route('/users/<user_id>', methods=['PUT'])
def api_put_users():
    
    event = request_parse(request)
    response = put_users.main(event)

    return response

# DELETE
@main.route('/users/<user_id>', methods=['DELETE'])
def api_delete_users(user_id):

    event = request_parse(request)
    response = delete_users.main(event)

    return response