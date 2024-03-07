class Rumah:
    def __init__(self, nama, alamat, kapasitas, harga_per_malam):  # Constructor
        self.nama = nama
        self.alamat = alamat
        self.kapasitas = kapasitas
        self.harga_per_malam = harga_per_malam
        self.status = "Tersedia"

    def info(self):
        return f"{self.nama} berlokasi di {self.alamat}. Kapasitas: {self.kapasitas} orang. Harga per malam: Rp {self.harga_per_malam}. Status: {self.status}"

class BookingRumah:
    def __init__(self):  # Constructor
        self.daftar_rumah = [
            Rumah("Villa Raya", "Jl. Turi Raya No. 123", 8, 1000000),
            Rumah("Rumah Waseboy", "Jl. Pegunungan Hijau No. 45", 6, 750000),
            Rumah("Penginapan Villa Citra", "Jl. Permata Raya No. 78", 4, 500000)
        ]

    def tampilkan_daftar_rumah(self):
        print("Daftar rumah penginapan yang Tersedia:\n")
        for rumah in self.daftar_rumah:
            print(rumah.info())

    def pesan_rumah(self, nama_rumah, jumlah_malam):
        rumah = None
        for r in self.daftar_rumah:
            if r.nama == nama_rumah:
                rumah = r
                break

        if rumah and rumah.status == "Tersedia":
            total_biaya = jumlah_malam * rumah.harga_per_malam
            rumah.status = "Dipesan"
            print(f"Anda telah memesan {rumah.nama} untuk {jumlah_malam} malam. Total biaya: Rp {total_biaya}.")
        elif rumah and rumah.status == "Dipesan":
            print(f"\nMaaf, {rumah.nama} sudah dipesan.")
        else:
            print("Rumah tidak ditemukan atau tidak tersedia.")

    def __del__(self):  # Destructor
        print("\nTerima kasih telah menggunakan layanan pemesanan rumah.")

def pesan_sambutan(func):  # Decorator
    def wrapper(self, *args, **kwargs):
        print("Selamat datang di layanan rumah penginapan \n")
        func(self, *args, **kwargs)
    return wrapper

booking = BookingRumah()
BookingRumah.tampilkan_daftar_rumah = pesan_sambutan(BookingRumah.tampilkan_daftar_rumah)

# Menampilkan daftar rumah yang tersedia
booking.tampilkan_daftar_rumah()

# Memesan rumah
booking.pesan_rumah("Villa Raya", 3)
booking.pesan_rumah("Rumah Waseboy", 2)
booking.pesan_rumah("Penginapan Villa Citra", 4)

# Menampilkan daftar rumah setelah pemesanan
booking.tampilkan_daftar_rumah()

# Mencoba memesan rumah yang tidak ada
booking.pesan_rumah("Rumah Watdelur", 1)

# Memesan rumah yang telah dipesan
booking.pesan_rumah("Penginapan Villa Citra", 3)

del booking