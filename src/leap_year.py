def is_leap_year() -> bool:
    year: int = int(input("Enter a year: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"El año {year} es bisiesto")
        return True

    print(f"El año {year} no es bisiesto")
    return False
