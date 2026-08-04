from client import Client
from account import Account
from transaction import Transaction


class Bank:
    def __init__(self):
        self.clients = []
        self.transaction = []

    def create_client(self, name):
        client = Client(name)
        self.clients.append(client)
        return client

    def find_client(self, id):
        for p in self.clients:
            if id == p.client_id:
                return p
        return None

    def open_account(self, client, balance):
        account = Account(client, balance)
        client.add_account(account)
        return account

    def transfer(self, from_account, to_account, amount):
        from_account.transfer(to_account, amount)
        transact = Transaction(from_account, to_account, amount)
        self.transaction.append(transact)
