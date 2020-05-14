from flask import Flask, jsonify, request
from flasgger import Swagger
import ticker as check_module
import sync as syncer

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


@app.route('/send', methods={'POST'})
def add_sqs():
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
    syncer.send_to_sqs(request_data['id'],
                       request_data['type_stop'],
                       request_data['id_stop'],
                       request_data['type_alert'],
                       request_data['timestamp'])
    return jsonify({"message": "Check-in made"}), 200



@app.route('/sync', methods={'GET'})
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


if __name__ == '__main__':
    app.run(port=5000, debug=True)
