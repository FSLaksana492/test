def deret(n):
    awal = 2
    selisih = 3
    deret = []

    for i in range(n):
        deret.append(awal + i * selisih)
    
    return deret

N = int(input("Masukkan input: "))

hasil = deret(N)
print(", ".join(map(str, hasil)))