# Ankush Food Court

---
## Usecase

* The application will have a log-in for admin and users.

### Admin will have the following functionalities:
1.	Add new food items. Food Item will have the following details:
2.	FoodID //It should be generated automatically by the application.
3.	Name
4.	Quantity. For eg, 100ml, 250gm, 4pieces etc
5.	Price
6.	Discount
7.	Stock. Amount left in stock in the restaurant.
8.	Edit food items using FoodID.
9.	View the list of all food items.
10.	Remove a food item from the menu using FoodID.


### The user will have the following functionalities:
1.	Register on the application. Following to be entered for registration:
2.	Full Name
3.	Phone Number
4.	Email
5.	Address
6.	Password
7.	Log in to the application
8.	The user will see 3 options:
9.	Place New Order
10.	Order History
11.	Update Profile
12.	Place New Order: The user can place a new order at the restaurant.
13.	Show list of food. The list item should as follows:
14.	1. Tandoori Chicken (4 pieces) [INR 240]
15.	2. Vegan Burger (1 Piece) [INR 320]
16.	3. Truffle Cake (500gm) [INR 900]
17.	Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]
18.	Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
19.	Order History should show a list of all the previous orders
20.	Update Profile: the user should be able to update their profile.



## Installation

```bash
. ./startup.sh
```

## Usage

* Delete all files inside (app/food-artifacts) and (app/users-artifacts)

* Then run following command to start app

```bash
python app/main.py
```

## Troubleshoot

* If you get no module found app
  * be sure to run 
    ```bash 
    python app/main.py 
    ```
    from the same terminal where you ran 
    ```bash
    . ./startup.sh
    ```
