from datetime import datetime
import random
database = {}
#name = input("What is your name? \n ")
# allowedUsers = ['Alison','Logan','Ivi']
# allowedPasword = ['Red', 'Apple','Rush']
balance = [1000, 500, 50000]
selectedOption = 1

def init():
    print("Welcome to bankPHP")

    haveAccount = int (input("Do you have account with us?: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        account()
    elif(haveAccount == 2):
        print(register())
    else:
        print("You have selected invalid option")
        init()

################
def account():
    print(" **** Member Login ***")
    name = input("What is your name? \n ")
    allowedUsers = ['Alison','Logan','Ivi']
    allowedPasword = ['Red', 'Apple','Rush']
    if(name in allowedUsers):
        password =input("Your password? \n")
        userId = allowedUsers.index(name)

        if(password == allowedPasword[userId]):
            print('Welcome %s' %name)
            print("Current time: %d", datetime.date(datetime.now()))
            print("Current time: %d", datetime.time(datetime.now()))
            # print('These are the available options:')
            # print('1. Withdrawal')
            # print('2. Cash Deposit')
            # print('3. Complaint')
            BankOptions()
        else:
            print('Password incorrect, please try again')
    else:
        print('Name not found,please try again')

################
def register():
    print(" **** Register ***")
    email = input("What is your email? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password? \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created")
    print("== === == === == ===")
    print("Your account number is: %s" % accountNumber)
    print("Make sure you keep it safe")
    print("== === == === == ===")
   
    loginAccount()


################
def loginAccount():
    print("***** Login *****")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginSuccessful = True

        print("Invalid account or password")
        BankOptions()


##############
def BankOptions():
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')

    selectedOption = int(input('Please select an option:'))

    if(selectedOption == 1):
        print('You selected %s' %selectedOption)
        withdraw = input("How much do you want to withdraw?")
        print("Take your cash")
            
        restart = input("Do you want to return to main menu?")
        if (restart == "yes"):
            BankOptions()
        else:
            loginout()
        

    elif(selectedOption == 2):
        print('You selected %s' %selectedOption)
        #BankOptions()
        depositAmount = int(input("How much would you like to deposit?"))
        currentBalance = balance[allowedUsers.index(name)]
        newBalance = int(currectBalance + depositAmount)
        print("New balance: $ %d " %newBalance)

        restart = input("Do you want to return to main menu?")
        if (restart == "yes"):
            BankOptions()
        else:
            loginout()

    elif(selectedOption == 3):
        print('You selected %s' %selectedOption)
        #BankOptions()
        report = input("What issue will you like to report?")
        print("Thank you for contacting us")

        restart = input("Do you want to return to main menu?")
        if (restart == "yes"):
            BankOptions()
        else:
            loginout()

    else:
        print('Invalid option selected, please try again')
        BankOptions()
        
################
def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

    
################
def loginout():
    print("Thank you! Come again!")

init()