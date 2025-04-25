import math


class ShoppingCart:
    def __init__(self):
        # Initialize the shopping cart with an empty cart, total cost, and total items.
        self.cart = {}
        self.total_cost = 0
        self.total_item = 0

        print("Welcome to our store!")
        choice = input("Window Shopping or Real Shopping: (w/r) ").lower()
        if choice == "w":
            print("Go Ahead")
        elif choice == "r":
            print("Here is your cart!")
            self.add_items()
        else:
            print("Enter correct option!")

    def add_items(self):
        # Add items to the cart. Input includes item name, price, and quantity.
        while True:
            item_details = input(
                "Enter item, price, and quantity (or 'n' to finish): "
            ).lower()
            if item_details == "n":
                break

            try:
                item, price, quantity = item_details.split()
                price = int(price)
                quantity = int(quantity)
            except ValueError:
                print("Invalid input. Please enter item, price, and quantity.")
                continue

            if item in self.cart:
                # Update quantity if item already exists.
                self.cart[item][1] += quantity
            else:
                # Add new item to the cart.
                self.cart[item] = [price, quantity]
                self.total_item += 1

            self.total_cost += price * quantity

        self.finalize_cart()

    def finalize_cart(self):
        # Finalize the cart and proceed to display or make changes.
        choice = input("Is this the final cart? (y/n) ").lower()
        if choice == "y":
            self.display_cart()
            self.make_payment()
        else:
            self.make_changes()

    def make_changes(self):
        # Modify the cart by adding or removing items.
        choice = input("Remove item or Add item: (r/a) ").lower()
        if choice == "r":
            self.remove_items()
        elif choice == "a":
            self.add_new_or_existing_items()
        else:
            print("Enter correct option!")

        self.display_cart()

    def remove_items(self):
        # Remove items or reduce their quantity in the cart.
        no_of_item = int(input("Enter the number of items to remove: "))
        r = input("Remove full item or part of it? (f/p) ").lower()

        for _ in range(no_of_item):
            item_name = input("Enter the item name: ").lower()
            if r == "f":
                if item_name in self.cart:
                    # Remove the item entirely from the cart.
                    self.total_cost -= math.prod(self.cart[item_name])
                    self.cart.pop(item_name)
                    self.total_item -= 1
                else:
                    print("Item Not Found!")
            elif r == "p":
                quantity = int(input("Enter quantity to remove: "))
                if item_name in self.cart:
                    if self.cart[item_name][1] >= quantity:
                        # Reduce the quantity of the item.
                        self.cart[item_name][1] -= quantity
                        self.total_cost -= self.cart[item_name][0] * quantity
                        if self.cart[item_name][1] == 0:
                            self.cart.pop(item_name)
                            self.total_item -= 1
                    else:
                        print("Not enough quantity to remove!")
                else:
                    print("Item Not Found!")

    def add_new_or_existing_items(self):
        # Add new items or increase the quantity of existing items.
        no_of_item = int(input("Enter the number of items to add: "))
        r = input("Add new item or existing item? (n/e) ").lower()

        for _ in range(no_of_item):
            if r == "n":
                # Add a completely new item to the cart.
                item_details = input(
                    "Enter item details (name price quantity): "
                ).lower()
                try:
                    item_name, item_price, item_quantity = item_details.split()
                    item_price = int(item_price)
                    item_quantity = int(item_quantity)
                    self.cart[item_name] = [item_price, item_quantity]
                    self.total_item += 1
                    self.total_cost += item_price * item_quantity
                except ValueError:
                    print("Invalid input. Please enter name, price, and quantity.")
            elif r == "e":
                # Increase the quantity of an existing item.
                item_name, item_quantity = (
                    input("Enter the name of the item and quantity: ").lower().split()
                )
                item_quantity = int(item_quantity)
                if item_name in self.cart:
                    self.cart[item_name][1] += item_quantity
                    self.total_cost += self.cart[item_name][0] * item_quantity
                else:
                    print("Item Not Found!")
            else:
                print("Enter correct option!")

    def display_cart(self):
        # Display the current cart with total items and cost.
        print(f"\nTotal Items = {self.total_item}")
        for item, details in self.cart.items():
            print(f"{item} - Rs {math.prod(details)} (Quantity: {details[1]})")
        print(f"Total Amount = Rs {self.total_cost}")

    def make_payment(self):
        # Calculate and display the final amount with applicable discount.
        discount = 0
        if self.total_cost > 10000:
            discount = 0.20

        final_amount = self.total_cost * (1 - discount)
        print(f"Discount of {discount * 100}% applied.")
        print(f"Final Amount to be paid = Rs {final_amount:.2f}")


s = ShoppingCart()
