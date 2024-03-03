print("Menentukan Sebuah Kata Anagram")
print("===============================")


def anagram(kataA, kataB):

    kataA = kataA.replace(" ", "").lower()
    kataB = kataB.replace(" ", "").lower()

    if len(kataA) != len(kataB):
        return "Bukan Anagram"

    frekuensi_kataA = {}
    for huruf in kataA:
        if huruf in frekuensi_kataA:
            frekuensi_kataA[huruf] += 1
        else:
            frekuensi_kataA[huruf] = 1

    for huruf in kataB:
        if huruf in frekuensi_kataA:
            frekuensi_kataA[huruf] -= 1
        else:
            return "Bukan Anagram"

    for frekuensi in frekuensi_kataA.values():
        if frekuensi != 0:
            return "Bukan Anagram"

    return "Anagram"


kata_pertama = input("Kata pertama: ")
kata_kedua = input("Kata kedua: ")


hasil = anagram(kata_pertama, kata_kedua)
print("Output:", hasil)
