from datetime import datetime
import math

def get_days_from_today(date):
    #current day
    current_date = datetime.now() 
    #given day in datetime
    given_date = datetime.strptime(date, "%Y-%m-%d")  
    #difference between given day and today
    days_difference = given_date.toordinal()-current_date.toordinal()
    return days_difference

result = get_days_from_today("2024-04-20")
if result>0:
    print(f"До введеної дати лишилось: {result} дні(в)")
elif result<0:
    print(f"Від введеної дати пройшло: {int(math.fabs(result))} дні(в)")
else:
    print("Введена дата сьогодні")
