from models import ToyStock
# import sync as syncer


def create_item(name_req, quantity_req, description_req=None):
    creation = ToyStock.create(
        name=name_req,
        description=description_req,
        quantity=quantity_req)

    # syncer.send_to_sqs(creation.id,
    #                    creation.type_stop,
    #                    creation.id_stop,
    #                    'creation', creation.timestamp)

    if creation.name is not None:
        return "Created Item"
    else:
        return "Failed to create item"


def get_itens():
    itens = ToyStock.select()
    itens_array = []
    for itens in itens:
        item = {
            'id': itens.id,
            'name': itens.name,
            'description': itens.description,
            'quantity': itens.quantity
        }
        itens_array.append(item)
    return itens_array


def get_item_by_id(id_req):
    itens = ToyStock.select().where(ToyStock.id == id_req)
    itens_array = []
    for itens in itens:
        item = {
            'id': itens.id,
            'name': itens.name,
            'description': itens.description,
            'quantity': itens.quantity
        }
        itens_array.append(item)
    return itens_array


def delete_item(id_req):
    query_delete = ToyStock.delete().where(ToyStock.id == id_req)
    rows_delete = query_delete.execute()
    if rows_delete != 0:
        return "Deleted item"
    else:
        return "No item was deleted"


def update_item(id_req, name_req, quantity_req, description_req=None):
    query_update = (ToyStock.update({
        'name': name_req,
        'description': quantity_req,
        'quantity': description_req
    }).where(ToyStock.id == id_req))

    rows_updated = query_update.execute()
    if rows_updated != 0:
        # syncer.send_to_sqs(query_update.id,
        #                    query_update.type_stop,
        #                    query_update.id_stop,
        #                    'Update', query_update.timestamp)
        return "Item Updated"
    else:
        return "No item was updated"
