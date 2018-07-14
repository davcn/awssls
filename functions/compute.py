import os
import uuid
import decimal
from contextlib import closing
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore

def handler(event, context):
    recordId = event["recordId"]
    dataId = event["dataId"]

    # Retrieving information about the sonda from DynamoDB table
    dataItem  = findById('dataTable', recordId)
    checkItem = findById('checkTable', dataId)
    
    sondaSpeed = dataItem["Items"][0]["speed"]
    checkSpeed = checkItem["Items"][0]["speed"]

    result = calc(sondaSpeed, checkSpeed)
    
    #Creating new record in DynamoDB table
    id = str(uuid.uuid4())
    table = getTable('resultsTable')
    table.put_item(
      Item={
        'id' : id,
        'speed' : result
      }
    )
    return result



def calc(sonda, real):
    return sonda * real * decimal.Decimal(10)

def getDynamoResource():
    return boto3.resource('dynamodb')

def getTable(tableName):
    return getDynamoResource().Table(tableName)

def findById(tableName, id):
    return getTable(tableName).query(KeyConditionExpression=Key('id').eq(id))


