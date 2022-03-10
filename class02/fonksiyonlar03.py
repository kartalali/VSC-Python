def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

sayi = int(input('Lütfen tam bölenleri bulmak istediğiniz sayiyi giriniz: '))

print(tamBolenleriBul(36))