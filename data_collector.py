

class DummyDB:
    def __init__(self):
        self.db_name = "my database"

    def insert_data(self, data):
        return f"Successful {data} inserted"

    def get_data(self):
        return {"data": "data to be processed"}


class DataCollector:
    def __init__(self):
        self.db = DummyDB()

    def collect_data(self):
        data = self.db.get_data()
        return data
