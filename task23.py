#ATM transaction
account_balance = 1000.0
user_pin = input("Enter your 4-digit PIN: ")
if len(user_pin) == 4 and user_pin.isdigit() and user_pin == "0437":
    print(f"Welcome! Your current balance is: {account_balance:.2f} AZN")
    withdraw_amount = float(input("Enter the amount you wish to withdraw :(withdrawal amount must be multiplicity of 10) "))
    if 0 < withdraw_amount <= account_balance and withdraw_amount % 10 == 0:
        account_balance -= withdraw_amount
        print(f"Withdrawal successful. Your new balance is: {account_balance:.2f} AZN")
    else:
        print("Invalid withdrawal amount.")

else:
    print("Invalid PIN. Please enter a 4-digit number.")