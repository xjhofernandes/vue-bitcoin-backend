from model.BitcoinValues import BitcoinValues
from repository.MongoDbAcess import MongoDbAcess
from mongoengine import Q
from datetime import date

class BitcoinService(object):
    def __init__(self) -> None:
        MongoDbAcess()

    def filter_date_interval(self, start, end):
        return BitcoinValues.objects.filter((Q(date__gte=start) & Q(date__lte=end)))   

    def period_filter(self, period_start):
        start = date.today() - period_start.value
        end = date.today()
        results = self.filter_date_interval(start, end)
        return results.to_json()        

    def calendar_filter(self, start, end):
        results = self.filter_date_interval(start, end)

        return results.to_json()      