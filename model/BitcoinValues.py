from mongoengine import *
import datetime

class BitcoinValues(Document):
    date = DateTimeField(default=datetime.datetime.utcnow)
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
            