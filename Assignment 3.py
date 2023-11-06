items = {}
total = 0
coupons = 0
orders = {}

def add_item():
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = float(input("Enter the item quantity: "))
    item_total = item_price * item_quantity
    items[item_name] = {'price': item_price, 'quantity': item_quantity, 'total': item_total}
    print(item_quantity ,item_name, "added to your order.")
    global total
    total += item_total


def check_total():
    print("The total of your bill is: $",total)


def add_coupon():
    global coupons
    coupon_value = float(input("Enter the coupon value: "))
    coupons += coupon_value
    print("Coupon of $",coupon_value,"applied to the bill.")


def print_order():
    print("Items bought:")
    for item, details in items.items():
        print(f"{item}: {details['quantity']} x ${details['price']:.2f} each")
    print("Total of the order: $",total)
    print("Total of coupons: $",coupons)
    print(f"Total to pay: $",total - coupons)


while True:
    print("1. Start a new order")
    print("2. Close the program")
    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("1. Add a new item")
            print("2. Check the total of the bill")
            print("3. Add a coupon")
            print("4. Checkout")
            option = input("Enter your choice: ")

            if option == '1':
                add_item()
            elif option == '2':
                check_total()
            elif option == '3':
                add_coupon()
            elif option == '4':
                print_order()
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == '2':
        print("Bye bye!")
        break
    else:
        print("Invalid choice. Please try again.")