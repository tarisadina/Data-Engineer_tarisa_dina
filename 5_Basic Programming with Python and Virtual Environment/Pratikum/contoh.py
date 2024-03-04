class Yoga:
    def __init__(self, tingkatKesulitan):
        self._tingkatKesulitan = tingkatKesulitan

    def setNama(self, nama):
        self._nama = nama

    def getNama(self):
        return self._nama

    def setUsia(self, nama):
        self._usia = usia

    def getUsia(self):
        return self._usia

    def identity(self):
        return self._usia + " Informasi " + str(self._idPelanggan) + ":" + self._nama


class Pelatih:
    def __init__(self, nama, spesialis, tahunPengalaman):
        super().__init__(nama, spesialis, tahunPengalaman)
        self.__spesialis = spesialis

    def setNama(self, nama):
        self._nama = nama

    def getNama(self):
        return self._nama

    def identity(self):
        return "Ini Class Pelatih " + "berkaki " + str(self._tahunPengalaman) + ":" + self._nama


class kelasLatihan:
    def __init__(self, jenisLatihan, jadwal):
        super().__init__(nama, jenisLatihan, jadwal)
        self.__jenisLatihan = jenisLatihan

    def setNama(self, nama):
        self._nama = nama

    def getNama(self):
        return self._nama

    def identity(self):
        return "Ini Class Latihan " + "berkaki " + str(self._jadwal) + ":" + self._nama


pelanggan1 = Pelanggan("Tarisa", "21", "01")
pelatih1 = Pelatih("Rafi", "Running", "2011")
latihan1 = kelasLatihan("Lari 5Km", "Senin jam 09.00 - 10.30")

print(str(pelanggan1.identity()))
print(pelatih1.identity())
print(latihan1.identity())

print("Nama Pelanggan:", pelanggan1.getNama())
pelatih1.setNama("Rafi")
print("Nama Pelatih:", pelatih1.getNama())
latihan1.setNama("Lari 5Km")
print("Nama Pelatih:", latihan1.getNama())
