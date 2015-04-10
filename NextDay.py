from ConvertToLunarDate import get_month_days
from ConvertToLunarDate import get_syear_days
from ConvertToLunarDate import get_lunar_date

BASE_DATE = (1901, 1, 1, 2)
#calculate the next day of the input day
def nextDay(year, month, day):
    month_days = get_month_days(year, month)
    if day < month_days:
        day = day + 1
        return (year, month, day)
    elif day == month_days:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
        return (year, month, day)

#validate the input date
def validateDate(year, month, day):
    result = True
    if year < 1900 or year > 2100:
        result = False
    elif month < 1 or month > 12:
        result = False
    elif day < 1 or day > get_month_days(year, month):
        result = False
    return result

#get the day of week of the input date
def nextDayOfWeek(year, month, day):
    week_table = ["星期二", "星期三","星期四", "星期五","星期六","星期日", "星期一"]
    total_days = 0
    for i_year in range(1901, year):
        total_days += get_syear_days(i_year)
    for i_month in range(1, month):
        total_days += get_month_days(year, i_month)
    total_days += day
    remain_days = total_days % 7
    return week_table[remain_days]

#combine for test
def main():
    year = input("Please input the year:")
    month = input("Please input the month:")
    day = input("Please input the day:")
    year = int(year)
    month = int(month)
    day = int(day)
    if validateDate(year,month,day):
        print("Input is valid!")
    else:
        print("The input is not valid, program will exit!")
        return
    print("The next day of the input day is:" + str(nextDay(year, month, day)))
    print("The day of the week for next day is:" + str(nextDayOfWeek(year, month, day)))
    print("The day == Lunar year:", get_lunar_date(year, month, day))
    print("Program End!")

if __name__ == "__main__":
    main()


