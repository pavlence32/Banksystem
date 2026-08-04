class Client:
    client_id = 1000

    def __init__(self, name):
        self.client_id = Client.client_id
        Client.client_id += 1
        self.name = name
        self.accounts = list()

    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        for p in self.accounts:
            print(f"Счет №{p.number}\nБаланс: {p.balance}")

    def get_account(self, number):
        for user in self.accounts:
            if user.number == number:
                return user
        return None

    def __str__(self):
        return f"Клиент №{self.client_id}: {self.name}"
