class Category:
  #list that keeps track of all the instances created
  #registry = []

  def __init__(self, name):
    self.name = name
    self.ledger = []
    #Category.registry.append(self.name) adds instance to the registry

  def get_balance(self):
    total = 0
    for item in self.ledger:
      total = total + item['amount']
    return total

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def deposit(self, amount, description=''):
    self.newItem = {}
    self.newItem['amount'] = float(amount)
    self.newItem['description'] = description
    self.ledger.append(self.newItem)

  def withdraw(self, amount, description=''):
    if self.check_funds(amount) == True:
      self.newItem = {}
      self.newItem['amount'] = float(-amount)
      self.newItem['description'] = description
      self.ledger.append(self.newItem)
      return True
    else:
      return False

  def get_ledger(self):
    return self.ledger

  def transfer(self, amount, differentCategory):
    if self.withdraw(amount, 'Transfer to ' + differentCategory.name):
      differentCategory.deposit(amount, 'Transfer from ' + self.name)
      return True
    else:
      return False

  def __repr__(self):
    title = self.name.center(30, '*') + '\n'

    items = ''
    for item in self.ledger:
      amount = "{:.2f}".format(item.get('amount'))
      itemLine = item.get('description')[0:23].ljust(23, ' ') + amount.rjust(7, ' ')
      items = items + itemLine + '\n'

    total = 'Total: ' + str(self.get_balance())
    return title + items + total

expensesByCategory = {}
def calculateExpenses(categories):
  for category in categories:
    category.totalExpenses = 0
    for item in category.ledger:
      if item['amount'] < 0:
        category.totalExpenses += item['amount']
        category.totalExpenses = round(category.totalExpenses)
    expensesByCategory[category.name] = category.totalExpenses
  totalExpenses = sum(expensesByCategory.values())
  print(expensesByCategory)
  for k, v in expensesByCategory.items():
    expensesByCategory[k] = round((v / totalExpenses) * 10)
  return expensesByCategory

def create_spend_chart(categories):
  calculateExpenses(categories)
  print(expensesByCategory)

  title = 'Percentage spent by category' + '\n'
  oneHundred = '100|'
  for k, v in expensesByCategory.items():
    if v >= 10:
      char = '  o'
    else:
      char = '   '
    oneHundred += char

  ninety = ' 90|'
  for k, v in expensesByCategory.items():
    if v >= 9:
      char = '  o'
    else:
      char = '   '
    ninety += char

  eighty = ' 80|'
  for k, v in expensesByCategory.items():
    if v >= 8:
      char = '  o'
    else:
      char = '   '
    eighty += char

  seventy = ' 70|'
  for k, v in expensesByCategory.items():
    if v >= 7:
      char = '  o'
    else:
      char = '   '
    seventy += char

  sixty = ' 60|'
  for k, v in expensesByCategory.items():
    if v >= 6:
      char = '  o'
    else:
      char = '   '
    sixty += char

  fifty = ' 50|'
  for k, v in expensesByCategory.items():
    if v >= 5:
      char = '  o'
    else:
      char = '   '
    fifty += char

  fourty = ' 40|'
  for k, v in expensesByCategory.items():
    if v >= 4:
      char = '  o'
    else:
      char = '   '
    fourty += char

  thirty = ' 30|'
  for k, v in expensesByCategory.items():
    if v >= 3:
      char = '  o'
    else:
      char = '   '
    thirty += char

  twenty = ' 20|'
  for k, v in expensesByCategory.items():
    if v >= 2:
      char = '  o'
    else:
      char = '   '
    twenty += char

  ten = ' 10|'
  for k, v in expensesByCategory.items():
    if v >= 1:
      char = '  o'
    else:
      char = '   '
    ten += char

  chart = title + oneHundred + '\n' + ninety + '\n' + eighty + '\n' + seventy + '\n' + sixty + '\n' + fifty + '\n' + fourty + '\n' + thirty + '\n' + twenty + '\n' + ten + '\n'
  print(chart)

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
