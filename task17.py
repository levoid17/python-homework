order_total = float(input("Enter the order total: "))
membership_status = input("Enter membership status (yes/no): ").strip().lower()
shipping_cost = 5
if order_total < 0:
    print("Invalid order total.")
elif membership_status not in ["yes", "no"]:
    print("Invalid membership status.")
elif order_total >= 50 or membership_status == "yes":
    print(f"Total: {order_total} AZN.")
else:
    print(f"Total: {order_total + shipping_cost} AZN.")