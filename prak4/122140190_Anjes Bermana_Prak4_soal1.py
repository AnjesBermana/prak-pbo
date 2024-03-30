class Hewan:
    def __init__(self, nama, jekel):
        self.nama = nama
        self.jekel = jekel

    def bersuara(self):
        pass

    def makan(self):
        pass

    def minum(self):
        pass

class KUCING(Hewan):
    def bersuara(self):
        print(f"Kucing {self.nama} bersuara : Meong !!")

    def makan(self):
        print(f"Kucing {self.nama} sedang makan : tulang")
    
    def minum(self):
        print(f"Kucing {self.nama} sedang minum air")

class ANJING(Hewan):
    def bersuara(self):
        print(f"Anjing {self.nama} bersuara : Guk Guk !!")

    def makan(self):
        print(f"Anjing {self.nama} sedang makan : tulang")
    
    def minum(self):
        print(f"Anjing {self.nama} sedang minum susu")

hewan1 = KUCING("Kiki", "Betina")
hewan2 = ANJING("Ichi", "Jantan")

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.makan()
hewan1.minum()

hewan2.bersuara()
hewan2.makan()
hewan2.minum()