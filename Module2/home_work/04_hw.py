# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
size=int(input("введите размер стороны квадрата: "))
str_topdown=size*"#"
print(str_topdown)
i=2
while i<size:
    str_middle="#"+(size-2)*" "+"#"
    print(str_middle)
    i+=1
print(str_topdown)
