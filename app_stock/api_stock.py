from flask import Flask, jsonify, request
import toystock as toy_module

app = Flask(__name__)


@app.route('/health-toy', methods={'GET'})
def health_toy_get():
    return jsonify({"message": "I`m well and alive, thanks for asking."})


@app.route('/toy', methods={'GET'})
def toy_get_all():
    toys = toy_module.get_toys()
    return jsonify(toys), 200


@app.route('/toy', methods={'POST'})
def toy_create():
    request_data = request.get_json()
    create_toy = toy_module.create_toy(request_data['name'],
                                       request_data['quantity'])
    if create_toy == "Checkin made":
        return jsonify({"message": "Toy created"}), 200
    else:
        return jsonify({"message": create_toy}), 500


@app.route('/toy/<string:id>', methods={'GET'})
def toy_get(id):
    toy = toy_module.get_toys_by_id(id)
    return jsonify(toy), 200


@app.route('/toy/<string:id>', methods={'DELETE'})
def toy_delete(id):
    delete_toy = toy_module.delete_toy(id)
    if delete_toy == "Deleted toy":
        return jsonify({"message": "Toy deleted"}), 200
    else:
        return jsonify({"message": delete_toy}), 500


@app.route('/toy/<string:id>', methods={'PUT'})
def toy_update(id):
    request_data = request.get_json()
    update_toy = toy_module.update_toy(id,
                                       request_data['name'],
                                       request_data['quantity'])
    if update_toy == "Toy Updated":
        return jsonify({"message": "Toy Updated"}), 200
    else:
        return jsonify({"message": update_toy}), 500


if __name__ == '__main__':
    app.run(port=5500, debug=True)
