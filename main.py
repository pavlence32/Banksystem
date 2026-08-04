from bank import Bank


bank = Bank()


def show_menu():
    print("""
 BANK SYSTEM 
1. Создать клиента
2. Открыть счет
3. Пополнить счет
4. Снять деньги
5. Перевести деньги
6. Показать клиентов
7. История операций
0. Выход

""")


while True:
    show_menu()

    choice = input("Выберите действие: ")

    try:

        if choice == "1":
            name = input("Введите имя клиента: ")

            client = bank.create_client(name)

            print(f"Создан клиент: {client}")

        elif choice == "2":
            client_id = int(input("ID клиента: "))

            client = bank.find_client(client_id)

            if client is None:
                print("Клиент не найден")
                continue

            balance = float(input("Начальный баланс: "))

            account = bank.open_account(client, balance)

            print("Счет создан:")
            print(account)

        elif choice == "3":
            client_id = int(input("ID клиента: "))

            client = bank.find_client(client_id)

            if client is None:
                print("Клиент не найден")
                continue

            number = int(input("Номер счета: "))

            account = client.get_account(number)

            if account is None:
                print("Счет не найден")
                continue

            amount = float(input("Сумма пополнения: "))

            account.deposit(amount)

            print("Баланс обновлен")
            print(account)

        elif choice == "4":
            client_id = int(input("ID клиента: "))

            client = bank.find_client(client_id)

            if client is None:
                print("Клиент не найден")
                continue

            number = int(input("Номер счета: "))

            account = client.get_account(number)

            if account is None:
                print("Счет не найден")
                continue

            amount = float(input("Сумма снятия: "))

            account.withdraw(amount)

            print("Операция выполнена")
            print(account)

        elif choice == "5":
            sender_id = int(input("ID отправителя: "))
            sender = bank.find_client(sender_id)

            if sender is None:
                print("Отправитель не найден")
                continue

            receiver_id = int(input("ID получателя: "))
            receiver = bank.find_client(receiver_id)

            if receiver is None:
                print("Получатель не найден")
                continue

            sender_number = int(input("Счет отправителя: "))
            receiver_number = int(input("Счет получателя: "))

            sender_account = sender.get_account(sender_number)
            receiver_account = receiver.get_account(receiver_number)

            if sender_account is None or receiver_account is None:
                print("Счет не найден")
                continue

            amount = float(input("Сумма перевода: "))

            bank.transfer(
                sender_account,
                receiver_account,
                amount
            )

            print("Перевод выполнен")
        elif choice == "6":

            for client in bank.clients:
                print(client)
                client.show_accounts()
                print()
        elif choice == "7":

            for transaction in bank.transactions:
                print(transaction)
                print()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Такого пункта нет")
    except Exception as error:
        print(f"Ошибка: {error}")
