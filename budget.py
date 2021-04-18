db = {}


class Category():
    """
    A budget app created to:
    1. Depositing funds to each of the categories
    2. Withdrawing funds from each category
    3. Computing category balances
    4. Transferring balance amounts between categories
    """


    def __init__(self, category):
        self.budget_type = category
        self.category_balance = 0
        # self.db.keys() = self.budget_type
        db[self.budget_type] = self.category_balance
        
    def deposit(self, amount):
        self.category_balance += amount
        db[self.budget_type] += amount
        
    def withdraw(self, amount):
        self.category_balance -= amount
        
    def balance(self):
        return db[self.budget_type]
        
    def transfer(self, amount, receive_category, sending_category):
        
        if db[sending_category] > amount:
            if receive_category in db.keys():
                if receive_category != sending_category:
                    db[receive_category] += amount
                    db[sending_category] -= amount
                else:
                    print("You cant transfer to the same budget")
            else:
                print("Category does not exist")
                
        else:
            print(f"Insuficient fund. Please fund your {sending_category} budget, current balance is {db[sending_category]}")


def init():
    print("*** WELCOME TO MY BUDGET APP ***")
    print("********************************")
    print("Please ensure you follow the Instructions")

    checker = int(input("Enter 0:To Create budget, 1:To Check Budget, 2:To Quit: "))

    def instantiator():
        budget = Category(input("Enter your budget name: "))
        return budget

    def operations():
        validator = int(input(
            "Enter 1:Deposit, 2:Withdraw, 3:Balance, 4:Transfer, 5:To Start Again, 6:Quit: "))
        if validator == 1:
            amount = int(input("Enter amount to deposit: "))
            budget.deposit(amount)
        elif validator == 2:
            amount = int(input("Enter amount to withdraw: "))
            budget.withdraw(amount)
        elif validator == 3:
            print(budget.balance())
        elif validator == 4:
            amount = int(input("Enter amount to transfer: "))
            receive_category = input("Enter category to transfer to: ")
            sending_category = input("Enter category to transfer from: ")
            budget.transfer(amount, receive_category, sending_category)
        elif validator == 5:
            init()
        elif validator == 6:
            exit()
        else:
            print("Invalid value, please try again ")
            init()

    while checker != 2:
        if checker == 0:
            budget = instantiator()
            print("What would you love to do?")
            operations()
        elif checker == 1:
            for keys in db:
                print("***", keys, "***")
            value = input("Do you want the entire balance or a specific budget. YES|NO: ")
            if value.upper() == "YES":
                for keys, values in db.items():
                    print("***", keys, "\t", values, "***")

                operations()
                # print(db)
            elif value.upper() == "NO":
                request = input("Enter budget name: ")
                if request in db.keys():
                    print(request, " ", db[request])
                    operations()
                else:
                    print("Budget do not exist")
                    init()
            else:
                print("Invalid value, please try again ")
                init()
        elif checker == 2:
            exit()
        else:
            print("Invalid value, please try again ")
            init()
        checker = int(input("Enter 0:To Create budget, 1:To Check Budget, 2:To Quit: "))


init()
