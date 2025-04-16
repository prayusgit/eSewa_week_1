from utils import *
import pandas as pd
from tabulate import tabulate


class Tracker:
    def __init__(self, budget):
        self.budget = budget

        df = pd.read_csv(FILE_CATEGORIES)
        self.categories = df.category.to_list()

    def show_budget(self):
        print(f'The budget available is {self.budget}\n')

    def view_transactions(self):
        df = pd.read_csv(FILE_TRANSACTION_RECORD)

        print('Categories:')
        for index, category in enumerate(self.categories):
            print(f'{index + 1}. {category}')

        category = self.categories[int(input('Choose category: ')) - 1]
        print(tabulate(df[df.category == category], headers='keys', tablefmt='pretty'))

    def buy_item(self):

        print('Categories:')
        for index, category in enumerate(self.categories):
            print(f'{index+1}. {category}')

        category = self.categories[int(input('Choose category: ')) - 1]
        product_name = input("Enter product name: ")
        amount = int(input('Amount: '))
        print('')
        if amount > self.budget:
            print('You don\'t have enough budget')
        else:
            self.budget -= amount

            # Creating and Saving transaction
            transaction = Transaction(category, product_name, amount)
            transaction.record()

    def add_amount(self):
        amount = int(input("Enter amount: "))
        print('')
        self.budget += amount

    def simulate(self):
        while True:
            try:
                print('\nAction available: \
                        \n1. Budget Available \
                        \n2. View Transactions of a category \
                        \n3. Buy item \
                        \n4. Add amount')

                option = int(input('Choose option: '))

                match option:
                    case 1:
                        self.show_budget()
                    case 2:
                        self.view_transactions()
                    case 3:
                        self.buy_item()
                    case 4:
                        self.add_amount()

            except:
                print("Invalid Input. Enter the correctly.\n")