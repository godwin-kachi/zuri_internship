import datetime
import random
from os import system

clear = lambda: system("cls") #I need to read the full implementation of this function

allowedUsers = {
     "onyekachi": "imagine",
     "mary": "bontel",
     "naomi": "pleasant",
     "dolapo": "sweetheart",
     "martina": "loverbae",
}  #the usernames are passed as the key, while password is the value

openingBalance = {
     "onyekachi": 125000,
     "mary": 23800,
     "naomi": 35000,
     "dolapo": 20500,
     "martina": 83000,
}


def validate():
     global username, pwd
     print("***Please provide your details again***")
     username = input("username: ")
     if username in allowedUsers:
          pwd = input("Password: ")
          if pwd == allowedUsers[username]:
               login()
          else:
               print("You have entered a wrong password.")
               closing()
     else:
          print("Username is not found")
          closing()
     return(username, pwd)

def deposit():
     print("Your current balance is", openingBalance[username], "How much are you depositing?")
     deposit = float(input())
     new_balance = openingBalance[username] + deposit
     print("Successfully posted...")
     print("Your new Balance is", new_balance)

     closing()

def change_password():
     print("Your current password is", pwd.upper())
     new_password = input("New Password")
     allowedUsers[username] = new_password
     print("You have changed your password from", pwd, "to", new_password)

     closing()

def withdraw():
     print("Your current Balance is", openingBalance[username], "How much are you withdrawing?")
     wtd = int(input())
     if wtd > openingBalance[username]:
          print("You can only withdraw", openingBalance[username] - 1000, "... Want to try again ? Y/N")
          dec = input("Want to try again ? Y/N ")
          if "y" or "Y" in dec:
               wtd = int(input())
               new_balance = openingBalance[username] - wtd
               print("Please take your cash")
               print("Your new Balance is", new_balance)
          else:
               print("Please top up your account to withdraw")
     else:
          new_balance = openingBalance[username] - wtd
          print("Please take your cash")
          print("Your new Balance is", new_balance)

     closing()

def closing():
     print("Thank you for using our services")
     confirmation = input("Would you like to do something else? Y/N ")
     if confirmation.upper() == "Y":
          clear()
          validate()
     else:
          print("Do ensure to pay your taxes")

def generateAccountNumber(username):
     return random.randrange(2230000000, 2239999999)

def time_determinant(username):
     login_time = datetime.datetime.now().strftime("%H")
     if (login_time > "4") and (login_time < "12"):
          print("Good morning", username.capitalize())
     elif (login_time > "12") and (login_time < "16"):
          print("Good afternoon", username.capitalize())
     else:
          print("Good evening", username.capitalize())


def login():
     pass_hash = len(pwd)
     hashed = "*" * pass_hash
     login_time = datetime.datetime.now().strftime("%H:%M:%S")
     print("*" * 20)
     print("Welcome here", username.capitalize(), "Your password is", hashed, "and your balance is", openingBalance[username])
     print("Your Account Number is", generateAccountNumber(username))
     print("You logged in today ", datetime.datetime.now().date(), "by", login_time)
     time_determinant(username)
     print("*" * 20)
     print("What would you like to do?")
     print("1. \t Change Password")
     print("2. \t Deposit")
     print("3. \t Withdraw")
     
     try:
          userchoice = int(input())
          if userchoice == 1:
               change_password()
          elif userchoice == 2:
               deposit()
          elif userchoice == 3:
               withdraw()
          else:
               print("You have selected a wrong choice")
               closing()
     except ValueError:
          print("You should select numbers not text")
          login()

print("Welcome to the improved ATM experience")
print("Created by Onyekachi")

validate()