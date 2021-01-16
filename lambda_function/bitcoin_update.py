from mongoengine import *
import requests
from datetime import datetime
import os

MONGODB_URL = os.getenv('MONGODB_URL')

class BitcoinValues(Document):
    date = DateTimeField(default=datetime.utcnow)
    opening = FloatField(default=0)
    closing = FloatField(default=0)
    lowest = FloatField(default=0)
    highest = FloatField(default=0)
    volume = FloatField(default=0)
    quantity = FloatField(default=0)
    amount = FloatField(default=0)
    avg_price = FloatField(default=0)

    def to_json(self):
        return {
            "date" : self.date,
            "opening" : self.opening,
            "closing" : self.closing,
            "lowest" : self.lowest,
            "highest" : self.highest,
            "volume" : self.volume,
            "quantity" : self.quantity,
            "amount" : self.amount,
            "avg_price" : self.avg_price,
        }
    
    meta = {
        "indexes" : ["date"]
    }

def update_bitcoin_value(event, context):
    today = datetime.now()
    r = requests.get(f'https://www.mercadobitcoin.net/api/BTC/day-summary/{today.year}/{today.month}/{today.day - 1}')
    data = r.json()
    doc = BitcoinValues(**data)
    
    connect('bitcoin', host=MONGODB_URL)
    doc.save()