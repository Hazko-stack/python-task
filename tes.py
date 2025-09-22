# Soal 1
A1 = int(input("Angka pertama: "))
A2 = int(input("Angka kedua: "))
A3 = int(input("Angka ketiga: "))

if A1 >= A2 and A1 >= A3:
    max_val = A1
elif A2 >= A1 and A2 >= A3:
    max_val = A2
else:
    max_val = A3

if A1 <= A2 and A1 <= A3:
    min_val = A1
elif A2 <= A1 and A2 <= A3:
    min_val = A2
else:
    min_val = A3

average = (A1 + A2 + A3) / 3

print("Nilai maksimum:", max_val)
print("Nilai minimum:", min_val)
print("Rata-rata:", average)


# Soal 2
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

C = (panjang + lebar) * 2

print("Keliling persegi panjang:", C)


# Soal 3
phi = 3.14
r = float(input("jari-jari: "))

C = 2 * phi * r

print("Keliling lingkaran:", C)

# Soal 4
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))

luas= 0.5 * alas * tinggi

print("Luas segitiga:", luas)

# Soal 5
second = int(input("Masukkan detik: "))

hour = second // 3600
minute = (second % 3600) // 60

print("Jam:", hour)
print("Menit:", minute)

