class Pelanggan:
    def __init__(self, nama, usia, idPelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__idPelanggan = idPelanggan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_usia(self):
        return self.__usia

    def set_usia(self, usia):
        self.__usia = usia

    def get_idPelanggan(self):
        return self.__idPelanggan

    def set_idPelanggan(self, idPelanggan):
        self.__idPelanggan = idPelanggan

    def tampilkanInfo(self):
        print("Informasi :")
        print("Nama:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__idPelanggan)


class Pelatih:
    def __init__(self, nama, spesialisasi, tahunPengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman

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

    def tampilkanInfo(self):
        print("Informasi:")
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahunPengalaman)


class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(nama, spesialisasi, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal

    def get_jenisLatihan(self):
        return self.__jenisLatihan

    def set_jenisLatihan(self, jenisLatihan):
        self.__jenisLatihan = jenisLatihan

    def get_jadwal(self):
        return self.__jadwal

    def set_jadwal(self, jadwal):
        self.__jadwal = jadwal

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Jenis Latihan:", self.__jenisLatihan)
        print("Jadwal:", self.__jadwal)


class Pelanggan:
    def __init__(self, nama, usia, idPelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__idPelanggan = idPelanggan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_usia(self):
        return self.__usia

    def set_usia(self, usia):
        self.__usia = usia

    def get_idPelanggan(self):
        return self.__id_pelanggan

    def set_idPelanggan(self, idPelanggan):
        self.__idPelanggan = idPelanggan

    def tampilkanInfo(self):
        print("Info Pelanggan:")
        print("Nama:", self.__nama)
        print("Usia:", self.__usia)
        print("ID Pelanggan:", self.__idPelanggan)


class Pelatih:
    def __init__(self, nama, spesialisasi, tahunPengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman

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

    def tampilkanInfo(self):
        print("Info Pelatih:")
        print("Nama:", self.__nama)
        print("Spesialisasi:", self.__spesialisasi)
        print("Tahun Pengalaman:", self.__tahunPengalaman)


class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(nama, spesialisasi, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal

    def get_jenisLatihan(self):
        return self.__jenisLatihan

    def set_jenisLatihan(self, jenisLatihan):
        self.__jenisLatihan = jenisLatihan

    def get_jadwal(self):
        return self.__jadwal

    def set_jadwal(self, jadwal):
        self.__jadwal = jadwal

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Jenis Latihan:", self.__jenisLatihan)
        print("Jadwal:", self.__jadwal)


pelanggan1 = Pelanggan("Tarisa", 21, "H02")
pelatih1 = Pelatih("Rafi", "Running", 7)
kelas_latihan1 = KelasLatihan(
    "Rafi", "Lari 5Km", 7, "Running", "Senin, Selasa, dan Rabu 16.00-17.30")

pelanggan1.tampilkanInfo()
print()
pelatih1.tampilkanInfo()
print()
kelas_latihan1.tampilkanInfo()
