from abc import ABC, abstractmethod

class Obat:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
        else:
            print("Harga tidak valid")

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
        else:
            print(f"Stok {self.nama} tidak cukup")

    def info(self):
        return f"{self.kode} | {self.nama} | Rp{self.__harga} | Stok: {self.__stok}"


class ObatResep(Obat):
    def __init__(self, kode, nama, harga, stok, nama_dokter):
        super().__init__(kode, nama, harga, stok)
        self.nama_dokter = nama_dokter

    def info(self):
        return super().info() + f" | Resep dari: {self.nama_dokter}"


class ObatBebas(Obat):
    def info(self):
        return super().info() + " | Dijual bebas"


class AlgoritmaPencarian(ABC):
    @abstractmethod
    def cari(self, daftar_obat, kode_target):
        pass


class LinearSearch(AlgoritmaPencarian):
    def cari(self, daftar_obat, kode_target):
        for obat in daftar_obat:
            if obat.kode == kode_target:
                return obat
        return None


class BubbleSortHarga:
    def urutkan(self, daftar_obat):
        n = len(daftar_obat)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if daftar_obat[j].get_harga() > daftar_obat[j + 1].get_harga():
                    daftar_obat[j], daftar_obat[j + 1] = daftar_obat[j + 1], daftar_obat[j]
        return daftar_obat


if __name__ == "__main__":
    daftar_obat = [
        ObatBebas("OB01", "Paracetamol", 5000, 100),
        ObatResep("OR01", "Amoxicillin", 12000, 50, "dr. Ririn")
    ]

    pencarian = LinearSearch()
    hasil = pencarian.cari(daftar_obat, "OR01")
    if hasil:
        print(hasil.info())

    pengurut = BubbleSortHarga()
    for o in pengurut.urutkan(daftar_obat):
        print(o.info())