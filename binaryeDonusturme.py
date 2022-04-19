#Binary - Decimal dönüşüm yapan pyhton kodu 
#bitsel işlem operatörleri şunlardır
# ve->'&' veya->'|' xor->'^' değil(tümleyen)->'~' 
#SağaSolaKaydırma-> '<<' '>>'
a =input("İkilik (binary) forma dönüştürülecek sayıyı giriniz :")
a =int(a)
print(bin(a))
c=~a
print(c)