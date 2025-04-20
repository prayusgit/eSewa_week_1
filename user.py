from utils import *
import pandas as pd

class User:
    def __init__(self):
        self.user_list = pd.read_csv(USER_LIST)
        self.authenticated = False
        self.username = None
        self.password = None
        self.amount = None

    def login(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        self.user_list = pd.read_csv(USER_LIST)

        if username in self.user_list.username.values:
            saved_password = self.user_list[self.user_list.username == username].password.values[0]
            if saved_password == password:
                print("Welcome " + username)
                self.authenticated = True
                self.amount = self.user_list[self.user_list.username == username].amount.values[0]
            else:
                print("Password is incorrect.")
        else:
            print("No such username.")

    def register(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        amount = int(input("Enter the money amount: "))
        if username in self.user_list.username.values:
            print("Username already exist. Try another")
        else:
            df = pd.DataFrame([[username, password, amount]], columns=['username', 'password', 'amount'])
            print("User registered successfully.\n")
            df.to_csv(USER_LIST, mode='a', index=False, header=False)

    def is_authenticated(self):
        return self.authenticated

    def logout(self, amount):
        self.user_list.loc[self.user_list['username'] == self.username, 'amount'] = amount
        self.user_list.to_csv(USER_LIST ,index=False ,)
        self.authenticated = False








