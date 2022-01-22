class Food:
  def __init__(self):
    self.food_items = dict()
  
  def add_food(self):
    food = dict()
    food['id'] = 1 if len(self.food_items.keys()) == 0 else max(self.food_items)+1
    print('Enter Food Details')
    food['name'] = input('Name: ')
    food['quantity'] = input('Quantity: ')
    food['price'] = input('Price: ')
    food['discount'] = input('Discount: ')
    food['stock'] = input('Stock: ')
    self.food_items.update({food['id']:food})
    print(f'Food Item added with id: {food["id"]}')

  def list_food_items(self):
    for food in self.food_items.values():
      print(food)
  
  def edit_food_item(self):
    id = int(input('Enter food id: '))
    if id not in list(self.food_items.keys()):
      raise Exception('Food item not found for given id')
    food = self.food_items[id]
    print('Enter Updated Food Details')
    food['name'] = input('Name: ')
    food['quantity'] = input('Quantity: ')
    food['price'] = input('Price: ')
    food['discount'] = input('Discount: ')
    food['stock'] = input('Stock: ')
    self.food_items.update({id:food})
    print('Food Item updated')
  
  def delete_food_item(self):
    id = int(input('Enter food id: '))
    if id not in list(self.food_items.keys()):
      raise Exception('Food item not found for given id')
    del self.food_items[id]
    print('Food Item deleted')