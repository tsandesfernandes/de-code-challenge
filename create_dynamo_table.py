import boto3

dyn_resources = boto3.resource('dynamodb')

table_name = "challenge"

schema = {
    "AttributeDefinitions": [
        {
            "AttributeName": "url_surtkey",
            "AttributeType": "S",
        },
        {
            "AttributeName": "url",
            "AttributeType": "S"
        },
       
    ],
    "KeySchema": [
        {"AttributeName": "url_surtkey", "KeyType": "HASH"},
        {"AttributeName": "url", "KeyType": "RANGE"},        
    ],
    "BillingMode": "PAY_PER_REQUEST",
    "TableName": table_name
}

table = dyn_resources.create_table(**schema)
print(f'Creating table {table_name}')
table.wait_until_exists()
print('Table created')
    