import json


class User:
    def __init__(self,kullaiciadi,parola,mail):
        self.kullaniciadi = kullaiciadi
        self.parola = parola
        self.mail = mail


class UserRepository:
    def __init__(self):
        pass

    def register(self):
        #kullanıcı oluşturma işlemi
        username = input("USERNAME =")
        password = input("PASSWORD =")
        mail = input("MAİL =")

        a = User(username,password,mail)

        dic = {}
        dic["kullaniciadi"] = a.kullaniciadi
        dic["parola"] = a.parola
        dic["mail"] = a.mail


        self.savetoFile(dic)


    def savetoFile(self,user):
        #kullanıcı bilgilerinin hepsini okuyup alacak
        # okunan bilgileri dicte çevirecek
        # dicte user verisini ekleyeceksin
        # tüm veriyi jsona dönüştüreceksin
        # json olarak database e kaydedecek
        #yukarıda kısa bir algoritma oluşturduk bu herzaman kolaylık sağlar
        with open("kullanicibilgileri.json", mode="r", encoding="utf-8") as file:
            file.seek(0)
            data = file.read()
            data = json.loads(data)
            data[f"{len(data)}"] = user
            d = json.dumps(data,indent=4,sort_keys=True)

        with open("kullanicibilgileri.json", mode="w", encoding="utf-8") as file:
            file.write(d)

    def login(self):
        #kullanıcı giriş işlemi
        #dosyadan str tipindeki veriler okunur json dan dict e dönüştürülür
        with open("kullanicibilgileri.json",mode="r",encoding="utf-8") as file:
            veri = file.read()
            veri = json.loads(veri)

        usern = input("USERNAME =")
        password = input("PASSWORD =")

        kosul = False
        #for döngüleriyle tüm dictler içerisinde sırayla karşılaştırma yapılır
        #eşitlik sağlanınca giriş yapılır
        for i in veri.values():
            if i["kullaniciadi"] == usern and i["parola"] == password:
                kosul = True
                print("Giriş başarılı")
                while True:
                    b = input('Çıkış yap --->0\nBilgileri göster --->1\n...')
                    if b == "0":
                        break
                    elif b == "1":
                        print("hello")
                        print(i["kullaniciadi"],i["mail"],i["parola"])
                break

        if kosul == False:
            print("Giriş başarısız")

while True:
    a = input('''
    ************* ANASAYFA *************
    Giriş yap ---> 0
    Üye ol ---> 1
    Çıkış yap --->2
    ''')

    u = UserRepository()

    if a == "1" :
        UserRepository.register(u)
        print("Üye oldunuz")

    elif a == "0" :
        UserRepository.login(u)

    elif a == "2" :
        break
