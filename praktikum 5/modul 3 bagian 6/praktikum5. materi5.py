# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # fungsi membentuk string biner panjang n
    # batas  : jumlah maksimum angka '1' yang boleh muncul
    # hasil  : kombinasi sementara
    # jumlah_1 : menghitung berapa '1' yang sudah dipakai

    # Pruning: jika jumlah_1 sudah melewati batas, hentikan cabang ini
    if jumlah_1 > batas:          # kalau jumlah '1' kebanyakan
        return                    # stop, tidak perlu lanjut (hemat waktu)

    # Base case
    if len(hasil) == n:           # jika panjang string sudah n
        print(hasil)              # cetak kombinasi valid
        return                    # hentikan cabang ini

    # Pilih '0'
    # tambahkan '0', jumlah_1 tidak berubah
    biner_batas(n, batas, hasil + "0", jumlah_1)
    # Pilih '1'
    # tambahkan '1', jumlah_1 bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


biner_batas(4, 2)   # panjang biner 4, maksimal 2 angka '1'
