# 1 Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

# num = 3
# while num <= 1000:
#     print(num)
#     num=num+3

 # 2 Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

# inches=float(input("Enter the inches: "))
# while inches>0:
#      centimeters=inches*2.54
#      print(centimeters)
#      inches=float(input("Enter the inches: "))
#      if inches<0:
#          break

# 3 Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.

# num = input("Enter a number: ")
# if num == "":
#     print("No numbers were entered.")
# else:
#     num1 = int(num)
#     smallest = num1
#     largest = num1
#     while num != "":
#         num = input("Enter a number: ")
#         if num != "":
#             num1 = int(num)
#             if num1 < smallest:
#                 smallest = num1
#             if num1 > largest:
#                 largest = num1
#     print(smallest)
#     print(largest)

# 4 Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

# import random
# ran = random.randint(1, 10)
# num = int(input("Enter a number between 1 and 10: "))
#
# while num != ran:
#     if num > ran:
#         print("Too high")
#     else:
#         print("Too low")
#     num = int(input("Enter a number between 1 and 10: "))
# print("Correct", ran)

# 5 Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.

# limit=5
# while limit>0:
#  username=input("Enter your username: ")
#  password=input("Enter your password: ")
#  if username=="python" and password=="rules":
#     print('Welcome')
#     break
#  else:
#     print('enter the username and password again')
#     limit=limit-1
# if limit==0:
#  print('Access denied')

# Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0).
# Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A
# compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points.
# Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test
# if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).












