num1 = int(input("enter the first number: "))
num2 = int(input("enter the first number: "))


while num2 != 0:
    num, num2 = num2, num1 % num2
    
print("the gcf is:", num1)