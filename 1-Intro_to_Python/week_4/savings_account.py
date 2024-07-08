"""Write a class named SavingsAccount, which allows an owner of an account to make deposits and withdrawals. 
These accounts also compute interest periodically (use an interest rate of 0.02). 
The account should allow the user to enter his/her name, PIN, and balance as attributes when an account is created, and it should return an account number for the user to use. 
The class should include the following functions: (createAccount, verifyInfo, getBalance, getName, getPin, deposit, withdraw, computeInterest).
When an account is created, the balance should be zero by default. When the account user wants to  access the account for withdrawal, deposit or computInterest, 
the program should check the user’s information against the information in the account created.

Use import statements to create the object and call each function."""

class SavingsAccount:

    def createAccount(self):
        self.name = input("Enter your name: ")
        self.__pin = int(input("Create your PIN: "))
        self.balance = float(input("Enter your balance: "))

        return self.name, self.__pin, self.balance

    def verifyInfo(self):
        __entered_pin = int(input("Please enter your pin: "))

        if __entered_pin == self.__pin:
            user_option = input("What would you like to do now?\nPlease enter getBalance, getName, getPin, deposit, withdraw, computeInterest, or quit (case sensitive). ")

            if user_option not in ['getBalance', 'getName', 'getPin', 'deposit', 'withdraw', 'computeInterest']:
                print("You did not enter the correct option, please try again.")
                self.verifyInfo()
            else:
                # the reason I asked for the user to enter case sensitive value is because it will use that value to run the function
                getattr(self, user_option)()
        else:
            print("You did not enter the correct pin.")
            self.verifyInfo()

    def getBalance(self):
        print(f"The balance is: ${self.balance:.2f}")
        self.verifyInfo()

    def getName(self):
        print(str(self.name))
        self.verifyInfo()

    def getPin(self):
        print(int(self.__pin))
        self.verifyInfo()
    
    def deposit(self):
        deposit_amount = float(input("Enter the amount you would like to deposit: $"))
        self.balance += deposit_amount

        print(f"You've deposited {deposit_amount}, your new balance is: ${self.balance:.2f}")
        self.verifyInfo()
    
    def withdraw(self):
        withdrawal_amount = float(input("Enter the amount you would like to withdraw: $"))
        self.balance -= withdrawal_amount

        print(f"You withdrew {withdrawal_amount}, your new balance is: ${self.balance:.2f}")
        self.verifyInfo()
    
    def computeInterest(self):
        interest = self.balance * 0.02
        float(interest)
        print(f"Your interest is ${interest:.2f}")
        self.verifyInfo()

    def quit(self):
        print("Good bye.")

        return


if __name__ == "__main__":
    savings_account = SavingsAccount()
    savings_account.createAccount()
    savings_account.verifyInfo()