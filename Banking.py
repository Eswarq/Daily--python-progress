class Bank:
    balance = float(0)
    def show_balance(self):
        print(f"your balance is {self.balance :.2f}")
    def Deposit(self):
        amount = float(input("Enter the amount to be deposited : "))
        if amount < 0:
            print("Deposit must be greater than 0 ! ")
            return 0
        else:
            return amount
    def withdraw(self):
        amount = float(input("Enter the withdrawl amount : "))
        if amount > self.balance :
            print("sorry insufficient balance !!")
            return 0
        else :
            print('Current balance: ', self.balance)
            return amount


def Banking():
    myBank = Bank()
    is_run = True
    while is_run:
        print("Welcome to Bank ")
        print("1. show_balance ")
        print("2. To Deposit ")
        print("3. To withdraw ")
        print("4. To exit ")
        
        choose = input("Select a number between (1 to 4 ) : ")

        if choose == '1':
            myBank.show_balance()
        elif choose == '2':
            myBank.balance += myBank.Deposit()
        elif choose == '3':
            myBank.balance -= myBank.withdraw()
        elif choose == '4':
            is_run = False 
        else :
            print("The number is not valid ")

print("Thank you for visting our Bank !")

if __name__ == "__main__":
    Banking()