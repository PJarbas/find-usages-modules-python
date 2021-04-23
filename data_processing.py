from data_collector import DataCollector


class Preprocessing:
    def __init__(self):
        self.di = DataCollector()

    def to_upper(self):
        data = self.di.collect_data()
        upper = data['data'].upper()
        return upper
