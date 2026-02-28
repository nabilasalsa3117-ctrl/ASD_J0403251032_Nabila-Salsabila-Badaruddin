# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ======================================
# materi rekursif : faktorial
# ======================================

def faktorial(n):  # mendefinisikan fungsi bernama faktorial dengan parameter n
    # base case
    if n == 0:  # jika n sama dengan 0 (kasus paling dasar)
        return 1  # faktorial 0 adalah 1, hentikan rekursi

    # n dikali faktorial dari (n-1), di sinilah rekursi terjadi
    return n*faktorial(n-1)


print("hasil faktorial : ", faktorial(10))
# memanggil fungsi faktorial dengan n = 10 lalu mencetak hasilnya
