import pygame
import random

LEBAR_LAYAR = 800
TINGGI_LAYAR = 600
UKURAN_KOTAK = 20
KECEPATAN = 12
ATAS = (0, -1)
BAWAH = (0, 1)
KIRI = (-1, 0)
KANAN = (1, 0)
LEBAR_KOTAK = LEBAR_LAYAR // UKURAN_KOTAK
TINGGI_KOTAK = TINGGI_LAYAR // UKURAN_KOTAK

class Ular:
    def __init__(self):
        self.ukuran = 1
        self.posisi = [((LEBAR_LAYAR // 2), (TINGGI_LAYAR // 2))]
        self.arah = random.choice([ATAS, BAWAH, KIRI, KANAN])
        self.warna = (0, 255, 0)

    def get_head_pos(self):
        return self.posisi[0]

    def ganti_arah(self, arah_baru):
        # Fungsi untuk mengubah arah ular
        if self.ukuran > 1 and (arah_baru[0] * -1, arah_baru[1] * -1) == self.arah:
            return
        else:
            self.arah = arah_baru

    def move(self):
        # Fungsi untuk menggerakkan ular
        kepala_sekarang = self.get_head_pos()
        x, y = self.arah
        kepala_baru = (((kepala_sekarang[0] + (x * UKURAN_KOTAK)) % LEBAR_LAYAR), (kepala_sekarang[1] + (y * UKURAN_KOTAK)) % TINGGI_LAYAR)
        if len(self.posisi) > 2 and kepala_baru in self.posisi[2:]:
            self.reset()
        else:
            self.posisi.insert(0, kepala_baru)
            if len(self.posisi) > self.ukuran:
                self.posisi.pop()

    def reset(self):
        # Fungsi untuk mereset game jika ular menabrak dirinya sendiri
        self.ukuran = 1
        self.posisi = [((LEBAR_LAYAR // 2), (TINGGI_LAYAR // 2))]
        self.arah = random.choice([ATAS, BAWAH, KIRI, KANAN])
        self.warna = (0, 255, 0)

    def draw_snake(self, layar):
        # Fungsi untuk menggambar ular di layar
        for p in self.posisi:
            kotak = pygame.Rect((p[0], p[1]), (UKURAN_KOTAK, UKURAN_KOTAK))
            pygame.draw.rect(layar, self.warna, kotak)
            pygame.draw.rect(layar, (93, 216, 228), kotak, 1)

    def handle_keys(self):
        # Fungsi untuk mengubah arah ular
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_w]:
            self.ganti_arah(ATAS)
        elif tombol[pygame.K_s]:
            self.ganti_arah(BAWAH)
        elif tombol[pygame.K_a]:
            self.ganti_arah(KIRI)
        elif tombol[pygame.K_d]:
            self.ganti_arah(KANAN)

class Makanan:
    def __init__(self):
        self.posisi = (0, 0)
        self.warna = (255, 0, 0)
        self.acak_posisi()

    def acak_posisi(self):
        # Fungsi untuk mengacak posisi makanan di layar
        self.posisi = (random.randint(0, LEBAR_KOTAK - 1) * UKURAN_KOTAK, random.randint(0, TINGGI_KOTAK - 1) * UKURAN_KOTAK)

    def draw(self, layar):
        # Fungsi untuk menggambar makanan di layar
        kotak = pygame.Rect((self.posisi[0], self.posisi[1]), (UKURAN_KOTAK, UKURAN_KOTAK))
        pygame.draw.rect(layar, self.warna, kotak)

    def ubah_warna(self):
        # Fungsi untuk mengubah warna makanan secara acak
        warna_acak = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.warna = warna_acak

class Skorboard:
    def __init__(self):
        self.skor = 0
        self.font = pygame.font.SysFont(None, 30)

    def tambah_skor(self):
        # Fungsi untuk menambah skor setiap kali ular makan makanan
        self.skor += 1

    def tampilkan_skor(self, layar):
        # Fungsi untuk menampilkan skor di layar
        teks_skor = self.font.render(f"Skor : {self.skor}", True, (255, 255, 255))
        layar.blit(teks_skor, (LEBAR_LAYAR - 90, 10))

class GameUlar:
    def __init__(self):
        pygame.init()
        self.layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
        self.ular = Ular()
        self.makanan = Makanan()
        self.skorboard = Skorboard()

    def mainkan_langkah(self):
        # Fungs untuk menjalankan langkah permainan
        self.ular.handle_keys()
        self.ular.move()
        self.cek_tabrakan()
        self.update_ui()
        self.clock.tick(KECEPATAN)

    def cek_tabrakan(self):
        # Fungsi untuk memeriksa ular menabrak makanan atau tidak
        if self.ular.get_head_pos() == self.makanan.posisi:
            self.ular.ukuran += 1
            self.makanan.acak_posisi()
            self.makanan.ubah_warna()
            self.ular.warna = self.makanan.warna
            self.skorboard.tambah_skor()

    def update_ui(self):
        self.layar.fill((0, 0, 0))
        self.ular.draw_snake(self.layar)
        self.makanan.draw(self.layar)
        self.skorboard.tampilkan_skor(self.layar)
        pygame.display.flip()

    def run_game(self):
        # Fungsi utama menjalankan game
        pygame.display.set_caption('Game Ular Berkotak')
        self.clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.mainkan_langkah()
        pygame.quit()

if __name__ == "__main__":
    game = GameUlar()
    game.run_game()