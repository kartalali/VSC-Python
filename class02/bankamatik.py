hesapMerve = {

    'ad'        : 'Merve KARTAL',
    'hesapNo'   : '1356489',
    'bakiye'    :   9500,
    'ekHesap'   :   7500
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
        print('Buyrun paranız')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap'] 

        if (toplam >= miktar):
            ekHasapKullanimi = print(input('Ek hesap kullanılsın mı? (E/H)'))

            if ekHasapKullanimi == 'E':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Buyrun paranız')

            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} vardir.")
        else:
            print('Bakiye yetersiz')


paraCek(hesapAli, 2000)
paraCek(hesapAli, 1000)