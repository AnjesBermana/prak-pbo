def lukelLingkaran():
  phi =3.14
  r = int(input("Masukkan nilai jari-jari lingkaran : "))
  
  if r<0:
    print("\nNilai jari-jari lingkaran tidak boleh negatif")
  else:
    luas = phi*r*r
    keliling = 2*phi*r
    print("\nLuas lingkaran = ",luas)
    print("Keliling lingkaran = ",keliling)

lukelLingkaran()