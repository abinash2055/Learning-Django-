from itertools import count

# We will be assigning a number as account number. It will be incremental.

accounts = {}


class Account:
    count = count(start=1)  # [1,2,3,4,5,6........]

    def __init__(self, name, balance, pin):
        ac_n = next(self.count)
        self.ac_n = ac_n
        self.name = name
        self.balance = balance
        self.pin = pin

        accounts[ac_n] = self  # x get/change => x.property_name

        print(f"Congrats {name}, your account has been opened. Your account number is {ac_n} and your pin is {pin}")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("Your old pin is invalid")

    def __str__(self):
        return f"Account No: {self.ac_n}. Name: {self.name}"

    def transfer(self, pin, pathauna_aateko_manxe_ko_naam, reciever_ac_n, amount):
        if pin == self.pin:
            if accounts.get(reciever_ac_n) != self.ac_n:  # {key: value} dct.get(key) => if key exists: value... if key doesn't exist: None
                if self.balance >= amount:
                    reciever = accounts.get(reciever_ac_n)
                    if reciever.name != self.name:
                        if reciever.name == pathauna_aateko_manxe_ko_naam:
                            new_sender_balance = self.balance - amount  # deduction
                            self.balance = new_sender_balance  # storing after deduction
                            new_reciever_balance = reciever.balance + amount  # transfer
                            reciever.balance = new_reciever_balance  # store after transfer

                            print(f"Your transfer has been successful. Your new balance is Rs {self.balance}.")

                        else:
                            print("You can't transfer to self..")
                    else:
                        print("You can't transfer to your self")
                else:
                    print("Your balance is insufficient.")
            else:
                print("Sorry the reciever's account doesn't exist.")
        else:
            print("Your pin is incorrect. Please try again.")


my = Account(name='Aashish', balance=15000, pin=123)
your = Account(name='Abisam', balance=20000, pin=362)

my.transfer(pin=123, pathauna_aateko_manxe_ko_naam="Ram", reciever_ac_n=2, amount=1200)

print("My balance= ", my.balance)
print("Your balance= ", your.balance)