# pertemuan 2

nama_file = "data_mahasiswa.txt"

# fungsi untuk membaca data mahasiswa


def baca_data_mahasiswa(nama_file):
    data_dict = {}
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            parts = baris.split(",")

            if len(parts) != 3:
                continue
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)
            data_dict[nim] = {"nama": nama, "nilai": nilai_int}
            nim, nama, nilai = baris.split(",")

        # simpan data mahasiswa dalam dictionary
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
    print("=== Data Mahasiswa Dalam Dictionary ===")
    return data_dict


buka_data = baca_data_mahasiswa(nama_file)
print(len(buka_data))

# menampilkan data


def tampil_data(data_dict):
    if len(data_dict) == 0:
        print("data kosong")
        return

    # membuat tampilan tabel agar indentasinya rapi
    print("====Daftar  Mahasiswa====")
    print(f"{'NIM': <10} | {'nama': <12} | {"nilai": >5}")
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")


tampil_data(buka_data)

# mencari data


def cari_data(data_dict):
    # mencari data mahasiswa berdasarkan NIM
    nim_cari = input("masukkan NIM mahasiswa :").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]['nilai']

        print("==== Data Mahasiswa DItemukan ====")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("data tidak ditemukan")


cari_data(buka_data)

# update nilai


def update_nilai(data_dict):
    nim = input("masukkan nim mahasiswa :")

    if nim not in data_dict:
        print("NIMM tidak ditemukan,update dbatalkan")
        return
    try:
        nilai_baru = int(input("masukkan nilai baru (0-100) :"))
    except ValueError:
        print("nilai harus berupa angka")

    if nilai_baru < 0 or nilai_baru > 100:
        print("nilai harus antara 0 sampai 100")

    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]['nilai'] = nilai_baru

    print(
        f"update berhasil, nilai {nim} berubah dari {nilai_lama} manjadi {nilai_baru}")


update_nilai(buka_data)

# menyimpan perubahan data ke file


def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama}'{nilai}\n")


simpan_data(nama_file, buka_data)
print("data berhasil disimpan")


def main():  # main menandakan fungsi prioritas yang akan secara otomatis selalu dibuka lebih awal
    buka_data = baca_data_mahasiswa(nama_file)


while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tampilkan semua data")
    print("2. Cari data berdasarkan NIM")
    print("3. Update nilai mahasiswa")
    print("4. Simpan data ke file")
    print("0. keluar")

    pilihan = input("pilihan menu :")

    if pilihan == "1":
        tampil_data(buka_data)
    elif pilihan == "2":
        cari_data(buka_data)
    elif pilihan == "3":
        update_nilai(buka_data)
    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
        print("data berhasil disimpan")
    else:
        print("program selesai")
        break

if __name__ == "__main__":
    main()
