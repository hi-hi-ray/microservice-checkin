import peewee

db = peewee.SqliteDatabase('db_stock.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class ToyStock(BaseModel):
    id = peewee.IntegerField(unique=True, index=True, primary_key=True)
    name = peewee.CharField(null=False)
    quantity = peewee.IntegerField(null=False)


if __name__ == '__main__':
    try:
        ToyStock.create_table()
        print("Tabela 'Toy Stock' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Toy Stock' já existe!")
