max_withdrawal_limit = 1000.0
withdrawal_amount = float(input("Enter the amount to withdraw: "))
if withdrawal_amount <= 0:
    print("Invalid withdrawal amount.")
elif withdrawal_amount > max_withdrawal_limit:
    print(f"Insufficient balance. Maximum withdrawal limit is {max_withdrawal_limit}.")
