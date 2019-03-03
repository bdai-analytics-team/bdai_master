import MongoDBUploader

class Account():
    def __init__(self, account_name):
        self.name = account_name
        self.stocks = {}

