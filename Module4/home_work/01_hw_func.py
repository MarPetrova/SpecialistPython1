# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    numbers=str(ticket_number)
    sum1to3=int(numbers[0])+int(numbers[1])+int(numbers[2])
    sum4to6=int(numbers[3])+int(numbers[4])+int(numbers[5])
    if sum1to3 == sum4to6:
        res="Happy"
    else:
        res="Fail"
    return res

#print(lucky_ticket(123006))
#print(lucky_ticket(123213))
#print(lucky_ticket(436751))
print(lucky_ticket(912753))
