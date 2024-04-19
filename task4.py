from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date() #receive today's date
    upcoming_birthdays = [] # make empty list

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #parse user birthday in datetime format
        birthday_this_year = user_birthday.replace(year=today.year) #find this year birthday
        if birthday_this_year < today: #if date of birth in the past we check next year
            birthday_this_year = user_birthday.replace(year=today.year+1)
        day_delta = (birthday_this_year - today).days #calculate days quantity till birthday
        
        if 0<= day_delta <=7: # if birthday in next 7 days
            if birthday_this_year.weekday() == 5: #check if birthday in saturday - add 2 days to congratulation day
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6: #check if birthday in sanday - add 1 day to congratulation day
                birthday_this_year += timedelta(days=1)

            upcoming_birthdays.append({ #make list with name and congratulation day
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
                })
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.23"},
    {"name": "Jane Smith", "birthday": "1990.04.20"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)