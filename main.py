class Account():
    def __init__(self,Account_number,owner,balance=0):
        self.Account_number = Account_number
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"The deposit is successfully done.Balance amount is ${self.balance} ")
        else:
            print("Enter a valid amount")

    def withdrawl(self,amount):
        if 0 <amount <= self.balance:
            self.balance -= amount
            print(f"The withdrawl is successfully done.Balance amount is ${self.balance}")

        else:
            print("Insufficient balance or Invalid amount")

    def checkbalance(self):
        print(f"Balance amount : ${self.balance}")

    
def main():
    accounts = {}

    def create_account():

        account_number = int(input("Enter your account number here:"))

        if account_number in accounts:
            print("Account already exists!")

        else:
            owner = input("Enter account owner name here: ")
            accounts[account_number] = Account(account_number,owner)

            print(f"Account successfully created with the owner name of {owner}")

    def access_account():

        account_number = int(input("Enter your account number here:"))

        if account_number in accounts:
            account = accounts[account_number]

            print(f"Welcome {account.owner}")

            while True:

                print("1. Check Balance ")
                print("2. Deposit Money ")
                print("3. Withdrawl ")
                print(" 4. Exit ")

                choice = input("Choose an option:")

                if choice == '1':
                  account.checkbalance()

                elif choice == '2':
                    amount = float(input("Enter the amount to deposit: "))

                    account.deposit(amount)

                elif choice == '3':
                    amount = float(input("Enter the amount to withdrawl: "))

                    account.withdrawl(amount)

                elif choice == '4':
                    print("Logging out...")

                    break

                else:
                    print("Invalid option!!!")

        else:
            print("Account not found!")

    while True:
        print("__Welcome to the Bank__")

        print("1. Create a new account ")
        print("2. Access existing account ")
        print("3. Exit ")

        choice = input("Choose an option:")

        if choice == "1":
            create_account()

        elif choice == "2":
            access_account()

        elif choice == "3":
            print("Thank you for visiting our bank!")

        else:
            print("Invalid option")

            break

if __name__ =="__main__":
  main()

                    





            
        

       

        
    


        