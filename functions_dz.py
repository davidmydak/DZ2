def plate():
    your_number = input("Give me your plate : ")
    your_number = your_number.upper()
    lenght = (len(your_number))
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
        print(letters1, a, b, c, d, letters2)
        print(summa(a, b, c, d))
        return your_number
    else:
        print("False")

def summa(a, b, c, d, ):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = a + b + c + d
    print(e)
