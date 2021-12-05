import json
import boto3

# import requests

db = boto3.resource('dynamodb')
# dbTable = db.Table('resume')
dbTable = db.Table('Visitors')


def lambda_handler(event, context):
    print(dbTable.table_status)
    # rep = dbTable.get_item(Key= {'ID': '1'})
    rep = dbTable.get_item(Key={'VisitorCount': 1})

    count = rep["Item"]["VisitorCount"]
    new_count = count + 1
    result = dbTable.update_item(
        Key={'VisitorCount': 1},
        UpdateExpression='set VisitorCounter = :c',
        ExpressionAttributeValues={':c': new_count},
        ReturnValues='UPDATED_NEW'
    )
    print(result)
    return new_count