bwh = int(input("Masukkan nilai batas bawah : "))
ats = int(input("Masukkan nilai batas atas : "))
jumlah = 0

if bwh and ats < 0:
  print("Batas bawah dan atas yang dimasukkan tidak boleh Nol")
else:
  for i in range(bwh, ats):
    if i%2!=0:
      jumlah +=i
      print (i)

print("Total :",jumlah)