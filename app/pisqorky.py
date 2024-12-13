
pole = []
radky = 15
sloupce = 15
w = "není vítěz"
for i in range(radky):
    inner_list = [0 for j in range(sloupce)]
    pole.append(inner_list)
print(pole)

winner = False

while (winner == False):
    #křížky
    print("nyní hrají křížky")
    pridani_na_radek = int(input("zadej řádek "))
    pridani_do_sloupce = int(input("zadej sloupec "))
    radek = pole[pridani_na_radek - 1]
    while (radek[pridani_do_sloupce - 1] != 0):
        print("vyberte jiné souřadnice")
        pridani_na_radek = int(input("zadej řádek "))
        pridani_do_sloupce = int(input("zadej sloupec "))
    pole[pridani_na_radek -1][pridani_do_sloupce -1] =1
    rada = 0
    #řádky
    for i in radek:
        if (i==1):
            rada += 1
        else:
            rada = 0
        if (rada == 5):
            w = "vyhrály křížky"
            winner = True
            break
    #sloupce
    rada = 0
    for r in pole:
        if (r[pridani_do_sloupce - 1] == 1):
            rada += 1
        else:
            rada = 0
        if (rada == 5):
            w = "vyhrály křížky"
            winner = True
            break
    #diagonála
    rada = 0
    pozice = pridani_do_sloupce - pridani_na_radek
    if (pozice < 0):
        pozice = 0
    print("pozice: ", pozice)
    for r in pole:
        print(r)
        print(r[pozice])
        if (r[pozice] == 1):
            rada += 1
        else:
            rada = 0
        if (rada == 5):
            w = "vyhrály křížky"
            winner = True
            break
        if (pozice == 14):
            break
        pozice += 1

    for row in pole:
        for element in row:
            print(element, end=' ')
        print()
    if winner == True:
        break

    print("nyní hrají kolečka")
    pridani_na_radek = int(input("zadej řádek "))
    pridani_do_sloupce = int(input("zadej sloupec "))
    radek = pole[pridani_na_radek - 1]
    while (radek[pridani_do_sloupce - 1] != 0):
        print("vyberte jiné souřadnice")
        pridani_na_radek = int(input("zadej řádek "))
        pridani_do_sloupce = int(input("zadej sloupec "))
    pole[pridani_na_radek - 1][pridani_do_sloupce - 1] = 2
    for i in radek:
        if (i==2):
            rada += 1
        else:
            rada = 0
        if (rada == 5):
            w = "vyhrály kolečka"
            winner = True
            break
    rada = 0
    for r in pole:
        if (r[pridani_do_sloupce - 1] == 2):
            rada += 1
        else:
            rada = 0
        if (rada == 5):
            w = "vyhrály kolečka"
            winner = True
            break
    # diagonála
    rada = 0
    pozice = pridani_do_sloupce - pridani_na_radek
    if (pozice < 0):
        pozice = 0
    print("pozice: ", pozice)
    for r in pole:
        print(r)
        print(r[pozice])
        if (r[pozice] == 1):
            rada += 1
        else:
            rada = 0
        if (rada == 5):
            w = "vyhrály křížky"
            winner = True
            break
        if (pozice == 14):
            break
        pozice += 1

    for row in pole:
        for element in row:
            print(element, end=' ')
        print()
    if winner == True:
        break
print (w)