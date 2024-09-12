Month_day_year = '%d, %d, %d'

MM = input("Month> ")
DD = input("Day> ")
YY = input("Year> ")

print(Month_day_year) % (MM, DD, YY)