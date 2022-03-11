hesapMerve = {

    'ad'        : 'Merve KARTAL',
    'hesapNo'   : '1356489',
    'bakiye'    :   3500,
    'ekHesap'   :   2500
}

hesapAli = {

    'ad'        : 'Ali KARTAL',
    'hesapNo'   : '35615498451',
    'bakiye'    :   2000,
    'ekHesap'   :   1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap ['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranız hazırlanıyor, Lütfen kartınızı alınız')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap'] 

        if (toplam >= miktar):
            ekHasapKullanimi = print(input('Ek hesap kullanılsın mı? (E/H)'))

            if ekHasapKullanimi == 'E':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranız hazırlanıyor, Lütfen kartınızı alınız')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL vardir.")
        else:
            print('Bakiyeniz yetersizdir')
            bakiyeSorgula(hesap)
    
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")


paraCek(hesapMerve, 3500)

print("*********************************")

paraCek(hesapMerve, 2500)