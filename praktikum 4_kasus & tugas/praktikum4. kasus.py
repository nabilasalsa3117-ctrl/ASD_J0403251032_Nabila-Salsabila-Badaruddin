# ======================================================
# NAMA : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : TPL B2
# ======================================================

# ======================================================
# STUDI KASUS : sistem antrian layanan akademik
# implementasi queue
# stack ==> FRONT -> C -> B -> A -> None
# Queue ==> Front -> A -> B -> C ->Rear
# enququ = memindahkan pointer rear/tail (nambah data dari belakang)
# dequeu = memindahkan pointer head/front (hapus data dari depan)

# sebagai linked list
class Node:
    def __init__(self, nim, nama):
        self.nim = nim  # menyimpan Nim Mahasiswa
        self.nama = nama  # menyimpan Nama Mahasiswa
        self.next = None  # pointer ke node berikutnya

# untuk queue


class queueAkademik:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        # ketiks queue kosong maka front = rearv= none
        return self.head is None

    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        # kalau data kosong
        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return

        # kalau data udah adaa
        self.tail.next = nodeBaru
        self.tail = nodeBaru

    def dequue(self):
        if self.is_empty():
            print("antrian kosong, tidak asa mahasiswa dilayani")
            return None

        node_dilayani = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return node_dilayani

    def tampilkan(self):
        print("daftar antrian mahasiswa (head -> tail) :")
        current = self.head
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} {current.nama}")
            current = current.next
            no += 1

# program utama


def main():
    q = queueAkademik()

    while True:
        print("=============sistem antrian akademik===============")
        print("1. tambah mahasiswa")
        print("2. layani mahasiswa")
        print("3. lihat antrian")
        print("4. keluar")

        pilihan = input("plih menu:").strip()

        if pilihan == "1":
            nim = input("masukkan nim :").strip()
            nama = input("masukkan nama :").strip()

            q.enqueue(nim, nama)
            print("mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequue()
            print(f"mahasiswa dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("program selesai")
            break

        else:
            print("pilihan tidak valid")


if __name__ == "__main__":
    main()
