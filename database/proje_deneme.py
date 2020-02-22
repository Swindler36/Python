from kütüphane import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

6. Database'i temizle


Çıkmak için 'q' ya basın.
***********************************""")

kütüphane = Kütüphane()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        time.sleep(1)
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        print("Kitaplar aranıyor...")
        time.sleep(2)
        kütüphane.kitapları_goster()

    elif (işlem == "2"):
        bilgi = input("Hangi kitabı istiyorsunuz ? ")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        if (not(kütüphane.kitap_sorgula(bilgi) and kütüphane.kitap_sorgula2(bilgi) and kütüphane.kitap_sorgula3(bilgi))):
            print("Bu kitap bulunmuyor...")

        if(kütüphane.kitap_sorgula(bilgi)):
            print(kütüphane.kitap_sorgula(bilgi))
        elif (kütüphane.kitap_sorgula2(bilgi)):
            print(kütüphane.kitap_sorgula2(bilgi))
        elif (kütüphane.kitap_sorgula3(bilgi)):
            print(kütüphane.kitap_sorgula3(bilgi))


    elif (işlem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap ekleniyor....")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi....")


    elif (işlem == "4"):
        bilgi = input("Hangi kitabı silmek istiyorsunuz ?")

        if (not(kütüphane.kitap_sorgula(bilgi) and kütüphane.kitap_sorgula2(bilgi) and kütüphane.kitap_sorgula3(bilgi))):
            print("Bu kitap bulunmuyor...")
        print("Silmek istediğiniz kitap bu mu?")
        if(kütüphane.kitap_sorgula(bilgi)):
            print(kütüphane.kitap_sorgula(bilgi))
            isim = kütüphane.findName(bilgi)
        elif (kütüphane.kitap_sorgula2(bilgi)):
            print(kütüphane.kitap_sorgula2(bilgi))
            isim = kütüphane.findName(bilgi)
        elif (kütüphane.kitap_sorgula3(bilgi)):
            print(kütüphane.kitap_sorgula3(bilgi))
            isim = kütüphane.findName(bilgi)

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E" or cevap == "e"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi....")


    elif (işlem == "5"):
        bilgi = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor....")

        if (kütüphane.kitap_sorgula(bilgi) and kütüphane.kitap_sorgula2(bilgi) and kütüphane.kitap_sorgula3(bilgi)):
            print("Bu kitap bulunmuyor...")

        if(kütüphane.kitap_sorgula(bilgi)):
            isim = kütüphane.findName(bilgi)
        elif (kütüphane.kitap_sorgula2(bilgi)):
            isim = kütüphane.findName(bilgi)
        elif (kütüphane.kitap_sorgula3(bilgi)):
            isim = kütüphane.findName(bilgi)

        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi....")

    elif(işlem == "6"):
        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E" or cevap == "e"):
            print("Kitaplar Siliniyor...")
            time.sleep(2)
            kütüphane.deleteAll()
            print("Kitaplar silindi....")
        else:
            print("Silme işlemi iptal edildi..")


    else:
        print("Geçersiz İşlem...")