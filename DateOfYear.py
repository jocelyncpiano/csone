def is_year_leap (year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True
    
def days_in_month(year, month): 
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap (year) and month==2:
        return 29
    else:
        return months[month]
        
def day_of_year(year, month, day):
    if year<=0 or month<=0 or day<=0:
        return None
    if day>days_in_month(year, month):
        return None
    day_of_yr = 0
    for x in range (1, month):
        day_of_yr+=days_in_month(year, x)
    return day_of_yr+day
    
        
print(day_of_year(2000, -5, 31))
print(day_of_year(1987, 5, 32))
print(day_of_year(1985, 6, 31))
print(day_of_year(1991, 7, 20))
print(day_of_year(2024, 3, 22))
print(day_of_year(2200, 9, 30))