# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):  # fungsi untuk menghitung a pangkat n (a^n)

    # Base case
    if n == 0:  # jika pangkat 0
        return 1  # hasilnya selalu 1 → hentikan rekursi

    # Recursive case
    return a * pangkat(a, n - 1)
    # a dikali hasil a pangkat (n-1)
    # di sinilah fungsi memanggil dirinya sendiri (rekursi)


print(pangkat(2, 4))  # memanggil fungsi: 2^4
