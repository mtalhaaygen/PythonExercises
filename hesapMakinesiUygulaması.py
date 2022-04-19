import math
print("HESAP MAKİNESİ UYGULAMASI")
a = input("Bir sayı giriniz : ")
a = float(a)
print("""
		 -------İşlem seçiniz-------
            1)Toplama
            2)Çıkarma
            3)Ondalıklı Bölme /
            4)Çarpma
            5)Üs alma
            6)Kök alma
            7)Tam bölme //
            8)Kalan bulma (mod) %
		         """)
secilenİslem = input("Bir işlem seçiniz : ")
secilenİslem = int(secilenİslem)
if secilenİslem == 1 :
	b = input("Diger sayıyı giriniz...")
	b = float(b)
	print(a,b,sep="+")
	print(a+b)
elif secilenİslem == 2 :
	b = input("Diger sayıyı giriniz...")
	b = float(b)
	print(a,b,sep="-")
	print(a-b)
elif secilenİslem == 3 :
	b = input("Diger sayıyı giriniz...")
	b =float(b)
	print(a,b,sep="/")
	print(a/b)
elif secilenİslem == 4 :
	b = input("Diger sayıyı giriniz...")
	b = float(b)
	print(a,b,sep="x")
	print(a*b)
elif secilenİslem == 5 :
	b = input("Kaçıncı üssü alınsın...")
	b = int(b)
	print(a,b,sep="^")
	print(a**b)
elif secilenİslem == 6 :
	b = math.sqrt(a)
	print(b)
elif secilenİslem == 7 :
	b = input("Diger sayıyı giriniz...")
	b = float(b)
	print(a,b,sep="//")
	print(a//b)
elif secilenİslem == 8 :
	b = input("Diger sayıyı giriniz...")
	b = float(b)
	print(a,b,sep="%")
	print(a%b)
else : print("Seçtiğiniz işlem tanımlanmamıştır")