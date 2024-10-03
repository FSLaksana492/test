# Fungsi untuk menghasilkan barisan aritmatika
def aritmatika(start, jumlah, beda):
    barisan = []
    for i in range(jumlah):
        elemen = start + i * beda
        barisan.append(elemen)
    return barisan

# Input
start = 2  # nilai awal barisan
jumlah = 7  # jumlah elemen yang ingin dihasilkan
beda = 3    # beda antar elemen

# Menghasilkan barisan
hasil = aritmatika(start, jumlah, beda)

# Menampilkan hasil
print(hasil)