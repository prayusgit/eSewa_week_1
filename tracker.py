import utils
import pandas as pd
from tabulate import tabulate
from user import User
from transaction import Transaction


class Tracker:
    def __init__(self):
        df = pd.read_csv(utils.FILE_CATEGORIES)
        self.categories = df.category.to_list()
        self.budget = None
        self.user = None

    def show_budget(self):
        print(f'The budget available is {self.budget}\n')

    def view_transactions(self):
        df = pd.read_csv(utils.FILE_TRANSACTION_RECORD)

        print('Categories:')
        for index, category in enumerate(self.categories):
            print(f'{index + 1}. {category}')

        category = self.categories[int(input('Choose category: ')) - 1]
        print(tabulate(df[(df.category == category) & (df.username == self.user.username)], headers='keys', tablefmt='pretty'))

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
            transaction = Transaction(self.user.username, category, product_name, amount)
            transaction.record()

    def add_amount(self):
        amount = int(input("Enter amount: "))
        print('')
        self.budget += amount

    def simulate(self):
        self.user = User()
        while True:
            try:
                if not self.user.is_authenticated():
                    print('\n1. Register \
                           \n2. Login\n')

                    user_input = input("Choose option: ")

                    match int(user_input):
                        case 1:
                            self.user.register()
                        case 2:
                            self.user.login()
                            self.budget = self.user.amount
                else:
                    print('\nAction available: \
                            \n1. Budget Available \
                            \n2. View Transactions of a category \
                            \n3. Buy item \
                            \n4. Add amount \
                            \n5. Logout')

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
                        case 5:
                            self.user.logout(self.budget)
            except:
                print("Invalid Input. Enter correctly.\n")