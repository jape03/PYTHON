class Restaurant:
    def __init__(self, menu, book, orders):
        self.resto_menu_items = menu
        self.resto_book_table = book
        self.resto_customer_orders = orders

    def add_item_to_menu(self, item):
        self.resto_menu_items.append(item.lower())
        print(f"Added {item} to the menu.")

    def book_tables(self, number_of_tables):
        self.resto_book_table += number_of_tables
        print(f"Booked {number_of_tables} tables.")

    def customer_order(self, order):
        order_lower = order.lower()
        if order_lower in self.resto_menu_items:
            self.resto_customer_orders.append(order_lower)
            print(f"Order added: {order}")
        else:
            print(f"{order} is not on the menu. Please order only from available menu items.")

restaurant = Restaurant([], 0, [])

while True:
    print("\n")
    print("What would you like to do?")
    print("1. Add menu item")
    print("2. Book tables")
    print("3. Add order")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    print("\n")

    if choice == "1":
        item = input("Enter the menu item to add: ")
        restaurant.add_item_to_menu(item)
    elif choice == "2":
        number_of_tables = int(input("How many tables to book?: "))
        restaurant.book_tables(number_of_tables)
    elif choice == "3":
        print("Available menu items:", ", ".join(restaurant.resto_menu_items))
        order = input("Enter the order: ")
        restaurant.customer_order(order)
    elif choice == "4":
        break
    else:
        print("Invalid option")

print("Menu Items:", ", ".join(restaurant.resto_menu_items))
print("Tables Booked:", restaurant.resto_book_table)
print("Customer Orders:", ", ".join(restaurant.resto_customer_orders))
