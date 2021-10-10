# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def hh_mm_ss(sec):
    hh=sec//60**2
    mm=sec//60-hh*60
    ss=sec-hh*60*60-mm*60
    #return f"{hh}:{mm}:{ss}"
    return f"{hh:0>2}:{mm:0>2}:{ss:0>2}"
print(hh_mm_ss(29143))
print(hh_mm_ss(300))
print(hh_mm_ss(58))
