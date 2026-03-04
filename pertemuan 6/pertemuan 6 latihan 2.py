# =======================================
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# =======================================

'''
1. Lengkapi kondisi agar menjadi sorting ascending.
'''


def insertion_sort1(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:   # kondisi ascending
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key   # tempatkan key di posisi yang benar

    return data


print(insertion_sort1([5, 2, 9, 1, 3]))

'''
2. Ubah agar menjadi descending.
'''


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Ubah kondisi di sini
        while j >= 0 and data[j] < key:   # kondisi descending
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


print(insertion_sort([5, 2, 9, 1, 3]))
