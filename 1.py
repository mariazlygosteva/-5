year = int(input("Введите год: "))
def days_in_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365
print(days_in_year(year))
