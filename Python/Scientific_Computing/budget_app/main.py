import math

class Category:
    def __init__(self, category_name):
       self.ledger = []
       self.name = category_name
    
    def __repr__(self):
        header_stars_amount = math.floor((30 - len(self.name)) / 2)
        header = f"{'*' * header_stars_amount}{self.name}{'*' * header_stars_amount}"
        item_list = f""
        for item in self.ledger:
            # format description
            description = ""
            if len(item['description']) >= 23:
                description += item['description'][0:23]
            else:
                description = item['description']
            #format amount
            amount = ""
            if len(format(item['amount'], '.2f')) > 7:
                amount += f"{format(item['amount'], '.2f')}"
            else:
                amount += f"{format(item['amount'], '.2f')[0:7]}"
            # calculate needed space
            space = 30 - len(amount) - len(description)
            
            item_list += f"{description}{space * ' '}{amount}\n" 
        total = f"Total: {format(self.get_balance(), '.2f')}"
        full_str = f"{header}\n{item_list}{total}"
        return full_str
    
    def deposit(self,amount,description=""):
        self.ledger.append( {"amount": float(amount), "description": description} )

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append( {"amount": float(-amount), "description": description} )
            return True
        else:
            return False
            
    def get_balance(self):
        balance = 0
        for dict in self.ledger:
            balance += dict['amount']
            print(balance)
        return balance
        
    def transfer(self,amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget.name)
            budget.deposit(amount, "Transfer from " + self.name)
            return True
        else: 
            return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    
    

def create_spend_chart(categories):

    spent = []
    for category in categories:
        temp_sum = 0
        for dict in category.ledger:
            amount = dict['amount']
            if amount < 0: temp_sum += amount
        spent.append(-temp_sum)

    total = sum(spent)
    percentages = [s * 100 / total for s in spent]
    full_str = ["Percentage spent by category"]
    for i in range(0, 11):
        level = 10 * (10 - i)
        s = '{:>3}| '.format(level)
        for p in percentages:
            if p >= level:
                s += "o  "
            else:
                s += "   "
        full_str.append(s)
    padding = " " * 4
    full_str.append(padding + "-" * 3 * len(spent) + "-")

    names = [category.name for category in categories]
    n = max(map(len, names))
    for i in range(0, n):
        s = padding
        for name in names:
            s += f" {name[i]} " if len(name) > i else "   "
        full_str.append(s + " ")

    full_str = "\n".join(full_str)
    
    return full_str


food = Category('Food')
cars = Category('Cars')
cars.deposit(100)
cars.withdraw(60)

food.deposit(100, "initial deposit")
food.withdraw(40.5, "chicken")
print(food)

business = Category('Business')
business.deposit(200)
business.withdraw(20)
print(create_spend_chart([business, food, cars]))