import pandas as pd
import random
import datetime as dt
import utils

class Transaction:
    def __init__(self, username, category, product_name ,amount):
        self.username = username
        self.category = category
        self.amount = amount
        self.product_name = product_name

    def record(self):
        time = dt.datetime.now()
        id = random.randint(1, 100000)
        df = pd.DataFrame([[id, time, self.username,  self.category, self.product_name , self.amount]], columns=['id', 'time', 'username' ,'category', 'product_name', 'amount'])
        df.to_csv(utils.FILE_TRANSACTION_RECORD, mode='a', index=False, header=False)
