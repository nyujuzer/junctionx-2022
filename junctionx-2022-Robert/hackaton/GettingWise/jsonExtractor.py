from itertools import count
import requests
import json

url_finsfprava = "https://ekasa.financnasprava.sk/mdu/api/v1/opd/receipt/find"

def over(string: id):
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    data = {"receiptId": id}
    json_object = json.dumps(data, indent = 4)
    a =  json.dumps((requests.post(url=url_finsfprava,headers=headers,data=json_object).json()))
    price = a['receipt']['totalPrice']
    Id = a['receipt']['receiptId']
    date = a['receipt']['issueDate']
    country = a['receipt']['organization']['country']
    vendor = a['receipt']['organization']['name']
    code = a['receipt']['unit']['cashRegisterCode']

    return json.dumps(price, Id, date, country, vendor, code)
    #print(a.json())

#over("O-3A63E4A211344716A3E4A211345716AC")