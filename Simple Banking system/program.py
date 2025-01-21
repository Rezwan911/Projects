import random
import time

accounts = []

def load_accounts():
    myfile = open("accounts.txt", 'r')
    for line in myfile:
        name, acc_number, balance, loan, pin = line.strip().split(",")
        accounts.append([name, int(acc_number), float(balance), float(loan), pin])
    myfile.close()

load_accounts()

def save_accounts():
    myfile = open("accounts.txt", 'w')
    for account in accounts:
        myfile.write(f"{account[0]},{account[1]},{account[2]},{account[3]},{account[4]}\n")
    myfile.close()

def add_account():
    name = input("Enter name: ")
    acc_number = random.randint(100000, 999999)
    print("Your account number is", acc_number)
    initial_deposit = float(input("Enter initial deposit: "))
    loan = 0
    pin = input("Set a 4-digit PIN for your account: ")
    accounts.append([name, acc_number, initial_deposit, loan, pin])
    print("Account has been added.")

def login():
    acc_number = int(input("Enter your account number: "))
    pin = input("Enter your 4-digit PIN: ")
    for account in accounts:
        if account[1] == acc_number and account[4] == pin:
            print(f"Login successful! Welcome, {account[0]}.")
            return account
    print("Invalid account number or PIN!")
    return None

def deposit(account):
    amount = float(input("Enter deposit amount: "))
    account[2] += amount
    print("Processing...")
    time.sleep(1)
    print(f"{amount}$ has been added to your account.")

def check_balance(account):
    print("Fetching account details...")
    time.sleep(1)
    print(f"{account[0]} has {account[2]}$ in their account.")

def withdraw(account):
    amount = float(input("Enter withdrawal amount: "))
    print("Checking...")
    time.sleep(1)
    if account[2] < amount:
        print("Insufficient balance!")
    else:
        account[2] -= amount
        print(f"{amount}$ has been withdrawn from your account.")

def loan(account):
    max_loan = account[2] * 2
    print(f"Your maximum loan amount is: {max_loan}")
    loan_amount = float(input("Enter loan amount: "))
    print("Processing loan request...")
    time.sleep(2)
    if loan_amount > max_loan:
        print("Loan amount exceeds the maximum allowed!")
        return
    account[3] += loan_amount
    save_accounts()
    print(f"Loan of {loan_amount}$ granted successfully!")

def repay_loan(account):
    print(f"Your current loan is {account[3]}$.")
    repayment = float(input("Enter the amount you want to repay: "))
    print("Processing...")
    time.sleep(1)
    if repayment <= account[3]:
        account[3] -= repayment
        print(f"{repayment}$ has been repaid.")
    else:
        print("Repayment amount exceeds your loan balance.")

def remove_account(account):
    print("Account found: ", account[0], " with balance ", account[2], "$.")
    confirm = input("Are you sure you want to delete this account? (Y/N): ")
    if confirm.lower() == "y":
        accounts.remove(account)
        save_accounts()
        print("Account removed successfully!")
    else:
        print("Account deletion canceled.")

def balance_sheet():   
    if not accounts:
        print("No accounts available.")
        return
    print("Collecting data.....")
    time.sleep(1)
    print("============================ Balance Sheet ============================")
    print("Name              Account Number         Balance              Loan")
    print("=======================================================================")
    total_balance = 0
    for account in accounts:
        total_balance += account[2]
        print(f"{account[0]}           {account[1]}               {account[2]}$              {account[3]}$")
    print("=======================================================================")
    print(f"Total Balance:                                      {total_balance}$")

def mobilerechage(account):
    phone_number = int(input("Enter Your phone number: "))
    amount = float(input("Enter the amount you want to recharge: "))
    print("Checking Number....")
    time.sleep(2)
    if amount <= account[2]:
        account[2] -= amount
        print(f"{amount}$ has been recharged to {phone_number}.")
    else:
        print("Amount exceeding account limit.")

def bank_bkash(account):
    amount = float(input("Enter the amount you want to send to your Bkash: "))
    print("Checking....")
    time.sleep(2)
    if amount <= account[2]:
        print("Transferring....")
        time.sleep(1)
        account[2] -= amount
        print(f"{amount}$ has been sent to your Bkash.")
    else:
        print("You don't have enough money in your account.")

def banking_menu(account):
    while True:
        print("===================================================")
        print("================= Banking Menu ====================")
        print("===================================================")
        print("1. Deposit")
        print("2. Check Balance")
        print("3. Withdraw Money")
        print("4. Apply for a Loan")
        print("5. Repay Loan")
        print("6. Bank To Bkash")
        print("7. Mobile Recharge")
        print("8. Remove Account")
        print("9. Logout")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit(account)
        elif choice == 2:
            check_balance(account)
        elif choice == 3:
            withdraw(account)
        elif choice == 4:
            loan(account)
        elif choice == 5:
            repay_loan(account)
        elif choice == 6:
            bank_bkash(account)
        elif choice == 7:
            mobilerechage(account)
        elif choice == 8:
            remove_account(account)
            break
        elif choice == 9:
            print("Logging out...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Try again.")

while True:
    print("======================================================")
    print("================ Simple Banking System ===============")
    print("======================================================")
    print("1. Add Account")
    print("2. Login")
    print("3. Balance Sheet (admin)")
    print("4. Save and Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_account()
    elif choice == 2:
        account = login()
        if account !=0:
            banking_menu(account)
    elif choice == 3:
        balance_sheet()
    elif choice == 4:
        save_accounts()
        print("Saving and exiting...")
        time.sleep(1)
        break
    else:
        print("Invalid choice. Try again.")
