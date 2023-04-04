import calendar

def get_day(day_index):
    list_of_days = ["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
    return list_of_days[day_index]
def leap_year(y):
    if y%100 == 0:
        if y%400 == 0:
            return True
        else:
            return False
    else:
        if y%4 == 0:
            return True
        else:
            return False

def check_valid_date(dt,m,y,l):
    if l:
        if m == 2: #Feb of leap year
            if dt < 30:
                return True
            else:
                return False
        else:
            if m < 8: # odd months 31 days
                if m%2 == 1: 
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
            
            else: # even months 31 days
                if m%2 == 0: 
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False

    else:
        if m == 2: #Feb of leap year
            if dt < 29:
                return True
            else:
                return False
        else:
            if m < 8: # odd months 31 days
                if m%2 == 1: 
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
            
            else: # even months 31 days
                if m%2 == 0: 
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False


while(1):
    year = int(input("Enter year (1970-present year) : "))
    if year < 1970:
        print("Enter a year in the range 1970 - present year....")
    else:
        break

while(1):
    month = int(input("Enter month between 1 to 12 : "))
    if 0 > month or month > 12:
        print("Enter a valid month....")
    else:
        break

leap = leap_year(year)

while(1):
    date = int(input("Enter date :"))
    if check_valid_date(date,month,year,leap):
        break
    else:
        print("Enter a valid date.....")


day_index = calendar.weekday(year,month,date)

day_index = get_day(day_index)

print(date,"/",month,"/",year,"falls on",day_index)




