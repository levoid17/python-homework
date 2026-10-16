#online shop checkout

total_price = 0

while True:
    you_want_to_continue = input("Do you want to continue shopping? (yes/no): ").lower()
    if you_want_to_continue == "no":
        print(f"Thank you for shopping with us! Your total price is: {total_price:.2f} AZN")
        break
    item = input("Enter the item name: ").lower()

    match item.lower():
        case "headphones":
            print("item price is 60AZN selected.") 
            headphones_quantity = int(input("Enter the quantity of headphones: "))
            total_price += headphones_quantity * 60
        case "mouse":
            print("item price is 20AZN selected.") 
            mouse_quantity = int(input("Enter the quantity of mice: "))
            total_price += mouse_quantity * 20
        case "keyboard":
            print("item price is 40AZN selected.") 
            keyboard_quantity = int(input("Enter the quantity of keyboards: "))
            total_price += keyboard_quantity * 40
        case _:
            print("Invalid item.")
if total_price > 100:
    print("You have spent more than 100AZN. You are eligible for a SAVE10 coupon.")
    total_price *= 0.9
if total_price > 80:
    print("You have spent more than 80AZN. You are eligible for free shipping.")
    total_price += 0
else:
    print("You have spent less than 80AZN. Shipping cost is 10AZN.")
    total_price += 5
