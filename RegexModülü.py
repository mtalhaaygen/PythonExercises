import re

# Bu modül genel olarak bize arama sonucunda bir sonuç döndürür.
#açılımı regular expression
#regular expression karakterlerini yazmayı biliyor olmamız gerekiyor
#sadece python a özel bir şey değil(regular expression)
#

# örnegin kullanıcıdan alınan bir input email adresi formatına uyuyor mu?
# Bunun regular expression ifadesini oluşturup kullanıcı dogru formatta veri girerse
# veriyi kaydedeiyoruz, dogru formatta girmezse kullanıcıya hata mesajı veriyoruz.
#

print(dir(re))

str = "Selamın aleyküm arkadaşlar | I love you "
result = re.findall("la",str)

result = re.split(" ",str)

result = re.sub(" ","\/",str)

result = re.search("love",str)

print(result)

for i in dir(result):
    print(i)