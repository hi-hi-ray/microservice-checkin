import peewee

db = peewee.SqliteDatabase('db_order.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class ToyOrder(BaseModel):
    id = peewee.IntegerField(unique=True, index=True, primary_key=True)
    id_toy = peewee.IntegerField(null=False)
    quantity = peewee.IntegerField(null=False)


if __name__ == '__main__':
    try:
        ToyOrder.create_table()
        print("Tabela 'Toy Order' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Toy Order' já existe!")
