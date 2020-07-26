from models import ToyOrder
import send_to_sqs as sync_sqs


def create_order(id_toy_req, quantity_req):
    creation = ToyOrder.create(
        id_toy=id_toy_req,
        quantity=quantity_req)

    if creation.id_toy is not None:
        response_sqs = sync_sqs.send_to_sqs(creation.id,
                                            creation.id_toy,
                                            creation.quantity)
        if response_sqs == "Success":
            return "Order Created"
        else:
            return "Failed to create order"
    else:
        return "Failed to create order"


def get_orders():
    orders = ToyOrder.select()
    orders_array = []
    for item in orders:
        order = {
            'id': item.id,
            'id_toy': item.id_toy,
            'quantity': item.quantity
        }
        orders_array.append(order)
    return orders_array


def get_order_by_id(id_req):
    orders = ToyOrder.select().where(ToyOrder.id == id_req)
    orders_array = []
    for item in orders:
        order = {
            'id': item.id,
            'id_toy': item.id_toy,
            'quantity': item.quantity
        }
        orders_array.append(order)
    return orders_array


def delete_order(id_req):
    query_delete = ToyOrder.delete().where(ToyOrder.id == id_req)
    rows_delete = query_delete.execute()
    if rows_delete != 0:
        return "Order Deleted"
    else:
        return "No order was deleted"


def update_order(id_req, id_toy_req, quantity_req):
    query_update = (ToyOrder.update({
        'id_toy': id_toy_req,
        'quantity': quantity_req
    }).where(ToyOrder.id == id_req))

    rows_updated = query_update.execute()
    if rows_updated != 0:
        return "Order Updated"
    else:
        return "No order was updated"
