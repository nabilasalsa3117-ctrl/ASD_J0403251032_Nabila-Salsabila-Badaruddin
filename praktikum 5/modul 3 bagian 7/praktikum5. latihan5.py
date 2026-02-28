# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):      # fungsi rekursif untuk membuat semua kemungkinan PIN
    # panjang : jumlah digit PIN
    # hasil   : string sementara (PIN yang sedang dibentuk)

    if len(hasil) == panjang:   # base case: jika panjang PIN sudah sesuai
        print("PIN:", hasil)  # cetak satu PIN lengkap
        return  # hentikan cabang rekursi ini

    for angka in ["0", "1", "2"]:     # loop pilihan digit yang boleh dipakai
        buat_pin(panjang, hasil + angka)
        # pilih satu digit, tambahkan ke hasil, lalu lanjutkan rekursi


buat_pin(3)   # mulai membentuk PIN dengan panjang 3 digit

# Bagaimana cara mencegah angka yang sama muncul berulang?
# kita harus “mengingat” angka yang sudah dipakai, lalu tidak memilihnya lagi. Angka yang sama dicegah muncul berulang dengan memeriksa apakah angka tersebut sudah terdapat pada hasil sementara sebelum melanjutkan rekursi, sehingga setiap digit hanya digunakan satu kali dalam satu kombinasi.
