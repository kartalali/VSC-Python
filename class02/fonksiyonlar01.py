def yazdir(kelime,adet):
    print(kelime*adet)

yazdir('Merhaba\n', 10)

def listeyap(*params):
    liste=[]

    for param in params:
        liste.append(param)

    return liste

result = listeyap(10,20,30,40,50,'Merhaba')
print(result)
