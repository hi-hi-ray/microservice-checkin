from models import Ticker
from datetime import datetime
import sync as syncer


def create_check(type_req, id_stop_req):
    now = datetime.now()
    timestamp_req = datetime.timestamp(now)
    creation = Ticker.create(timestamp=timestamp_req, type_stop=type_req,
                             id_stop=id_stop_req)

    syncer.send_to_sqs(creation.id,
                       creation.type_stop,
                       creation.id_stop,
                       'creation', creation.timestamp)

    if creation.type_stop is not None:
        return "Checkin made"
    else:
        return "Failed to check-in"


def get_checks():
    checks = Ticker.select()
    ticks = []
    for check in checks:
        tick = {
            'id': check.id,
            'timestamp': check.timestamp,
            'type_stop': check.type_stop,
            'id_stop': check.id_stop
        }
        ticks.append(tick)
    return ticks


def get_checks_by_id(id_req):
    checks = Ticker.select().where(Ticker.id == id_req)
    ticks = []
    for check in checks:
        tick = {
            'id': check.id,
            'timestamp': check.timestamp,
            'type_stop': check.type_stop,
            'id_stop': check.id_stop
        }
        ticks.append(tick)
    return ticks


def delete_check(id_req):
    query_delete = Ticker.delete().where(Ticker.id == id_req)
    rows_delete = query_delete.execute()
    if rows_delete != 0:
        return "Deleted checkin"
    else:
        return "No checkin was deleted"


def update_check(id_req, type_req, id_stop_req):
    query_update = (Ticker.update({
        'type_stop': type_req,
        'id_stop': id_stop_req}).where(Ticker.id == id_req))
    rows_updated = query_update.execute()
    if rows_updated != 0:
        return "Check-in Updated"
    else:
        return "No check was updated"
