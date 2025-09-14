# 1 Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

#
# import mysql.connector
#
#
# def fetch_airport_info(icao_code):
#     try:
#         # Connect to the database
#         connection = mysql.connector.connect(
#             host='127.0.0.1',
#             port=3306,
#             database='airport',
#             user='NEW_USER',
#             password='0000',
#             autocommit=True
#         )
#
#         cursor = connection.cursor()
#         query = "SELECT name, municipality FROM airport WHERE ident = %s"
#         cursor.execute(query, (icao_code,))
#
#         result = cursor.fetchone()
#         if result:
#             name, municipality = result
#             print(f"Airport Name: {name}")
#             print(f"Location: {municipality}")
#         else:
#             print("No airport found with that ICAO code.")
#
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#
# if __name__ == "__main__":
#     icao_code = input("Enter the ICAO code of the airport: ")
#     fetch_airport_info(icao_code)

# 2 Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.


# import mysql.connector
#
#
# def fetch_airports_by_country(area_code):
#     connection = None
#     try:
#         # Connect to the database
#         connection = mysql.connector.connect(
#             host='127.0.0.1',
#             port=3306,
#             database='airport',
#             user='NEW_USER',
#             password='0000',
#             autocommit=True
#         )
#
#         cursor = connection.cursor()
#         query = """
#                 SELECT type, COUNT(*) AS count
#                 FROM airport
#                 WHERE iso_country = %s
#                 GROUP BY type
#                 ORDER BY count DESC \
#                 """
#         cursor.execute(query, (area_code,))
#
#         results = cursor.fetchall()
#
#         if results:
#             print(f"Airports in {area_code}:")
#             for airport_type, count in results:
#                 print(f"{count} {airport_type} airports")
#         else:
#             print(f"No airports found for country code '{area_code}'.")
#
#     except mysql.connector.Error as err:
#         print(f"Error: {err.msg} (Error code: {err.errno})")
#
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
#
#
# if __name__ == "__main__":
#     area_code = input("Enter the area code (e.g., 'FI' for Finland): ").upper()
#     fetch_airports_by_country(area_code)

# 3 Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database

# import mysql.connector
# from geopy.distance import great_circle
#
# def fetch_airport_coordinates(icao_code):
#     connection = None
#     try:
#         # Connect to the database
#         connection = mysql.connector.connect(
#             host='127.0.0.1',
#             port=3306,
#             database='airport',
#             user='NEW_USER',
#             password='0000',
#             autocommit=True
#         )
#
#         cursor = connection.cursor()
#         query = """
#         SELECT latitude_deg, longitude_deg
#         FROM airport
#         WHERE ident = %s
#         """
#         cursor.execute(query, (icao_code,))
#         result = cursor.fetchone()
#
#         if result:
#             return result
#         else:
#             print(f"No airport found with ICAO code '{icao_code}'.")
#             return None
#
#     except mysql.connector.Error as err:
#         print(f"Error: {err.msg} (Error code: {err.errno})")
#         return None
#
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
#
# def calculate_distance(icao_code1, icao_code2):
#     coords1 = fetch_airport_coordinates(icao_code1)
#     coords2 = fetch_airport_coordinates(icao_code2)
#
#     if coords1 and coords2:
#         distance = great_circle(coords1, coords2).kilometers
#         print(f"The distance between {icao_code1} and {icao_code2} is {distance:.2f} kilometers.")
#     else:
#         print("Could not calculate the distance due to missing airport data.")
#
# if __name__ == "__main__":
#     icao_code1 = input("Enter the ICAO code of the first airport: ").strip().upper()
#     icao_code2 = input("Enter the ICAO code of the second airport: ").strip().upper()
#     calculate_distance(icao_code1, icao_code2)