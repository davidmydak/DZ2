После выполнения домашнего задания по определению есть ли номерные знаки в списке,

переделать программу, таким образом,

1 . чтоб функция получала на вход введенные данные с командной строки и
Проверяла на соответствие Длине введенного текста
Возвращала 6 значений полученных из введенного номера (по 2 буквы и 4 цифры)
Если общее количество символов больше или меньше 8 (во введенных данных) возвращала False



2. Написать вторую функцию, которая будет считать сумму чисел внутри последовательности.

Функция должна вернуть сумму



3.Использовать эти функции в изначальной задаче
a = 0
b = 0
c = 0
d = 0
def plate(a = "",b = "",c = "",d = ""):
    your_number = input("Give me your plate : ")
    lenght.upper = (len(your_number))
    if lenght == 8:
        letter_1 = your_number[0]
        letter_2 = your_number[1]
        letters1 = letter_1 + letter_2
        letter_3 = your_number[6]
        letter_4 = your_number[7]
        letters2 = letter_3 + letter_4
        a = (your_number[2])
        b = (your_number[3])
        c = (your_number[4])
        d = (your_number[5])
        print(letters1,a, b, c, d, letters2)
        return a, b, c, d
    else:
        print("false")
print(a,b,c,d)
plate()
print(a,b,c,d)
def summa(a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = a + b + c + d
    print(e)
summa(a,b,c,d)