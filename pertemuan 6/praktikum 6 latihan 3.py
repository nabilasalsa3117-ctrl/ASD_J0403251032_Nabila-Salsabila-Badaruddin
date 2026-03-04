# =======================================
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# =======================================

'''
Buat program dengan menggunakan algoritma insertion sort
Tracing dengan data = [5, 2, 4, 6, 1, 3]

1. Tuliskan isi list setelah iterasi i = 1.
[2, 5, 4, 6, 1, 3]
2. Tuliskan isi list setelah iterasi i = 3.
[2, 4, 5, 6, 1, 3]
3. Berapa kali pergeseran terjadi pada iterasi i = 4?
4 kali
'''


def insertion_sort(data):
    print("Data awal:", data)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"\nLangkah ke-{i}")
        print("Key =", key)

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            print("Geser:", data)

        data[j + 1] = key
        print("Sisipkan key:", data)

    return data


data = [5, 2, 4, 6, 1, 3]
hasil = insertion_sort(data)
print("\nHasil akhir:", hasil)
