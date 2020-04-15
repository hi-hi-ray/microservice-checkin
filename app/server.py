from flask import Flask, jsonify, request
from flasgger import Swagger
import authentication as auth_module
import ticker as check_module


app = Flask(__name__)
swagger = Swagger(app)


@app.route('/health-check/', methods={'GET'})
def health_check_get():
    """This endpoint shows that the application it`s up.
    ---
    tags:
      - health check
    definitions:
      message:
        type: string
    responses:
      200:
        description: A message will appear
        schema:
        examples:
          message: 'I`m well and alive, thanks for asking.'
    """
    return jsonify({"message": "I`m well and alive, thanks for asking."})


@app.route('/user/create', methods={'POST'})
def auth_create():
    """Create a new user
   ---
   tags:
     - user
   parameters:
     - in: body
       name: body
       description: JSON parameters.
       schema:
         properties:
           username:
             type: string
             description: Username to be created.
             example: Teste123
           password:
             type: string
             description: Password to be created.
             example: senha1234
   responses:
     201:
       description: Created.
       schema:
       examples:
         message: 'a message will appear'
     409:
       description: Failed to create user.
       schema:
       examples:
         message: 'a message will appear'
     500:
       description: Internal server error.
       schema:
       examples:
         message: 'a message will appear'

    """
    request_data = request.get_json()
    creation_status = auth_module.create_auth(
        request_data['username'],
        request_data['password'])
    if creation_status == "Created User":
        return jsonify({"message": creation_status}), 201
    elif creation_status == "Username already exists.":
        return jsonify({"message": creation_status}), 409
    elif creation_status == "Failed Creating User":
        return jsonify({"message": creation_status}), 500
    else:
        return jsonify({"message": "Unknown Error, sorry we didn't see this coming"}), 500


@app.route('/user/auth', methods={'POST'})
def auth_post():
    """Authenticate user
   ---
   tags:
     - user
   parameters:
     - in: body
       name: body
       description: JSON parameters.
       schema:
         properties:
           username:
             type: string
             description: Username to be created.
             example: Teste123
           password:
             type: string
             description: Password to be created.
             example: senha1234
   definitions:
      token:
        type: string
   responses:
     403:
       description: Failed in authentication.
       schema:
       examples:
         message: 'a message will appear'
     200:
       description: Ok and token to use.
       schema:
       examples:
         token: 'a token will appear'
   """
    request_data = request.get_json()
    user_token = auth_module.do_auth(
        request_data['username'],
        request_data['password'])
    if user_token == "Username or Password invalid." or user_token == "Username does not exist.":
        return jsonify({"message": "Check the informations, please"}), 403
    else:
        return jsonify({"token": user_token}), 200


@app.route('/check', methods={'GET'})
def check_get_all():
    """Get all your check-ins
    ---
    tags:
      - check-in / ticker
    parameters:
      - in: header
        name: header
        description: Header parameter.
        schema:
          properties:
            token:
              type: string
              description: Token to use.
              example: dx62hy0v
   definitions:
      checks:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      403:
        description: Failed in authentication.
        schema:
        examples:
          message: 'a message will appear'
      200:
        description: Ok and token to use.
        schema:
        examples:
          token: 'a token will appear'
    """
    token = request.headers.get('token')
    if token is None:
        return jsonify({"message": "Please check the header the token parameter is missing."}), 403
    access_flag = auth_module.check_token(token)
    if access_flag == "DENIED.":
        return jsonify({"message": "Invalid token"}), 403
    else:
        checks = check_module.get_checks(token)
        return jsonify(checks), 200


@app.route('/check', methods={'POST'})
def check_create():
    """Get all your check-ins
    ---
    tags:
      - check-in / ticker
    parameters:
      - in: header
        name: header
        description: Header parameter.
        schema:
          properties:
            token:
              type: string
              description: Token to use.
              example: dx62hy0v
      - in: body
        name: body
        description: JSON parameters.
        schema:
          properties:
            username:
              type: string
              description: Username to be created.
              example: Teste123
            password:
              type: string
              description: Password to be created.
              example: senha1234
    responses:
      403:
        description: Failed in authentication.
        schema:
        examples:
          message: 'a message will appear'
      200:
        description: Ok and token to use.
        schema:
        examples:
          token: 'a token will appear'
    """
    token = request.headers.get('token')
    if token is None:
        return jsonify({"message": "Please check the header the token parameter is missing."}), 403
    access_flag = auth_module.check_token(token)
    if access_flag == "DENIED.":
        return jsonify({"message": "Invalid token"}), 403
    else:
        request_data = request.get_json()
        create_pill = check_module.create_site(
            request_data['category'],
            request_data['name'],
            request_data['content'],
            request_data['highlight'],
            request_data['origin_address'],
            token)
        if create_pill == "Created check":
            return jsonify({"token": "Pill saved"}), 200
        else:
            return jsonify({"message": create_pill}), 500


@app.route('/check/<string:id>', methods={'GET'})
def check_get(id):
    token = request.headers.get('token')
    if token is None:
        return jsonify({"message": "Please check the header the token parameter is missing."}), 403
    access_flag = auth_module.check_token(token)
    if access_flag == "DENIED.":
        return jsonify({"message": "Invalid token"}), 403
    else:
        check = check_module.get_site_by_id(id)
        return jsonify(check), 200


@app.route('/check/<string:id>', methods={'DELETE'})
def check_delete(id):
    token = request.headers.get('token')
    if token is None:
        return jsonify({"message": "Please check the header the token parameter is missing."}), 403
    access_flag = auth_module.check_token(token)
    if access_flag == "DENIED.":
        return jsonify({"message": "Invalid token"}), 403
    else:
        delete_pill = check_module.delete_site(id)
        if delete_pill == "Deleted pill":
            return jsonify({"token": "Pill saved"}), 200
        else:
            return jsonify({"message": delete_pill}), 500


@app.route('/check/<string:id>', methods={'PUT'})
def check_update(id):
    token = request.headers.get('token')
    if token is None:
        return jsonify({"message": "Please check the header the token parameter is missing."}), 403
    access_flag = auth_module.check_token(token)
    if access_flag == "DENIED.":
        return jsonify({"message": "Invalid token"}), 403
    else:
        request_data = request.get_json()
        update_checkin = check_module.update_site(id,
                                                  request_data['timestamp'],
                                                  request_data['type_stop'],
                                                  request_data['id_stop'],
                                                  token)
        if update_checkin == "Updated pill":
            return jsonify({"token": "Pill updated"}), 200
        else:
            return jsonify({"message": update_checkin}), 500


app.run(port=5000, debug=True)