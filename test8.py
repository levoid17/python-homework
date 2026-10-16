total_price = float(input("Enter the total price of the items: "))
if total_price < 0:
    print("Invalid price. Please enter a non-negative number.")
else:
    if total_price > 100 and total_price < 300:
        discount = total_price * 0.10
        final_price = total_price - discount
        print(f"You received a 10% discount. Final price: AZN{final_price:.2f}")
    elif total_price >= 300 and total_price < 500:
        discount = total_price * 0.15
        final_price = total_price - discount
        print(f"You received a 15% discount. Final price: AZN{final_price:.2f}")
    elif total_price >= 500:
        discount = total_price * 0.20
        final_price = total_price - discount
        print(f"You received a 20% discount. Final price: AZN{final_price:.2f}")
    else:
        print(f"No discount applied. Final price: AZN{total_price:.2f}")
