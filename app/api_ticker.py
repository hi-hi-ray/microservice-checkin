from flask import Flask, jsonify, request
import ticker as check_module

app = Flask(__name__)


@app.route('/health-check', methods={'GET'})
def health_check_get():
    return jsonify({"message": "I`m well and alive, thanks for asking."})


@app.route('/check', methods={'GET'})
def check_get_all():
    checks = check_module.get_checks()
    return jsonify(checks), 200


@app.route('/check', methods={'POST'})
def check_create():
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
    check = check_module.get_checks_by_id(id)
    return jsonify(check), 200


@app.route('/check/<string:id>', methods={'DELETE'})
def check_delete(id):
    delete_check = check_module.delete_check(id)
    if delete_check == "Deleted checkin":
        return jsonify({"message": "Check-in deleted"}), 200
    else:
        return jsonify({"message": delete_check}), 500


@app.route('/check/<string:id>', methods={'PUT'})
def check_update(id):
    request_data = request.get_json()
    update_checkin = check_module.update_check(id,
                                               request_data['type_stop'],
                                               request_data['id_stop'])
    if update_checkin == "Check-in Updated":
        return jsonify({"message": "Check-in Updated"}), 200
    else:
        return jsonify({"message": update_checkin}), 500


if __name__ == '__main__':
    app.run(port=5500, debug=True)
