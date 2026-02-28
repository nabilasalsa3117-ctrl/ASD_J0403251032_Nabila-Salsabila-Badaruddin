# ======================================
# nama : Nabila salsabila badaruddin
# nim : J0403251032
# kelas : B2
# ======================================
# materi rekursif : menjumlahkan elemen list
# ======================================


def jumlah_list(data, index=0):  # fungsi untuk menjumlahkan isi list, index mulai dari 0
    if index == len(data):       # base case: jika index sudah mencapai panjang list
        return 0                 # tidak ada lagi elemen → kembalikan 0

    return data[index] + jumlah_list(data, index+1)
    # ambil elemen saat ini + hasil penjumlahan elemen berikutnya (rekursif)


print(jumlah_list([2, 3, 4]))   # memanggil fungsi dengan list [2, 3, 4]
