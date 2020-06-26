import random

symbols = ['a','b','c','d','e','f','g','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6',
           '7','8','9','0']

passcount = int(input('Введите кол-во генерируемых паролей\n'))

passlenghtmin = int(input('Введите минимальную длинну пароля\n'))

passlenghtmax = int(input('Введите максимальную длинну пароля\n'))

passs = []

for i in range(passcount):
    currentpass = ""
    lenghtofpass = random.randint(passlenghtmin, passlenghtmax)
    for c in range(lenghtofpass):
        symbolindex = random.randint(0, len(symbols)-1)
        uppercase = random.randint(0, 1)
        letter = symbols[symbolindex]
        if uppercase == 1: letter =  letter.upper()
        currentpass += letter
    passs.append(currentpass)

for p in passs:
    print(p)

savetofile = input("Сохранить пароли в txt файл?[Y/N]\n").upper()

if savetofile == "y".upper():
    filename = input("Укажите имя файла\n")
    file = open(filename+".txt", "w")
    for p in passs:
        file.write(p+"\n")