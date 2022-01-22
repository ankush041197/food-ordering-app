import os
import pickle_secure as pickle
from cryptography.fernet import InvalidToken

from app.food import Food

class User:
  def __init__(self,is_login):
    self.is_login = is_login
    self.is_admin = 0
    self.email = None
    self.password = None
    self.user = None
    self.food_password = '123'
    self.order_history = []


  def _encrypt_and_save_user_data(self,obj,email):
    with open(os.path.join('app/users-artifacts',f'{email}.pkl'), 'wb') as f:
     pickle.dump(obj, f,key=self.password)    
  
  
  def _decrypt_and_restore_user_data(self):
    with open(os.path.join('app/users-artifacts',f'{self.email}.pkl'), 'rb') as inp:
      try:
        self.user = pickle.load(inp,key=self.password)
      except InvalidToken:
        raise Exception('Password is incorrect')
  

  def _encrypt_and_save_food_data(self,obj):
    with open(os.path.join('app/food-artifacts',f'food.pkl'), 'wb') as f:
     pickle.dump(obj, f,key=self.food_password)    
  
  
  def _decrypt_and_restore_food_data(self):
    with open(os.path.join('app/food-artifacts',f'food.pkl'), 'rb') as inp:
      try:
        return pickle.load(inp,key=self.food_password)
      except InvalidToken:
        raise Exception('Password is incorrect')


  def _check_if_admin(self):
    users = os.listdir('app/users-artifacts')
    return 1 if len(users) == 0 else 0
  
  
  def _validate_if_user_already_exist(self):
    users = os.listdir('app/users-artifacts')
    return 1 if f'{self.email}.pkl' in users else 0
  
  
  def _register(self):
    print("Enter your personal details:")
    self.full_name = input('Full Name: ')
    self.ph_number = input('Phone Number: ')
    self.email = input('Email: ')
    self.address = input('Address: ')
    self.password = input('Password: ')
    self.is_admin = self._check_if_admin()
    user_already_exist_status =  self._validate_if_user_already_exist()
    if user_already_exist_status:
      raise Exception("user with same email already exist")
    self._encrypt_and_save_user_data(obj=self,email=self.email)
    self._decrypt_and_restore_user_data()
    print(f'Welcome {self.user.full_name}')
  
  
  def _login(self):
    print("Enter your login details:")
    self.email = input('Email: ')
    self.password = input('Password: ')
    user_already_exist_status =  self._validate_if_user_already_exist()
    if not user_already_exist_status:
      raise Exception(f"user with {self.email} does not exist, try registering new user")
    self._decrypt_and_restore_user_data()
    print(f'Welcome {self.user.full_name}')


  def _place_order(self,food):
    food_ids = []
    for _food in food.food_items.values():
      food_ids.append(_food["id"])
      print(f'{_food["id"]}. {_food["name"]} ({_food["quantity"]}) [{_food["price"]}] @ discount {_food["discount"]}, left in stock {_food["stock"]}')    
    ordered_list = list()
    def _input_food_ids():
        return int(input("""Input items number one by one, enter -1 when no more to order\n"""))  
    while True:
      _option = _input_food_ids()
      if _option == -1:
        break
      while _option not in food_ids:
        print("Entered value is Invalid")
        _option = _input_food_ids()
      print(ordered_list,_option)
      ordered_list.append(_option)
    for _food in food.food_items.values():
      print(ordered_list,_food)
      if _food["id"] in ordered_list:
        self.user.order_history.append(f'{_food["id"]}. {_food["name"]} ({_food["quantity"]}) [{_food["price"]}] @ discount {_food["discount"]}, left in stock {_food["stock"]}')
    self._encrypt_and_save_user_data(obj=self.user,email=self.email)
    print("Ordered placed succussfully")


  def _user_order_history(self):
    for order in self.user.order_history:
      print(order)  


  def _update_user_data(self):
    print("Enter your personal details:")
    self.user.full_name = input('Full Name: ')
    self.user.ph_number = input('Phone Number: ')
    self.user.address = input('Address: ')
    self.user.password = input('Password: ')
    self.password = self.user.password
    self._encrypt_and_save_user_data(obj=self.user,email=self.email)


  def _logout(self):
    print('Thanks for Visiting us, please come again')
  
  
  def _show_user_dashboard(self):
    if self.user.is_admin == 1:
      if len(os.listdir('app/food-artifacts')) == 0:
        food = Food()
      else:        
        food = self._decrypt_and_restore_food_data()
      def _check_dashboard_option():
        return int(input("""Input from the below option\n
                                  1 for Add Food Item or\n 
                                  2 for Edit Food Item or\n
                                  3 for List all Food Item or\n
                                  4 for Delete a Food Item or\n
                                  5 for Logout : \n"""))
      while True:
        dashboard_option = _check_dashboard_option()
        while dashboard_option not in  [1,2,3,4,5]:
          print("Entered value is Invalid")
          dashboard_option = _check_dashboard_option()
        
        if dashboard_option == 1:
          food.add_food()
          self._encrypt_and_save_food_data(food)
        elif dashboard_option == 2:
          food.edit_food_item()
          self._encrypt_and_save_food_data(food)
        elif dashboard_option == 3:
          food.list_food_items()
        elif dashboard_option == 4:
          food.delete_food_item()
          self._encrypt_and_save_food_data(food)
        else:
          self._logout() 
          break 
    else:
      if len(os.listdir('app/food-artifacts')) == 0:
        raise Exception("NO FOOD ITEM IN STOCK")
      else:        
        food = self._decrypt_and_restore_food_data()
      def _check_dashboard_option():
        return int(input("""Input from the below option\n
                                  1 for Place Order or\n 
                                  2 for Show Order History or\n
                                  3 for Update Profile or\n
                                  4 for Logout : \n"""))
      while True:
        dashboard_option = _check_dashboard_option()
        while dashboard_option not in  [1,2,3,4]:
          print("Entered value is Invalid")
          dashboard_option = _check_dashboard_option()
        if dashboard_option == 1:
          self._place_order(food)
        elif dashboard_option == 2:
          self._user_order_history()
        elif dashboard_option == 3:
          self._update_user_data()
        else:
          self._logout()
          break
      

  def run(self):
    if self.is_login == 1: # register request
      self._register()
    else:
      self._login()
    self._show_user_dashboard()



  