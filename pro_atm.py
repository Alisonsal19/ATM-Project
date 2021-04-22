import random
import validation
import database
from getpass import getpass

# database = {
#     4318246141: ["alison", "sal", "ansfanf", "re", 200]
# }

user_auth = "data/auth_session/"


def init():
    print("Welcome to the BANK")
    have_account = int(input("Do you have an account?: 1 (yes) 2 (no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("Invalid option")
        init()


def login():
    print(" **** LOGIN  **** ")

    user_account_number = input("What is your account number? \n")

    is_valid_accnum = validation.account_number_validation(user_account_number)

    if is_valid_accnum:

        # password = input("What is your password? \n")
        password = getpass("What is your password? \n")

        user = database.auth_user(user_account_number, password)
        if user:
            bank_operations(user)

        # for account_number, user_details in database.items():
        #     if account_number == int(user_account_number):
        #         if user_details[3] == password:
        #             bank_operations(user_details)

        print("Invalid account or password")
        login()

        try:
            f = open(user_auth + str(user_account_number) + ".txt", "x")

        except FileExistsError:
            file_contain_data = database.read(user_auth + str(user_account_number) + ".txt")
            if not file_contain_data:
                database.delete(user_account_number)

        finally:
            f.close()


    else:
        print("Account Number Invalid: check if there's 10 digits")
        init()


def register():
    print(" **** REGISTER ***")

    email = input("What is your email? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("reate a password? \n")

    # try:
    #     account_number = generation_account_number()
    #
    # except ValueError:
    #     print("Account failed, try again")
    #     init()

    account_number = generation_account_number()

    # database[account_number] = [first_name, last_name, email, password, 0]
    user_created = database.create(account_number, first_name, last_name, email, password)

    if user_created:
        print("Your account has been created")
        print("== === == === == ===")
        print("Your account number is: %s" % account_number)
        print("Make sure you keep it safe")
        print("== === == === == ===")
        login()
    else:
        print("Please try again")
        register()


def bank_operations(user):
    print("Welcome % s %s" % (user[0], user[1]))
    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_operation()
    elif selected_option == 3:
        login()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected")
        bank_operations(user)


def withdrawal_operation(user_details, balance):
    print("********* WITHDRAWAL **********")
    # get current balance
    # get amount to withdraw
    # check if the current balance > withdraw balance
    # deduct withdraw amount form current balance
    # display current balance

    balance = user_details[4]
    print("Current amount: $" + balance + "\n")

    withdraw = input("How much do you want to withdraw?")
    print("Take your cash \n")
    amount_remaining = int(balance - withdraw)
    print("Current amount after withdraw: $" + amount_remaining)
    restart = input("Do you want to return to main menu?")
    if restart == "yes":
        bank_operations()
    else:
        logout()


def deposit_operation(user_details, balance):
    print("******** DEPOSIT ********")

    # get current balance
    # get account to deposit
    # add deposited amount to current balance
    # display current balance
    balance = user_details[4]
    deposit_amount = int(input("How much would you like to deposit?"))
    new_balance = int(balance + deposit_amount)
    print("New balance: $ %d " % new_balance)

    restart = input("Do you want to return to main menu?")
    if restart == "yes":
        bank_operations()
    else:
        logout()


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    print("Thank you! Come again!")


init()
