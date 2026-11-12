# Area Calculation 
 
print("1. Area of Circle") 
print("2. Area of Rectangle") 
print("3. Area of Triangle") 
 
choice = int(input("Enter your choice: ")) 
 
if choice == 1: 
    r = float(input("Enter radius: ")) 
    area = 3.14 * r * r 
    print("Area of Circle =", area) 
 
elif choice == 2: 
    length = float(input("Enter length: ")) 
    width = float(input("Enter width: ")) 
    area = length * width 
    print("Area of Rectangle =", area) 
 
elif choice == 3: 
    base = float(input("Enter base: ")) 
    height = float(input("Enter height: ")) 
    area = 0.5 * base * height 
    print("Area of Triangle =", area) 
 
else: 
 print("Invalid choice")