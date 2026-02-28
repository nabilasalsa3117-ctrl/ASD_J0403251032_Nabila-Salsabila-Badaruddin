# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):   # fungsi rekursif untuk mencari nilai maksimum dalam list
    # data  : list angka
    # index : posisi yang sedang dicek (mulai dari 0)

    # Base case
    if index == len(data) - 1:  # jika index sudah di elemen terakhir
        # kembalikan elemen terakhir sebagai pembanding awal
        return data[index]

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)
    # memanggil fungsi untuk mencari nilai maksimum di sisa list (index berikutnya)

    if data[index] > maks_sisa:  # jika elemen saat ini lebih besar dari maksimum sisa
        return data[index]  # elemen saat ini adalah nilai maksimum
    else:
        return maks_sisa   # jika tidak, maksimum tetap dari sisa list


angka = [3, 7, 2, 9, 5]    # list angka yang akan dicari nilai maksimumnya
print("Nilai maksimum:", cari_maks(angka))
# memanggil fungsi cari_maks dan mencetak hasilnya
