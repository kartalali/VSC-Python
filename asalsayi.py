#Asal sayı uygulaması

sayi = int(input('Bir sayı giriniz: '))
prime = True

if sayi == 1:
    prime = False

for i in range(2, sayi):
    if (sayi % i == 0):
        prime = False
        break

if prime:
    print('Sayı asaldır')
else:
    print('Sayı asal değildir.')
