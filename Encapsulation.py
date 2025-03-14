class BankAccount:
    def __init__(self,account_number,balence):
        self.account_number = account_number
        #Public 
        # self.balence = balence 
        #Make this Private
        self.__balence = balence

    def depositer(self,ammount):
        self.__balence +=ammount
    def get_balence(self):
        return self.__balence

account =BankAccount('12345',5000)
account.depositer(2000)
print(account.get_balence())    
# 
# 
# class BankAccount:
#     def __init__(self, account_number, balance):  # Fixed spelling of 'balence' -> 'balance'
#         self.account_number = account_number
#         self.__balance = balance  # Private variable

#     def deposit(self, amount):  # Fixed spelling of 'depositer' -> 'deposit'
#         self.__balance += amount  # Corrected indentation

#     def get_balance(self):  # Fixed spelling of 'get_balence' -> 'get_balance'
#         return self.__balance

# # Creating an account
# account = BankAccount('12345', 5000)
# account.deposit(2000)

# # Corrected method call
# print(account.get_balance())  # Output: 7000
       