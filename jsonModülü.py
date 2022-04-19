import json
# json un açılımı JavaScriptObjectNotation
#internetten örnek bir json aldım dosyaya yazdım
#daha sonra dosyadaki aslında string olan json veriyi
# jsondan json.loads() metoduyla pythonda kullanabileceğimiz
# dictionary veri tipine dönüştürdük
with open("subat.json",mode="r") as file :
    veri = file.read()
    print(veri)
    print(type(veri))
    print("************************\n"*5)
    veri = json.loads(veri) # JSON string to Dict
    print(veri)
    print(type(veri))

#Elimizde veri adında dict tipindeki dataları değiştirip jsona çevirelim
print(type(veri)) # ÇIKTI : <class 'dict'>
veri["urunler"][0]["yil"] = 2022


veri = json.dumps(veri,indent=4,sort_keys=True) # Dict to JSON string
print(veri)


print(type(veri)) # ÇIKTI : <class 'str'>

'''

# yeni verilerimizi yeni.json dosyasına kaydettik fakat 
# aşağıdaki kod ile süslü bir şekilde yapamamıştık

with open("yeni.json","w") as f:
    json.dump(veri,f)

zaten dönüştürme işlemi uygulamışsın bunu dosyaya kaydederken tekrar etmene gerek yok yavrum
DİREKT =
'''
with open("yeni.json","w") as f:
    f.write(veri)