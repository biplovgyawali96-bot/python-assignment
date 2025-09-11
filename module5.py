# 1 Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

# import random
#
# numdice = int(input("How many dice do you want to roll? "))
# total = 0
# for i in range(numdice):
#     roll = random.randint(1, 6)
#     total = total + roll
# print("Sum of dice:", total)

# 2 Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

# numbers = []
#
# while True:
#     entry = input("Enter a number (empty to quit): ")
#     if entry == "":
#         break
#     numbers.append(int(entry))
#
# numbers.sort(reverse=True)
# print("Five greatest numbers:", numbers[:5])

# 3 Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
#
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

# n = int(input("Enter an integer: "))
#
# if n < 2:
#     print("Not a prime number")
# else:
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break
#     if prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")

# 4 Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

# cities = []
#
# for i in range(5):
#     city = input("Enter the name of a city: ")
#     cities.append(city)
#
# print("You entered:")
# for c in cities:
#     print(c)
