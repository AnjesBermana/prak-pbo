class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        #private
        self.__nim = nim
        self.__nama = nama

        #nonprivate
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim
    
    def set_nim(self, nim):
        self.__nim = nim
    
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def cekprodi(self):
        angka_prodi = int(self.__nim[0])
        if angka_prodi == 1:
            return "Teknik Informatika"
        elif angka_prodi == 2:
            return "Teknik Sipil"
        elif angka_prodi == 3:
            return "Teknik Elektro"
        elif angka_prodi == 4:
            return "Teknik Industri"
        else :
            return "Prodi tidak diketahui"
        
    def get_status_mahasiswa(self):
        if self.isMahasiswa:
            return f"{self.__nama} adalah Mahasiswa"
        else:
            return f"{self.__nama} bukanlah Mahasiswa"
    
    def hitung_semester(self, tahun_sekarang, semester_sekarang):
        tahun_masuk = self.angkatan
        total_semester = (tahun_sekarang - tahun_masuk) * 2
        total_semester += semester_sekarang
        return total_semester

mahasiswa1 = Mahasiswa("123", "Anjes", 2022)
print("NIM : ", mahasiswa1.get_nim())
print("Nama : ", mahasiswa1.get_nama())
print("Angkatan : ", mahasiswa1.angkatan)
print("Prodi : ", mahasiswa1.cekprodi())
print("Status Mahasiswa : ", "Mahasiswa" if mahasiswa1.get_status_mahasiswa() else "Bukan Mahasiswa")
print("Total Semester : ", mahasiswa1.hitung_semester(2024, 2))
print()

mahasiswa2 = Mahasiswa("234", "Andi", 2020)
print("NIM : ", mahasiswa2.get_nim())
print("Nama : ", mahasiswa2.get_nama())
print("Angkatan : ", mahasiswa2.angkatan)
print("Prodi : ", mahasiswa2.cekprodi())
print("Status Mahasiswa : ", "Mahasiswa" if mahasiswa2.get_status_mahasiswa() else "Bukan Mahasiswa")
print("Total Semester : ", mahasiswa2.hitung_semester(2024, 2))