# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):  # fungsi rekursif untuk menghitung mundur dari n

    if n == 0:  # base case: jika n sudah 0
        print("Selesai")  # tanda bahwa rekursi berhenti
        return  # keluar dari fungsi (mulai proses naik)

    print("Masuk:", n)  # dijalankan SAAT fungsi dipanggil (proses turun)

    countdown(n - 1)  # memanggil fungsi countdown dengan nilai n-1 (rekursi)

    print("Keluar:", n)  # dijalankan SETELAH rekursi selesai (proses naik)


countdown(3)  # memulai rekursi dari nilai 3

# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# Karena rekursi bekerja seperti tumpukan (stack): masuk berurutan, keluar kebalik.
