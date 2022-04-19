from datetime import datetime, timedelta

simdi = datetime.now()
birthday = datetime(1999,7,12,17,30,0)
Age = simdi - birthday

print(f"doğum tarihi {birthday} \n ŞİMDİ = {simdi} \n AGE = {Age}")

print(type(Age),"\n",type(simdi),"\n",type(birthday))

simdi += timedelta(days=730, seconds=60)
print(f"doğum tarihi {birthday} \n ŞİMDİ = {simdi} \n AGE = {Age}")


'''
SONUÇ : iki  <class 'datetime.datetime'> objesi toplanamaz, çıkartılabilir.
        çıkartıldığında farklı bir obje => <class 'datetime.timedelta'> objesi oluşur.
        timedelta metodu ilede tarih bilgisinin üzerine ekleme yapabiliriz
'''



