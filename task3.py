import re
def normalize_phone(phone_number):
    pattern = r"[^0-9]" #regular expression for any character excerpt digits
    norm_number = re.split(pattern, phone_number) #remove all characters excerpt digits
    norm_number = ''.join(norm_number)
    if not norm_number.startswith('38'): #check if number not start from 38 - add "38" to start of number
        norm_number = "38" + norm_number
    norm_number = "+" + norm_number #add + to start of number
    return norm_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)