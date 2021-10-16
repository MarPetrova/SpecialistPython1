# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    f = open(file, "a")
    newText = text +"\n"
    f.write(newText)
    f.close()

log("hello world")

f = open("log.txt", 'r') #проверяем, что записали в файл
f.seek(0)
print("\nВыводим содержимое файла, удалив символы переноса строки:")
for line in f:
    print("next line:", line.rstrip())
f.close()

def log(text, file):
    f = open(file, "a")
    newText = text + "\n"
    f.write(newText)
    f.close()

log("message", "log01.txt")

f = open("log01.txt", 'r')#проверяем, что записали в файл
f.seek(0)
print("\nВыводим содержимое файла, удалив символы переноса строки:")
for line in f:
    print("next line:", line.rstrip())
f.close()
