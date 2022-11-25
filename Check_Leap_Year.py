# check if year is a leap year or not


year = int(input("Enter the year: "))
if year % 400 == 0 and year % 100 == 0:
    print("{0} is the leap year".format(year))
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")