from models import ToyOrder


def create_item(id_toy_req, quantity_req):
    creation = ToyOrder.create(
        id_toy=id_toy_req,
        quantity=quantity_req)

    # syncer.send_to_sqs(creation.id,
    #                    creation.type_stop,
    #                    creation.id_stop,
    #                    'creation', creation.timestamp)

    if creation.id_toy is not None:
        return "Created Item"
    else:
        return "Failed to create item"


def get_orders():
    orders = ToyOrder.select()
    orders_array = []
    for orders in orders:
        item = {
            'id': orders.id,
            'id_toy': orders.id_toy,
            'quantity': orders.quantity
        }
        orders_array.append(item)
    return orders_array


def get_item_by_id(id_req):
    orders = ToyOrder.select().where(ToyOrder.id == id_req)
    orders_array = []
    for orders in orders:
        item = {
            'id': orders.id,
            'id_toy': orders.id_toy,
            'quantity': orders.quantity
        }
        orders_array.append(item)
    return orders_array


def delete_item(id_req):
    query_delete = ToyOrder.delete().where(ToyOrder.id == id_req)
    rows_delete = query_delete.execute()
    if rows_delete != 0:
        return "Deleted item"
    else:
        return "No item was deleted"


def update_item(id_req, id_toy_req, quantity_req):
    query_update = (ToyOrder.update({
        'id_toy': id_toy_req,
        'quantity': quantity_req
    }).where(ToyOrder.id == id_req))

    rows_updated = query_update.execute()
    if rows_updated != 0:
        # syncer.send_to_sqs(query_update.id,
        #                    query_update.type_stop,
        #                    query_update.id_stop,
        #                    'Update', query_update.timestamp)
        return "Item Updated"
    else:
        return "No item was updated"
