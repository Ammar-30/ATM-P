import random

balance = random.randint(0,10000000)

pin = "7890"

flag = False
chance = 3 
while chance > 0:
    pswrd = input ("Enter the pin ")
    if pswrd == pin:
        print("PIN accepted")
        flag = True
        break
    else:
        chance -= 1
        print ("Pin is incorrect, you have", chance, "chances left")
        if chance == 0:
            print ("Your card has been retained. Contact the Bank")

def show_menu():
    print ("Choose the options below: ")
    print ("1. Show balnce")
    print ("2. Withdraw money")
    print ("3. Deposit money")
    print ("4. Quit")
    option = int(input())
    return option

while flag:
    user_option = show_menu()
    if user_option == 1:
        print (balance) 
    
    elif user_option == 2:
        withdrawl = int(input("How much money you would like to withdraw "))
        if withdrawl > balance:
            print ("You dont have enough money in your account")
        else:
            balance = balance - withdrawl
            print ("Withdrawl successful") 
   
    elif user_option == 3:
        deposit = int(input("How much money you want to deposit?" ))
        if deposit < 0:
            print ("You cannot enter negative number as an amount")
        else:
            balance = balance + deposit
            print ("Deposit successful")
    elif user_option == 4:
        print ("Thanks for using ATM machine. Goodbye! ")    
        break
    
    else:
        print("Invalid option")
    
