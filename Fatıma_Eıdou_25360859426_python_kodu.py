# Orijinal veri tanımlanır
veri = "AAAAABBBCCDDAA"

# Kodlama için gerekli değişkenler
kodlanmis = []
sayac = 1

# İkinci karakterden başlayarak veri dolaşılır
for i in range(1, len(veri)):
    # Eğer karakterler aynıysa sayaç artırılır
    if veri[i] == veri[i - 1]:
        sayac += 1
    else:
        # Farklı karakter gelince sayı ve karakter eklenir
        kodlanmis.append(str(sayac) + veri[i - 1])
        sayac = 1

# Son karakter grubu eklenir
kodlanmis.append(str(sayac) + veri[-1])

# Liste stringe çevrilir
kodlanmis_metin = "".join(kodlanmis)


# Çözme işlemi için değişkenler
cozulmus = []
sayac = ""

# Kodlanmış metin karakter karakter okunur
for karakter in kodlanmis_metin:
    # Eğer rakamsa sayaç stringine eklenir
    if karakter.isdigit():
        sayac += karakter
    else:
        # Harf gelince sayı kadar tekrar edilir
        cozulmus.append(karakter * int(sayac))
        sayac = ""

# Liste stringe çevrilir
cozulmus_metin = "".join(cozulmus)


# Sıkıştırma oranı hesaplanır
azalma = len(veri) - len(kodlanmis_metin)
oran = (azalma / len(veri)) * 100


# Sonuçlar ekrana yazdırılır
print("Orijinal:", veri)
print("Kodlanmış:", kodlanmis_metin)
print("Çözülmüş:", cozulmus_metin)
print("Sıkıştırma Oranı:", oran)