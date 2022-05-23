class Ogrenci:
    def __init__(self, id,ogrencino,ad,soyad,dogumtarihi,cinsiyet,classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.ogrencino = ogrencino      
        self.ad = ad
        self.soyad = soyad
        self.dogumtarihi = dogumtarihi
        self.cinsiyet = cinsiyet
        self.classid = classid

    @staticmethod
    def OgrenciYarat(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Ogrenci(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Ogrenci(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list