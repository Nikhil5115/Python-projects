fl= open ("Nik.txt","a+")

userName = []
passWord = []
Balance = []
data = []


def input1():

    startScreen = input(" If New user please enter '1' And If already have Account Please Enter '2' : ")

    if startScreen == str(1):
        newUser()
    elif startScreen == str(2):
        main()
    elif((startScreen>='a' and startScreen<= 'z') or (startScreen>='A' and startScreen<='Z')):
        print("Please enter Valid Input")
        input1()
    else:
        print("Please enter Valid Input")
        input1()

def newUser():

    # to Enter New User Details in file

    userName = input("Enter Username :")
    passWord = input("Enter Password :")
    amount = float(input("Enter the amount you want to deposit: "))
    print("Hello, " + userName + "\n Thank you for Creating Account! currently you have " + str(
        amount) + " in your account ")
    fl.write(userName + " " + passWord + " " + str(amount) + "\n")
    input1()
    fl.close()

def main():
    # Read the file and stores the data in respective list
    with open("Nik.txt", 'r') as f:
        for line in f:
            words = line.split(" ")
            names = words[0].split(" ")
            userName.append(names[0])
            passwords = words[1].split(" ")
            passWord.append(passwords[0])
            balance = words[2].split(" ")
            Balance.append(balance[0])

def auth():

    # Authantication of Username and Password and showing Balance of That User

    global userName1,passWord1,availableBalance

    userName1 = input("Enter your user name : ")
    passWord1 = input("Enter your password : ")
    counter = 0


    for i in range(len(userName)):

        if userName1 == userName[i] and passWord1 == passWord[i]:

            availableBalance = 0.0
            availableBalance = float(Balance[i])

            global g
            g=i
            print("Your current Balance is ", availableBalance)
            counter += 1
            showbalance(availableBalance)
            options(userName1)

    if counter == 0:
        print("In Valid Username or Password, Please try again")
        auth()

def showbalance(a):
    print(a)

def depositCash(amount):
    print(amount)

def withDraw(amount):
    print(amount)

def updt(userName1, showBalance):

    # To Update the data in file

    global data

    words = []
    with open('Nik.txt', 'r') as file:
        data = file.readlines()

    for i in range(len(data)):
        words = data[i].split(" ")
        if words[0] == userName1:
            data[i] = words[0] + " " + words[1] + " " + str(showBalance) + "\n"

    with open('Nik.txt', 'w') as file:
        file.writelines(data)

    option1(showBalance)

def options(userName1):
    global availableBalance
    print("Type D to deposit money\n"
          "Type W to withdraw money \n"
          "Type B to display Balance\n"
          "Type C to change user, display user name\n"
          "Type E to exit\n")
    Option = input("Enter your option from above Menu : ")

    global showBalance

    while Option == "E":
        exit()

    while Option == "D":
        amount = float(input("Enter the amount you want to deposit : "))
        showBalance = availableBalance + amount

        print(showBalance)
        updt(userName1, showBalance)
        depositCash(amount)
        showbalance(showBalance)
        option1(showBalance)

    while Option == "W":
        amount = float(input("Enter the amount you want to withdraw : "))
        if availableBalance >= amount:
            showBalance = availableBalance - amount
            print(showBalance)
            updt(userName1, showBalance)
        else:
            print("Transaction Declined due to Insufficient Balance ")
        withDraw(amount)
        showbalance(availableBalance)
        updt(userName1, showBalance)
        option1(showBalance)

    while Option == "B":
        print(availableBalance)
        # updt(showBalance)
        options(userName1)

    while Option == "C":
        input1()

def option1(showBalance):
    print("Type D to deposit money\n"
          "Type W to withdraw money \n"
          "Type B to display Balance\n"
          "Type C to change user, display user name\n"
          "Type E to exit\n")
    Option = input("Enter your option from above Menu : ")


    while Option == "E":
        exit()

    while Option == "D":
        print("Hello")
        amount = float(input("Enter the amount you want to deposit : "))
        showBalance = showBalance + amount

        print(showBalance)
        updt(userName1, showBalance)
        depositCash(amount)
        showbalance(showBalance)
        options()

    while Option == "W":
        print("Hello")
        amount = float(input("Enter the amount you want to withdraw : "))
        if showBalance >= amount:
            showBalance = showBalance - amount
            print(showBalance)
            updt(userName1, showBalance)
        else:
            print("Transaction Declined due to Insufficient Balance ")
        withDraw(amount)
        showbalance(showBalance)
        updt(userName1, showBalance)
        option1(showBalance)

    while Option == "B":
        print(showBalance)
        # updt(showBalance)
        option1(showBalance)

    while Option == "C":
        input1()


input1()
main()
auth()