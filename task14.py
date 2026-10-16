#triangle
a=int(input("Enter the first side of the triangle: "))
b=int(input("Enter the second side of the triangle: "))
c=int(input("Enter the third side of the triangle: "))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("The triangle is equilateral.")
    elif a==b or b==c or a==c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.")
