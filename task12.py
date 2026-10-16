starting_fee=2
distance=float(input("Enter the distance traveled in kilometers: "))
if distance <= 0:
    print("Invalid distance.")
elif distance <= 5:
    if distance * 0.7 > starting_fee:
        print(f"Your taxi fare is {distance * 0.7:.2f} AZN")
    else:   
        print(f"Your taxi fare is {starting_fee:.2f} AZN")
elif distance <= 15 and distance > 5:
    print(f"Your taxi fare is {distance * 0.6:.2f} AZN")
elif distance > 15:
    print(f"Your taxi fare is {distance * 0.5:.2f} AZN")