#restored pin is 0437
user_pin=input("PIN must be 4 digits: ")
if len(user_pin) == 4 and user_pin.isdigit() and user_pin == "0437":
    print("Valid PIN.")
else:
    print("Invalid PIN.")
