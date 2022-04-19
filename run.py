import ogrenci

while True:
    a = int(input('''
    Ögrenci kaydetmek için ----> 1
    Öğrenci listesi için ------> 2
    Öğrenci ortalamaları ------> 3
    Çıkış yapmak için ---------> 0

    '''))
    if a == 1 :
        ad= input("adı = ")
        soyad = input("soyadı = ")
        not1 = int(input("not1 = "))
        not2= int(input("not2 = "))
        not3 = int(input("not3 = "))
        o = ogrenci.Ogrenci(ad,soyad,not1,not2,not3)
        with open("ogrenci listesi.txt","a",encoding="utf-8") as file:
            content = o.bilgiler()
            file.write(content)
            file.write("\n")
    elif a == 2:
        print("**********ÖĞRENCİ LİSTESİ**********")
        with open("ogrenci listesi.txt","r",encoding="utf-8") as file:
            print(file.read())

    elif a == 3:
        with open("ogrenci listesi.txt","r",encoding="utf-8") as file:
            satırlar = file.readlines()

            for i in satırlar:
                a = i[-12:-2]
                print(a)
                a = a.split(", ")
                print(a)
                sonuc = 0
                for i in a:
                    i = int(i)
                    sonuc +=i

                ortalama = sonuc / 3
                print(ortalama)

                if ortalama <50:
                    harfnotu = "FF"
                elif ortalama >85:
                    harfnotu = "AA"
                else :
                    harfnotu = "CC"

                with open("harf notları.txt", "a", encoding="utf-8") as file:
                    file.write(f"HARF NOTU = {harfnotu} \n")




    elif a == 0 :
        print("Çıkıldı")
        break