# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ======================================
# materi rekursif : call stack
# tracing bilangan (masuk keluar)
# input 3
# 3-2-1 | 1-2-3
# ======================================

def hitung(n):  # mendefinisikan fungsi hitung dengan parameter n
    # base case
    if n == 0:  # jika n sudah 0
        print("selesai")  # tanda bahwa rekursi berhenti
        return            # keluar dari fungsi (stop rekursi)

    print("masuk :", n)  # dijalankan SAAT fungsi dipanggil (turun)
    hitung(n-1)         # memanggil diri sendiri dengan n-1 (rekursi)
    print("keluar", n)  # dijalankan SAAT fungsi selesai (naik)


hitung(5)  # memulai rekursi dari n = 5
