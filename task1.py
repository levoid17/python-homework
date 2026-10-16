a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal")