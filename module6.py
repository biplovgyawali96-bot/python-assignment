# 1 Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

# import random
#
# roll = 0
# while roll != 6:
#     roll = random.randint(1, 6)
#     print("Rolled:", roll)

# 2 Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.

# import random
#
# sides = int(input("Enter number of sides: "))
# roll = 0
# while roll != sides:
#     roll = random.randint(1, sides)
#     print("Rolled:", roll)

# 3 Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

# while True:
#     gallons = float(input("Enter gallons (negative to quit): "))
#     if gallons < 0:
#         break
#     litres = gallons * 3.78541
#     print(gallons, "gallons is", round(litres, 2), "litres")

# 4 Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for n in numbers:
#     total = total + n
# print("Sum:", total)

# 5 Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.

# numbers = [1, 2, 3, 4, 5, 6, 7]
# evens = []
# for n in numbers:
#     if n % 2 == 0:
#         evens.append(n)
#
# print("Original:", numbers)
# print("Evens:", evens)

# 6 Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

import math

# d1 = float(input("Enter diameter of pizza 1 (cm): "))
# p1 = float(input("Enter price of pizza 1 (€): "))
# d2 = float(input("Enter diameter of pizza 2 (cm): "))
# p2 = float(input("Enter price of pizza 2 (€): "))
#
# r1 = d1 / 2
# r2 = d2 / 2
# a1 = math.pi * r1 * r1 / 10000   
# a2 = math.pi * r2 * r2 / 10000
#
# u1 = p1 / a1
# u2 = p2 / a2
#
# print("Pizza 1 unit price:", u1, "€/m²")
# print("Pizza 2 unit price:", u2, "€/m²")
#
# if u1 < u2:
#     print("Pizza 1 is better value")
# elif u2 < u1:
#     print("Pizza 2 is better value")
# else:
#     print("Both are the same value")
