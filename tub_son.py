def tub_sonlarni_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar

oraliq1 = int(input("Birinchi oraliq: "))
oraliq2 = int(input("Ikkinchi oraliq: "))
tub_oraliq = tub_sonlarni_top(oraliq1,oraliq2)
print(tub_oraliq)