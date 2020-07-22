from flask import Flask, jsonify, request
import sync as syncer

app = Flask(__name__)


@app.route('/health-check/', methods={'GET'})
def health_check_get():
    return jsonify({"message": "I`m well and alive, thanks for asking."})


@app.route('/send', methods={'POST'})
def add_sqs():
    request_data = request.get_json()
    syncer.send_to_sqs(request_data['id'],
                       request_data['type_stop'],
                       request_data['id_stop'],
                       request_data['type_alert'],
                       request_data['timestamp'])
    return jsonify({"message": "Check-in made"}), 200


@app.route('/sync', methods={'GET'})
def check_get():
    messages = syncer.get_from_sqs()
    return jsonify(messages), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
