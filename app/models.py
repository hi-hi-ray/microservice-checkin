import peewee

db = peewee.SqliteDatabase('dados.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Ticker(BaseModel):
    id = peewee.IntegerField(unique=True, index=True, primary_key=True)
    timestamp = peewee.TimestampField(null=False)
    type_stop = peewee.CharField(null=False)
    id_stop = peewee.CharField(null=True)


if __name__ == '__main__':
    try:
        Ticker.create_table()
        print("Tabela 'Ticker' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Ticker' ja existe!")
