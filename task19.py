Tea=2
Coffee=4
Juice=3
user_input=input("Enter your choice (Tea/Coffee/Juice): ").upper()
match user_input:
    case "Tea":
        print("The price of Tea is:", Tea)
    case "Coffee":
        print("The price of Coffee is:", Coffee)
    case "Juice":
        print("The price of Juice is:", Juice)
    case _:
        print("Invalid choice.")