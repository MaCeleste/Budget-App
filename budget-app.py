class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

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

  def deposit(self, amount, description=' '):
    self.newItem = {}
    self.newItem['amount'] = amount
    self.newItem['description'] = description
    self.ledger.append(self.newItem)

  def withdraw(self, amount, description=' '):
    if self.check_funds(amount) == True:
      self.newItem = {}
      self.newItem['amount'] = -amount
      self.newItem['description'] = description
      self.ledger.append(self.newItem)
      return True
    else:
      return False

  def get_ledger(self):
    return self.ledger

  def transfer(self, differentCategory, amount):
    if self.withdraw(amount, 'Transfer to ' + differentCategory.name):
      differentCategory.deposit(amount, 'Transfer from ' + differentCategory.name)
      return True
    else:
      return False

food = Category('food')
food.deposit(5, 'initial deposit')
food.withdraw(3, 'cake')
print(food.get_ledger())
print(food.get_balance())
beauty = Category('beauty')
beauty.deposit(15, 'initial deposit')
print(beauty.transfer(food, 3))
print(beauty.get_ledger())
print(food.get_ledger())
