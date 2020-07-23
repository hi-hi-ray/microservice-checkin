from models import ToyStock
# import sync as syncer


def create_item(name_req, quantity_req):
    creation = ToyStock.create(
        name=name_req,
        quantity=quantity_req)

    # syncer.send_to_sqs(creation.id,
    #                    creation.type_stop,
    #                    creation.id_stop,
    #                    'creation', creation.timestamp)

    if creation.name is not None:
        return "Toy created"
    else:
        return "Failed to create toy"


def get_items():
    items = ToyStock.select()
    items_array = []
    for item in items:
        toy = {
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity
        }
        items_array.append(toy)
    return items_array


def get_item_by_id(id_req):
    items = ToyStock.select().where(ToyStock.id == id_req)
    items_array = []
    for item in items:
        toy = {
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity
        }
        items_array.append(toy)
    return items_array


def delete_item(id_req):
    query_delete = ToyStock.delete().where(ToyStock.id == id_req)
    rows_delete = query_delete.execute()
    if rows_delete != 0:
        return "Deleted toy"
    else:
        return "No toy was deleted"


def update_item(id_req, name_req, quantity_req):
    query_update = (ToyStock.update({
        'name': name_req,
        'quantity': quantity_req
    }).where(ToyStock.id == id_req))

    rows_updated = query_update.execute()
    if rows_updated != 0:
        # syncer.send_to_sqs(query_update.id,
        #                    query_update.type_stop,
        #                    query_update.id_stop,
        #                    'Update', query_update.timestamp)
        return "Toy Updated"
    else:
        return "No toy was updated"
