# =======================================
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# =======================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = key

    return data


'''
1. Mengapa perulangan dimulai dari indeks 1?
jawab = 
Karena:
>Elemen pertama (index 0) dianggap sudah “terurut”
>Kita mulai membandingkan dari elemen kedua
Bagian kiri dianggap sudah rapi, lalu kita sisipkan elemen berikutnya ke posisi yang benar.

2. Apa fungsi variabel key?
jawab = key adalah nilai yang sedang ingin kita tempatkan pada posisi yang benar.

3. Mengapa digunakan while, bukan for?
jawab = 
Karena:
Kita tidak tahu berapa kali harus mundur
Perulangan berhenti saat:
sudah di awal list (j < 0) atau ketemu angka yang lebih kecil dari key
while cocok karena:
Berhenti berdasarkan kondisi, bukan jumlah langkah tetap.
Kalau pakai for, jadi kurang fleksibel.

4. Operasi apa yang terjadi di dalam while?
jawab =
Di dalam while terjadi perbandingan dan pergeseran elemen untuk memberi ruang bagi key.
'''
