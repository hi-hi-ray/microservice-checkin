import peewee

db = peewee.SqliteDatabase('dados.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(unique=True, null=False, index=True)
    password = peewee.CharField(null=False)
    token = peewee.CharField(null=False, primary_key=True)


class Ticker(BaseModel):
    id = peewee.IntegerField(unique=True, index=True, primary_key=True)
    timestamp = peewee.TimestampField(null=False)
    type_stop = peewee.CharField(null=False)
    id_stop = peewee.CharField(null=True)
    user_fk = peewee.CharField(null=True)


if __name__ == '__main__':
    try:
        User.create_table()
        print("Tabela 'User' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'User' ja existe!")
    try:
        Ticker.create_table()
        print("Tabela 'Ticker' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Ticker' ja existe!")
