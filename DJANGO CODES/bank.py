from itertools import count
# We will be assigning a number as account number. It will be incremental.
 
accounts = {}
 
class Account:
 
    count = count(start=1) # [1,2,3,4,5,6........]
    
    def __init__(self, name, balance, pin):
        ac_n = next(self.count)
        self.ac_n = ac_n
        self.name = name
        self.balance = balance
        self.pin = pin
 
        accounts[ac_n] = self # x get/change => x.property_name 
 
        print(f"Congrats {name}, your account has been opened. Your account number is {ac_n} and your pin is {pin}")
 
    def change_pin(self, old_pin ,new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("Your old pin is invalid")
 
    def __str__(self):
        return f"Account No: {self.ac_n}. Name: {self.name}"
 
    def transfer(self, pin, pathauna_aateko_manxe_ko_naam, reciever_ac_n, amount):
        if pin == self.pin:
            if accounts.get(reciever_ac_n) != None: # {key: value} dct.get(key) => if key exists: value... if key doesn't exist: None
                if self.balance >= amount:
                    reciever = accounts.get(reciever_ac_n)     
                    if reciever.name == pathauna_aateko_manxe_ko_naam:
                        new_sender_balance = self.balance - amount #deduction
                        self.balance = new_sender_balance #storing after deduction
                        new_reciever_balance = reciever.balance + amount #transfer
                        reciever.balance = new_reciever_balance #store after transfer
 
                        print(f"Your transfer has been successful. Your new balance is Rs {self.balance}.")
 
                    else:
                        print("The name and account number didn't match.")    
                else:
                    print("Your balance is insufficient.")
            else:
                print("Sorry the reciever's account doesn't exist.")                                       
        else:
            print("Your pin is incorrect. Please try again.")
 
 
my = Account(name='ABINASH NATH PANDEY', balance=50000000, pin=5674)
your = Account(name='abinash nath pandey', balance=200000000, pin=7564)
 
my.transfer(pin=5674, pathauna_aateko_manxe_ko_naam="ABINASH NATH PANDEY", reciever_ac_n=76568, amount=12000000000)
 
print("My balance= ", my.balance)
print("Your balance= ", your.balance)
 
# check if pin is correct
# check if reciever exists
# check if enough balance
# check if reciever's account number and name match
 
 
# Assignment: Put a validation to check own account and print("You can't transfer to self.")