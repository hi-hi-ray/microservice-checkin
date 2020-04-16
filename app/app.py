from flask import Flask, jsonify, request
from flasgger import Swagger
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


@app.route('/check', methods={'GET'})
def check_get_all():
    """Get all your check-ins
    ---
    tags:
      - check-in / ticker
    definitions:
      checks:
        type: object
        properties:
          checks:
            type: array
            items:
              id : string
              timestamp: timestamp
              type_stop: string
              id_stop: string
      id:
        type: string
      timestamp:
        type: timestamp
      type_stop:
        type: string
      id_stop:
        type: string
    responses:
      500:
        description: Failed in application.
        schema:
        examples:
          message: 'a message will appear'
      200:
        description: Ok and an array of your checks.
        schema:
        examples:
          checks: "#/ref/definitions/checks"
    """
    checks = check_module.get_checks()
    return jsonify(checks), 200


@app.route('/check', methods={'POST'})
def check_create():
    """Create your check-in
  ---
  tags:
    - check-in / ticker
  parameters:
    - in: body
      name: body
      description: JSON parameters.
      schema:
        properties:
          type_stop:
            type: string
            description: Type of stop.
            example: Bus
          id_stop:
            type: string
            description: Id of stop.
            example: Bus Jacaparepagua1
  responses:
    500:
      description: Failed in application.
      schema:
      examples:
        message: 'a message will appear'
    200:
      description: Ok and an array of your checks.
      schema:
      examples:
        message: 'Check-in made'
  """
    request_data = request.get_json()
    create_checkin = check_module.create_check(
        request_data['type_stop'],
        request_data['id_stop'])
    if create_checkin == "Checkin made":
        return jsonify({"message": "Check-in made"}), 200
    else:
        return jsonify({"message": create_checkin}), 500


@app.route('/check/<string:id>', methods={'GET'})
def check_get(id):
    """Get your check-in
    ---
    tags:
      - check-in / ticker
    parameters:
      - in: path
        name: id
        description: Path parameter.
        schema:
          properties:
            id:
              type: string
              required: true
              description: Id to search.
              example: 1
    definitions:
      checks:
        type: object
        properties:
          checks:
            type: array
            items:
              id : string
              timestamp: timestamp
              type_stop: string
              id_stop: string
      id:
        type: string
      timestamp:
        type: timestamp
      type_stop:
        type: string
      id_stop:
        type: string
    responses:
      500:
        description: Failed in application.
        schema:
        examples:
          message: 'a message will appear'
      200:
        description: Ok and an array of your check-in.
        schema:
        examples:
          checks: "#/ref/definitions/checks"
    """
    check = check_module.get_checks_by_id(id)
    return jsonify(check), 200


@app.route('/check/<string:id>', methods={'DELETE'})
def check_delete(id):
    """Delete your check-in
    ---
    tags:
      - check-in / ticker
    parameters:
      - in: path
        name: id
        description: Path parameter.
        schema:
          properties:
            id:
              type: string
              required: true
              description: Id to search.
              example: 1
    definitions:
      checks:
        type: object
        properties:
          checks:
            type: array
            items:
              id : string
              timestamp: timestamp
              type_stop: string
              id_stop: string
      id:
        type: string
      timestamp:
        type: timestamp
      type_stop:
        type: string
      id_stop:
        type: string
    responses:
      500:
        description: Failed in application.
        schema:
        examples:
          message: 'a message will appear'
      200:
        description: Ok and a message.
        schema:
        examples:
          checks: "#/ref/definitions/checks"
    """
    delete_pill = check_module.delete_check(id)
    if delete_pill == "Deleted checkin":
        return jsonify({"message": "Check-in deleted"}), 200
    else:
        return jsonify({"message": delete_pill}), 500


@app.route('/check/<string:id>', methods={'PUT'})
def check_update(id):
    """Update all your check-in
  ---
  tags:
    - check-in / ticker
  parameters:
    - in: path
      name: id
      description: Path parameter.
      schema:
        properties:
          id:
            type: string
            required: true
            description: Id to search.
            example: 1
    - in: body
      name: body
      description: JSON parameters.
      schema:
        properties:
          type_stop:
            type: string
            description: Type of stop.
            example: Bus
          id_stop:
            type: string
            description: Id of stop.
            example: Bus Jacaparepagua1
  responses:
    500:
      description: Failed in application.
      schema:
      examples:
        message: 'a message will appear'
    200:
      description: Ok and an array of your checks.
      schema:
      examples:
        message: 'Check-in Updated'
  """
    request_data = request.get_json()
    update_checkin = check_module.update_check(id,
                                               request_data['type_stop'],
                                               request_data['id_stop'])
    if update_checkin == "Check-in Updated":
        return jsonify({"message": "Check-in Updated"}), 200
    else:
        return jsonify({"message": update_checkin}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
