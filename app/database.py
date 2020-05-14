import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': info,
            }
        )

def insert_ticker(id, timestamp, type_stop, id_stop):
    pass


def get_tickers():
    pass


def update_ticker(id, timestamp, type_stop, id_stop):
    pass


def delete_ticker(id):
    pass


def get_ticker(id):
    pass
