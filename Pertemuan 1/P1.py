# Praktikum 1 : konsep ADT dan file handling
# latihan dasar 1 : mmembaca seluruh isi file
# ===============================================
# membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print("===Hasil Read===")
print("Tipe data :", type(isi_file))
print("jumlah karakter :", len(isi_file))
print("jumlah baris :", isi_file.count("\n"))

# membaca file per baris
print("===membaca file per baris")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        # Menghilangkan baris baru, supaya data yang terambil tidak ada tambahan karakter (new line)
        baris = baris.strip()
        print("baris ke-", jumlah_baris)
        print("isinya : ", baris)

# membaca data satu per satu
jum_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for lines in file:
        jum_baris += 1
        lines = lines.strip()
        nim, nama, nilai = lines.split(",")
        print("baris ke-", jum_baris)
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

# memasukkan data kedalam list
data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        nim, nama, nilai = line.split(",")
        data_list.append([nim, nama, int(nilai)])
print(data_list)

print('===jumlah recrd dalam list===')
print("jumlah record :", len(data_list))

print("===menampilkan data record tertentu===")
nomor = int(input("nomor :"))
print("isi data :", data_list[nomor - 1])

# Latihan dasar 4
data_dict = {}
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for bar in file:
        bar = bar.strip()
        nim, nama, nilai = line.split(",")

        # simpan data mahasiswa dalam dictionary
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }

print("=== Data Mahasiswa Dalam Dictionary ===")
print(data_dict)
