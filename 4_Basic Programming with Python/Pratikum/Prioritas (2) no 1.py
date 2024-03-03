def hitung_tarif(berat, jarak):
    if berat <= 20:
        tarif_berat = 10000
    elif 21 <= berat <= 30:
        tarif_berat = 15000
    elif 31 <= berat <= 60:
        tarif_berat = 20000
    else:
        tarif_berat = 45000

    if jarak <= 5:
        tarif_jarak = 2000
    elif 6 <= jarak <= 15:
        tarif_jarak = 5000
    elif 16 <= jarak <= 30:
        tarif_jarak = 10000
    else:
        tarif_jarak = 15000

    total_tarif = tarif_berat + tarif_jarak
    return total_tarif


berat = int(input("Berat: "))
jarak = int(input("Jarak: "))

tarif_pengiriman = hitung_tarif(berat, jarak)
print("Output:", tarif_pengiriman)
