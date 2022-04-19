class Ogrenci():

    def __init__(self,ad,soyad,*notlar):
        self.ad = ad
        self.soyad = soyad
        self.notlar = notlar


    def bilgiler(self):
        return (f"Adı={self.ad} Soyadı={self.soyad} NOTLARI= {self.notlar}")




