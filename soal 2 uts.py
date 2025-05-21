def cariRelikTerkuat(arr, n):
    nilai_terbesar = 0
    indeks_terkuat = -1

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                count += 1
        nilai_efektif = arr[i] * count
        if nilai_efektif > nilai_terbesar:
            nilai_terbesar = nilai_efektif
            indeks_terkuat = i

    return nilai_terbesar, indeks_terkuat

# Contoh penggunaan
arr = [10, 30, 20, 30, 15]
n = len(arr)
hasil = cariRelikTerkuat(arr, n)

print("Nilai efektif terbesar:", hasil[0])
print("Indeks relik:",hasil[1])

# input tambahan
arr = [5, 10, 5, 15, 5]
n = len(arr)
hasil = cariRelikTerkuat(arr, n)

print("Nilai efektif terbesar:", hasil[0])
print("Indeks relik:",hasil[1])