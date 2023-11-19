from routes import main, request_parse, request
from controllers import post_version, get_version, put_version, delete_version

# POST
@main.route('/versions', methods=['POST'])
def api_post_versions():
    
    event = request_parse(request)
    response = post_version.main(event)

    return response

# GET
@main.route('/versions/<version_id>/', methods=['GET'])
def api_get_versions(version_id):

    event = request_parse(request)
    response = get_version.main(event)

    return response

# PUT
@main.route('/versions/<version_id>', methods=['PUT'])
def api_put_versions(version_id):

    event = request_parse(request)
    response = put_version.main(event)

    return response

# DELETE
@main.route('/versions/<version_id>', methods=['DELETE'])
def api_delete_versions(version_id):

    event = request_parse(request)
    response = delete_version.main(event)

    return response