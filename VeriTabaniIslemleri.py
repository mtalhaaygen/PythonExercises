import sqlite3

# connected fonksiyonu ile veritabanı mecvutsa bağlantı kurar, mevcut değilse oluşturur.
# İstediğimiz veritabanı uzantısını teercih edebiliriz (.db .sqlite vs)
veritabanix = sqlite3.connect("hahaha.db")
veritabani = sqlite3.connect("sozluk.sqlite")

#SQLite veritabanımız üzerinde işlem yapabilmek için bir imleç(kürsör) oluşturmamız gerekir.
imlec = veritabani.cursor()

'''
imlec.execute("CREATE TABLE kelimeler(English TEXT,Turkish TEXT)")
'''
# eğer kelimeler adlı bir tablo daha önce oluşturulmuşsa yukarıdaki kod hata verir.
# (sqlite3.OperationalError: table kelimeler already exists) hatasını almamak için
imlec.execute("CREATE TABLE IF NOT EXISTS kelimeler(English TEXT,Turkish TEXT)")
#iki kolonlu bir tablo oluşturduk. Tablo oluştururken TR karakterlerden uzak durmakta fayda var


#veri eklemek için INSERT INTOyu kullanıyoruz.
imlec.execute("INSERT INTO kelimeler(English ,Turkish) VALUES('Apple','Elma')")
# Eğer commit komutunu çalıştırmazsak yapılan değişiklikler kaydedilmez
#birden çok değişiklik yapılacaksa bu komutu en sonda çağırmamız yeterli olacaktır

# Eğer bir tabloda yer alan tüm sütunlara tabloda yer aldığı sırayla ekleme yapılacaksa
# INSERT komutu şu şekilde kullanılabilir
imlec.execute("INSERT INTO kelimeler VALUES('Operating system (OS)','İşletim sistemi')")

liste = [("Book","Kitap"),
         ("Developer","Geliştirici"),
         ("Push","İttirmek"),
         ("Attribute","Öznitelik")]
#bir listeyi tabloya eklemek
for k in liste:
    imlec.execute("INSERT INTO kelimeler VALUES(?,?)",k)

# birden çok execute işleminden sonra commit ile o ana kadar olan değişiklikleri kaydediyoruz.
veritabani.commit()

#Listeleme işlemini fetch metodlarını kullanmadan gerçekleştirebiliriz
imlec.execute("SELECT * FROM kelimeler")
for veri in imlec:
    print(veri)


#veritabanı üzerinde gerçekleştirdiğimiz işlemleri tamamladıktan sonra close() ile bağlantı kapatılır.
#Eğer kapatılmazsa herhangi bir hata vermesede
# bağlantıyı kapatarak işletim sisteminin kullandığı kaynaklar serbest bırakılmış olur
veritabani.close() # sistemi yormayalım
vt = sqlite3.connect("sozluk.sqlite")
imlec = vt.cursor()

#GÜNCELLEME
imlec.execute("UPDATE kelimeler SET English='I dont know'")
# Yukardaki kod ile tablodaki tüm ingilizce sütunu "I dont know" oldu Böyle olmaması için
# aşağıdaki gibi koşul eklemeliydik
imlec.execute("UPDATE kelimeler SET English='Apple' WHERE Turkish= 'Elma'")
imlec.execute("UPDATE kelimeler SET English='Operating system (OS)' WHERE Turkish= 'İşletim sistemi'")


#LİSTELEME
imlec.execute("SELECT * FROM kelimeler")
'''
a = imlec.fetchall() # hepsini liste olarak yazmamızı sağlar
print(a)
'''
a = imlec.fetchmany(3) # sıradaki üç tanesini liste olarak yazdırmak için
print(a) # eğer daha önce listeleme yapmadıysak ilk baştan başlar yaptıysak sıradakinden

print(imlec.fetchone()) # sıradakini yazdırmak için
print(imlec.fetchone()) # eğer daha önce listeleme yapmadıysak ilkini yazdırır yaptıysak sıradakini yazdırır

#Listeleme işleminde farkettiğim bir durum var
# bu üç metod iteratör gibi çalışıyor sıradakini yada sıradakilerini listeliyor
#fetch --all (hepsini) , --many (istediğin kadarını) , -- one (bir tanesini)



#SİLME
imlec.execute("DELETE FROM kelimeler WHERE English='I dont know'")

vt.commit()
vt.close()


print("**************\n"*4)

#ilk başta bağlantı yaptığımız veri tabanı üzerinden işlem yapmak için cursor(imleç) oluşturduk.
cursor = veritabanix.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS kelimeler(English TEXT,Turkish TEXT)")

liste = [("Book","Kitap"),
         ("Developer","Geliştirici"),
         ("Push","İttirmek"),
         ("Attribute","Öznitelik")]
for k in liste:
    cursor.execute("INSERT INTO kelimeler VALUES(?,?)",k)

cursor.execute("SELECT * FROM kelimeler")
datalar = cursor.fetchall()

'''
VERİLERE TABİKİDE BU ŞEKİLDEDE ULAŞABİLİRİZ
print(datalar)
for data in datalar:
    print(data)
    print(data[0])
'''
#Eğer verilere sütun adıyla ulaşmak istiyorsak row_factory özelliğini row olarak belirlemeliyiz

veritabanix.row_factory = sqlite3.Row
cursor = veritabanix.cursor()
cursor.execute("SELECT * FROM kelimeler")
datalar = cursor.fetchall()

for data in datalar:
    print("ingilizce=",data["English"],"--türkçe=",data["Turkish"])


#BELLEKTE GEÇİCİ VERİTABANLARI OLUŞTURMA

databasess = sqlite3.connect(":memory:")

# ":memory:" ifadesi ile program çalışırken Ram bellek üzerinde veritabanı oluşturulması sağlanmış olur
#bu veritabanı programon çalışma esnasında oluşturulup program kapatılınca silinir