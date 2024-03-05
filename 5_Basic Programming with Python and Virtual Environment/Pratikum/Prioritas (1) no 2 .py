class KelasLatihan:
    def __init__(self, nama, spesialisasi, tahunPengalaman, jadwal):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman
        self.__jadwal = jadwal

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_spesialisasi(self):
        return self.__spesialisasi

    def set_spesialisasi(self, spesialisasi):
        self.__spesialisasi = spesialisasi

    def get_tahunPengalaman(self):
        return self.__tahunPengalaman

    def set_tahunPengalaman(self, tahunPengalaman):
        self.__tahunPengalaman = tahunPengalaman

    def get_jadwal(self):
        return self.__jadwal

    def set_jadwal(self, jadwal):
        self.__jadwal = jadwal

    def tampilkanInfo(self):
        print("Info Kelas Latihan:")
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahunPengalaman)
        print("Jadwal:", self.__jadwal)


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jadwal, tingkat_kesulitan):
        super().__init__(nama, spesialisasi, tahunPengalaman, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan

    def get_tingkat_kesulitan(self):
        return self.__tingkat_kesulitan

    def set_tingkat_kesulitan(self, tingkat_kesulitan):
        self.__tingkat_kesulitan = tingkat_kesulitan

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat Kesulitan:", self.__tingkat_kesulitan)

    def aturPosisiYoga(self, posisi):
        print("Posisi yoga diatur ke", posisi)


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jadwal, berat_maksimum):
        super().__init__(nama, spesialisasi, tahunPengalaman, jadwal)
        self.__berat_maksimum = berat_maksimum

    def get_berat_maksimum(self):
        return self.__berat_maksimum

    def set_berat_maksimum(self, berat_maksimum):
        self.__berat_maksimum = berat_maksimum

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Berat Maksimum:", self.__berat_maksimum)

    def aturBeratBeban(self, berat):
        print("Berat beban diatur ke", berat)


def panggil_metode_khusus(kelas_latihan):
    if isinstance(kelas_latihan, Yoga):
        kelas_latihan.aturPosisiYoga("Lotus")
    elif isinstance(kelas_latihan, AngkatBeban):
        kelas_latihan.aturBeratBeban(50)
    else:
        print("Kelas latihan tidak diketahui")


yoga1 = Yoga("Tarisa", "Yoga", 5, "Kamis 08.00-09.00", "Sulit")
angkat_beban1 = AngkatBeban(
    "Nova", "Angkat Beban", 3, "Jumat 15.00-17.00", 100)

yoga1.tampilkanInfo()
print()
angkat_beban1.tampilkanInfo()
print()

yoga1.aturPosisiYoga("Mountain Pose")
angkat_beban1.aturBeratBeban(80)
print()

panggil_metode_khusus(yoga1)
panggil_metode_khusus(angkat_beban1)
