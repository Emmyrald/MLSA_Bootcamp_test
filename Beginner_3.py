''' Write a program to determine if a year is a leap year or a common year '''
def is_leap(year = int(input('Enter a year to know if it is a leap year: '))):
    # Divide year by 4 to determine if it is a leap year
    leap = year/4
    if leap == round(leap):
        response = "Leap Year"
    else:
        response = "Common Year"
    return response
print (is_leap())
