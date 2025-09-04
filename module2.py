# 1 Write a program that asks your name and then greets you by your name

# text=input("What is your first name? \n")
# text1=input("What is your last name? \n")
# print("Hello,"+" " +text+" "+text1+" ")

# 2 Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

# import math
# radius=int(input("Enter the radius of the circle\n"))
# print(math.pi*radius*radius)

# 3 Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

# length=int(input("Enter the length of Rectangle\n"))
# width=int(input("Enter the width of Rectangle\n"))
# perimeter=length+width+length+width
# print("The perimeter of Rectangle is",perimeter)
# area=length*width
# print("The area of Rectangle is" ,area)

# 4 Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))
# num3=float(input("Enter the third number: "))
# sum=num1+num2+num3
# print("The total sum is",sum)
# product=num1*num2*num3
# print("The product is",product)
# average=(num1+num2+num3)/3
# print("The average is",average)

# 5 Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

# talents=float(input("Enter the number of talents: "))
# pounds=float(input("Enter the number of pounds: "))
# lots=float(input("Enter the number of lots: "))
# grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
# Kilogram=grams/1000
# print('The weight in modern units is',Kilogram,'kg')

# 6 Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

# import random
# print('3 digit code: ',random.randint(0,9),random.randint(0,9),random.randint(0,9))
# print('4 digit code: ',random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6))
