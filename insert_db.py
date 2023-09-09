import psycopg2
from psycopg2.extras import execute_batch
import boto3

def insert_db(values):

    connection = psycopg2.connect(user="postgresUser",
                                  password="postgresPW",
                                  host="127.0.0.1",
                                  port="5455",
                                  database="postgres")
    cursor = connection.cursor()
    
    sql = "INSERT INTO warc(warc_filename, warc_record_length, warc_record_offset, warc_segment) VALUES(%(warc_filename)s, %(warc_record_length)s, %(warc_record_offset)s, %(warc_segment)s)"
    
    try:
        print(values)
        execute_batch(cursor, sql, values)
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

response = dynamodb_client.get_item(
    TableName="challenge",
    Key = {
        'url_surtkey': {'S': 'com,bjs)/product/snickers-twix--more-chocolate-candy-bars-full-size-variety-pack-30-ct/281053'},
        'url': {'S': 'https://www.bjs.com/product/snickers-twix--more-chocolate-candy-bars-full-size-variety-pack-30-ct/281053'}
    }
)

result = [{"warc_segment": response['Item']['warc_segment']['S'], 
    "warc_record_length": response['Item']['warc_record_length']['N'],
    "warc_filename": response['Item']['warc_filename']['S'],
    "warc_record_offset": response['Item']['warc_record_offset']['N']}]

insert_db(result)