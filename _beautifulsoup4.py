htmldoc = """
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Sayfa Başlığı</title><style type="text/css">Buraya css kodlarımız gelir.</style>
</head>
<body><h1>h1 : Sayfada görünen tüm içerik buraya eklenir.</h1>bos : Sayfada görünen tüm içerik buraya eklenir.<div>
<h2>alt başlık</h2><ul><li>Menü1</li><li>Menü2</li><li>Menü3</li></ul>
</div><div><h2>alt başlık2</h2><ul><li>Menü1</li><li>Menü2</li><li>Menü3</li></ul>
</div><a href="http://example.com/elsie" class="sister" id="link1">Elsie</a><img src="f.png"></body></html>
"""
from bs4 import BeautifulSoup

corba = BeautifulSoup(htmldoc, "html.parser")

result = corba.prettify() # bunun ile verdiğimiz karmaşık htmli düzelttik
result = corba.head
result = corba.body
result = corba.title
result = corba.title.name
result = corba.title.string
result = corba.h1

result = corba.find_all("h2")
# yukardaki kod tüm h2 etiketlerinin hepsini liste şeklinde getiriyor
result = corba.find_all("div")[1]
# find_all ile bu şekilde istediğimiz etikete ulaşabiliriz
#h2 etiketine sahip olanları listeye alıp indexi 1 olanı seçtik
#seçtiğimiz bu etiketin altındaki ul etiketine ulaşmak için
result = corba.find_all("div")[1].ul



result = corba.find_all("div")[1].findChildren()
result = corba.find_all("div")[1].findParent().prettify()
'''
parrent
child
sibling(kardeş)
html etiketleri çıkıntılara göre parrent child olarak adlandırılabilir
örnegin burda
<head>
    <meta charset="UTF-8">
    <title>Sayfa Başlığı</title>
    <style type="text/css">
        Buraya css kodlarımız gelir.
    </style>
</head>
meta title ve style etiketleri sibling etiketlerdir 
head etiketi parrentlarıdır.Gibi
'''

#bir sonraki etikete ulaşmak için kullanılır
result = corba.div.findNextSibling()
#bir önceki etikete ulaşmak için ise findPreviousSibling() kullanılır

#print(result)

#bir etiketin içinceki özelliğe ulaşmak için
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
print(corba.a.get("href"))

