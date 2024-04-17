import random

def get_numbers_ticket(min, max, quantity):
    
    try:
        if min < 1 or max > 1000 or quantity < min or quantity > max:
            return [] #перевіряємо щоб числа відповідали умові
        else:    
            i=min
            number_list = [] #створюємо пустий список
            while i<=max: #цикл від мінімального до максимального числа
                
                number_list.append(i) #додаєм усі числа послідовно в список
                i += 1

            unique_numbers = random.choices(number_list, k=quantity) #вибираємо з списку задану кількість унікальних значень
            unique_numbers.sort() #сортуємо список
            return print(unique_numbers)

    except ValueError:
        return [] #якщо введено взагалі не числа

min = int(input ("Enter minimum number:"))
max = int(input ("Enter maximum number:"))
quantity = int(input ("Enter quantity of digits:"))

get_numbers_ticket(min, max, quantity)
