from app.users import User

if __name__ == "__main__" :
    print("Welcome to Ankush Food Court!")
    def _login_or_register():
      return int(input("Input 1 for register or 2 for login:\n"))
    login_or_register = _login_or_register()
    while login_or_register not in [1,2]:
      print("Entered value is Invalid")
      login_or_register = _login_or_register()
    
    user = User(login_or_register)
    user.run()

      