import math

class Bentuk:
    def hitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, jari):
        self.jari = jari

    def hitungLuas(self):
        return math.pi * self.jari ** 2

persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi : {persegi.hitungLuas()}")
print(f"Luas Lingkaran : {lingkaran.hitungLuas()}")