print("MENGHITUNG LUAS PERSEGI PANJANG")
print("===============================")

p = int(input("Nilai Panjang :"))
l = int(input("Nilai Lebar   :"))

luas = p*l
print("Luas Persegi Panjang adalah : ", luas)

if luas % 2 == 0:
    print("Hasil luas persegi panjang bilangan Even Rectangle")
else:
    print("Hasil luas persegi panjang bilangan Odd Rectangle")
