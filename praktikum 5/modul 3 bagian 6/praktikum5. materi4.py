# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):  # fungsi untuk membentuk string biner sepanjang n
    # hasil menyimpan kombinasi sementara
    # Base case: jika panjang string sudah n
    if len(hasil) == n:   # kalau panjang hasil sudah n karakter
        print(hasil)      # cetak satu kombinasi biner
        return            # hentikan cabang rekursi ini

    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")  # pilih '0', lanjutkan rekursi

    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")  # pilih '1', lanjutkan rekursi


biner(3)  # mulai membentuk biner sepanjang 3
