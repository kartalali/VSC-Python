'''
    1 ile 100 arasında rastgele üretilecek bir sayıyı
    aşağı yukarı ifadeleri ile buldurmaya çalışalım.
    **100 üzerinden puanlama yapalım.Her bilemediğinde 20 puan düşelim.
     
'''

import random

sayi = random.randint(1,100)
can = 5
sayac = 0

while (can > 0):
    can -= 1 
    sayac += 1 
    tahmin = int(input('Tahmin: '))

    if (sayi == tahmin):
        print(f'Tebrikler {sayac}. defada bildiniz.Toplam puanınız: {100-(sayac-1)*20}')
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    
    if can == 0:
        print(f'Hakkınız bitti. Tutulan sayi: {sayi}')
