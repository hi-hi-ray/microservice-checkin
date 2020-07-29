from flask import Flask, jsonify, request
import toyorder as toy_order

app = Flask(__name__)


@app.route('/health-check', methods={'GET'})
def health_check_get():
    return jsonify({"message": "I`m well and alive, thanks for asking."})


@app.route('/order', methods={'GET'})
def order_get_all():
    orders = toy_order.get_orders()
    return jsonify(orders), 200


@app.route('/order', methods={'POST'})
def order_create():
    request_data = request.get_json()
    create_order = toy_order.create_order(
        request_data['id_toy'],
        request_data['quantity'])
    if create_order == "Order Created":
        return jsonify({"message": "Order Created"}), 200
    else:
        return jsonify({"message": create_order}), 500


@app.route('/order/<string:id>', methods={'GET'})
def order_get(id):
    order = toy_order.get_order_by_id(id)
    return jsonify(order), 200


@app.route('/order/<string:id>', methods={'DELETE'})
def order_delete(id):
    delete_order = toy_order.delete_order(id)
    if delete_order == "Order Deleted":
        return jsonify({"message": "Order Deleted"}), 200
    else:
        return jsonify({"message": delete_order}), 500


@app.route('/order/<string:id>', methods={'PUT'})
def order_update(id):
    request_data = request.get_json()
    update_order = toy_order.update_order(id,
                                               request_data['id_toy'],
                                               request_data['quantity'])
    if update_order == "Order Updated":
        return jsonify({"message": "Order Updated"}), 200
    else:
        return jsonify({"message": update_order}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
