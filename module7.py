# 1 Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter

# seasons = ("Winter", "Spring", "Summer", "Autumn")
# month = int(input("Enter the number of month : "))
# if month in (12, 1):
#      print(seasons[0])
# elif month in (2, 3, 4):
#     print(seasons[1])
# elif month in (5, 6, 7, 8):
#     print(seasons[2])
# elif month in (9, 10, 11):
#     print(seasons[3])
# else:
#    print('Invalid number')

# 2 Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.

# names = set()
# name = input("enter the name")
# while name != "":
#     if name in names:
#         print("Existing name")
#     else:
#         print("New name")
#         names.add(name)
#     name = input()
# for n in names:
#     print(n)

# 3 Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)


# airports = {}
# while True:
#     choice = input("Enter 'new' to add, 'fetch' to find, or 'quit' to exit: ")
#     if choice == "new":
#         icao = input("Enter ICAO code: ")
#         name = input("Enter airport name: ")
#         airports[icao] = name
#     elif choice == "fetch":
#         icao = input("Enter ICAO code: ")
#         if icao in airports:
#             print(airports[icao])
#         else:
#             print("Airport not found")
#     elif choice == "quit":
#         break
#     else:
#         print("Invalid choice")





