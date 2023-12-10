# Make restaurant model: (Project outline received from Amjad)
#
# 1) Show the menu of restaurant i.e names of dishes and their prices per unit (i.e per kg or per plate or per piece etc.)
#
# 2) Take user input for  his/her order. Save amount somewhere in code.
#
# 3) provide the billing receipt showing what he/she ordered with total billed amount.
class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: Rs.{self.price:.2f}"

class Order:
    def __init__(self):
        self.menu = {
            "Pizza": 500.00,
            "Burger": 150.00,
            "Pasta": 250.00,
            "Salad": 100.00,
        }

        self.order_items =[]
        self.total_amount = 0.0

    def show_menu(self):
        print("Welcome to the ABC Restaurant!")
        print("***** Menu Items *****")
        for item, price in self.menu.items():
            print(MenuItem(item,price))

    def take_order(self):
        while True:
            item_name = input("Enter the item name to order or type 'x' to finish! ")
            if item_name.lower() == "x":
                break

            if item_name in self.menu:
                quantity = float(input(f"Enter the quantity of {item_name} ! "))
                amount = self.menu[item_name] * quantity
                self.order_items.append((item_name,quantity, amount))
                self.total_amount += amount
            else:
                print("Invalid item. Please enter a valid item from menu!")

    def print_receipt(self):
        print("\nBilling Receipt:")
        for item, quantity, amount in self.order_items:
            print(f"{item} x {quantity}: Rs.{amount:.2f}")
        print(f"Total Amount: Rs.{self.total_amount:.2f}")
        print("Thank you for your order! Enjoy your meal!")

if __name__ == "__main__":
    order = Order()
    order.show_menu()
    order.take_order()
    order.print_receipt()

