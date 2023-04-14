def root13_sifrele(metin):
    sifrelenmis_metin = ""
    for harf in metin:
        if harf.isalpha():
            karakter_kodu = ord(harf)
            if harf.islower():
                karakter_kodu = (karakter_kodu - 97 + 13) % 26 + 97
            else:
                karakter_kodu = (karakter_kodu - 65 + 13) % 26 + 65
            sifrelenmis_metin += chr(karakter_kodu)
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

def sezar_sifrele(metin, anahtar):
    sifrelenmis_metin = ""
    for harf in metin:
        if harf.isalpha():
            karakter_kodu = ord(harf)
            if harf.islower():
                karakter_kodu = (karakter_kodu - 97 + anahtar) % 26 + 97
            else:
                karakter_kodu = (karakter_kodu - 65 + anahtar) % 26 + 65
            sifrelenmis_metin += chr(karakter_kodu)
        else:
            sifrelenmis_metin += harf
    return sifrelenmis_metin

metin = input("lütfen metin giriniz : ")
root13_sifreli_metin = root13_sifrele(metin)
sezar_anahtar = int(input("lütfen anahtar girinizz :"))
sifreli_metin = sezar_sifrele(root13_sifreli_metin, sezar_anahtar)

print("Orijinal Metin: ", metin)
print("Root13 Şifrelenmiş Metin: ", root13_sifreli_metin)
print("Şifrelenmiş Metin: ", sifreli_metin) 


ef sezar_desifre(sifreli_metin, anahtar):
    orijinal_metin = ""
    for harf in sifreli_metin:
        if harf.isalpha():
            karakter_kodu = ord(harf)
            if harf.islower():
                karakter_kodu = (karakter_kodu - 97 - anahtar) % 26 + 97
            else:
                karakter_kodu = (karakter_kodu - 65 - anahtar) % 26 + 65
            orijinal_metin += chr(karakter_kodu)
        else:
            orijinal_metin += harf
    return orijinal_metin

def root13_desifre(metin):
    orijinal_metin = ""
    for harf in metin:
        if harf.isalpha():
            karakter_kodu = ord(harf)
            if harf.islower():
                karakter_kodu = (karakter_kodu - 97 - 13) % 26 + 97
            else:
                karakter_kodu = (karakter_kodu - 65 - 13) % 26 + 65
            orijinal_metin += chr(karakter_kodu)
        else:
            orijinal_metin += harf
    return orijinal_metin

sifreli_metin = input("lütfen şifreli metni giriniz : ")
sezar_anahtar = int(input("lütfen anahtar giriniz : "))

metin = sezar_desifre(sifreli_metin, sezar_anahtar)
orijinal_metin = root13_desifre(metin)

print("Şifreli Metin: ", sifreli_metin)
print("Deşifrelenmiş Metin: ", orijinal_metin)