def hapusPilarMistik(arr, n, pos):
    # Salin array untuk menghindari modifikasi langsung
    original_arr = arr[:]
    
    if pos < 0 or pos >= n:
        return arr, n, 0  # Posisi tidak valid

    # Hitung array setelah penghapusan
    new_arr = arr[:pos] + arr[pos+1:]
    if len(new_arr) == 0:
        return arr, n, 0  # Tidak ada elemen tersisa
    
    # Hitung rata-rata energi setelah penghapusan
    rata_rata = sum(new_arr) / len(new_arr)

    if arr[pos] < rata_rata:
        # Elemen harus dihapus dan geser sisanya
        jumlah_pergeseran = n - pos - 1
        return new_arr, len(new_arr), jumlah_pergeseran
    else:
        return arr, n, 0

# Contoh penggunaan
# Contoh 1
arr = [10, 30, 20, 40]
n = 4
pos = 1
hasil = hapusPilarMistik(arr, n, pos)
print("Contoh 1:")
print("Pilar setelah proses:", hasil[0])
print("Panjang baru:", hasil[1])
print("Jumlah pergeseran:", hasil[2])
#conroh 2
arr = [50, 20, 30, 40]
n = 4
pos = 1
hasil = hapusPilarMistik(arr, n, pos)
print("\nContoh 2:")
print("Pilar setelah proses:", hasil[0])
print("Panjang baru:", hasil[1])
print("Jumlah pergeseran:",hasil[2])
#input tambahanarr2 = [50, 20, 30, 40]
arr = [15, 25, 35, 45]
pos = 2
hasil = hapusPilarMistik(arr, n, pos)
print("\ninputtambahan:")
print("Pilar setelah proses:", hasil[0])
print("Jumlah pergeseran:",hasil[2])
