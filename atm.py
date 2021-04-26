import random
from datetime import datetime, date

# name = input("wat is your name? \n")
allowedName = ["ibukunoluwa", "emmanuel", "kehinde"]
allowedPin = [1234, 2456, 7283]

# if (name in allowedUsers):
# password = input("Your password? \n")
# userId = allowedUsers.index(name)

# if (password == allowedPassword[userId]):

#     today = date.today()
#     current_date = today.strftime("%b-%d-%Y")
#     now = datetime.now()

#     current_time = now.strftime("%H:%M:%S")
#     print(current_date, current_time)


class Account:
    # Construct an Account object
    def __init__(self, id, balance=0, annualInterestRate=3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()


def main():
    print("Welcome to the atm!")

    # ATM Processes
    while True:
        print("\n1 - Register \t 2 - Login \t 3 - Cancel")
        action = int(input("\nEnter your action: "))

        if action == 1:
            name = input("\nEnter your name: ")
            id = int(input("\nEnter account pin: "))
            while id < 1000 or id > 9999:
                id = int(input("\nInvalid pin.. Re-enter: "))

        elif action == 3:
            print("Thanks for choosing us as your bank")
            exit()

        elif action == 2:
            name = input("\nEnter your name: ")
            if (name in allowedName):
                # Reading id from user
                id = int(input("\nEnter account pin: "))

                #  Loop till id is valid
                while (id not in allowedPin):
                    id = int(input("\nInvalid Id.. Re-enter: "))
        else:
            print("nInvalid selection. Try again.")
            continue

        # account_number = random.randint(1000000000, 100000000000)

        # print("Your Account number is: ", account_number)

        # Creating accounts
        accounts = []
        for i in range(1000, 9999):
            account = Account(i, 0)
            accounts.append(account)

        account_number = random.randint(1000000000, 100000000000)

        print("Your Account number is: ", account_number)

        # Iterating over account session
        while True:

            # Printing menu
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

            # Reading selection
            selection = int(input("\nEnter your selection: "))

            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break

            # View Balance
            if selection == 1:
                # Printing balance
                print(accountObj.getBalance())
                continue

            # Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw: "))
                ver_withdraw = input(
                    "Is this the correct amount, Yes or No ? " + str(amt) + " ")

                if ver_withdraw == "Yes":
                    print("Verify withdraw")

                else:
                    break

                if amt < accountObj.getBalance():
                    # Calling withdraw method
                    accountObj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " +
                          str(accountObj.getBalance()) + " n")
                else:
                    print("\nYou're balance is less than withdrawl amount: " +
                          str(accountObj.getBalance()) + " n")
                    print("\nPlease make a deposit.")

            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input(
                    "Is this the correct amount, Yes, or No ? " + str(amt) + " ")

                if ver_deposit == "Yes":
                    # Calling deposit method
                    accountObj.deposit(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " +
                          str(accountObj.getBalance()) + " n")
                else:
                    break

            elif selection == 4:
                print("Account number: ", account_number)
                print("Transaction is now complete.")
                print("Transaction number: ", random.randint(10000, 1000000))
                print("Current Interest Rate: ", accountObj.annualInterestRate)
                print("Monthly Interest Rate: ",
                      accountObj.annualInterestRate / 12)
                print("Thanks for choosing us as your bank")
                exit()

            # Any other choice
            else:
                print("nThat's an invalid choice.")


# Main function
main()
