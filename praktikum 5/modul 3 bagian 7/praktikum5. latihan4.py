# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):  # fungsi rekursif untuk membentuk kombinasi huruf sepanjang n
    # n     : panjang kombinasi
    # hasil : string sementara yang sedang dibangun

    if len(hasil) == n:  # base case: jika panjang hasil sudah sama dengan n
        print(hasil)  # cetak satu kombinasi yang lengkap
        return  # hentikan cabang rekursi ini

    kombinasi(n, hasil + "A")  # pilih 'A' lalu lanjutkan rekursi
    kombinasi(n, hasil + "B")  # pilih 'B' lalu lanjutkan rekursi


kombinasi(2)  # mulai membentuk kombinasi sepanjang 2

# bagaimana jumlah kombinasi yang dihasilkan.
# Jumlah kombinasi yang dihasilkan adalah 2ⁿ karena pada setiap posisi terdapat dua pilihan karakter dan panjang kombinasi adalah n.
