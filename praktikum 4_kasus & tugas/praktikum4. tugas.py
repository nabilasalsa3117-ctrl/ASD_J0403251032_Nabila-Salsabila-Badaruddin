# ========IDENTITAS MAHASISWA===================
# NAMA : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : P2
# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None


class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, no, nama, servis):
        node_baru = Node(no, nama, servis)   # membuat node baru

        if self.front is None:   # jika antrian masih kosong
            self.front = node_baru  # front menunjuk node baru
            self.rear = node_baru   # rear juga menunjuk node baru
        else:
            self.rear.next = node_baru  # node terakhir menunjuk node baru
            self.rear = node_baru  # rear pindah ke node baru

    def dequeue(self):
        if self.front is None:   # jika antrian kosong
            print("Antrian kosong!")
            return

        temp = self.front    # simpan node terdepan sementara
        self.front = self.front.next  # front pindah ke node berikutnya

        if self.front is None:  # jika antrian jadi kosong
            self.rear = None    # rear juga dikosongkan

        print("Melayani pelanggan:")
        print("No:", temp.no)
        print("Nama:", temp.nama)
        print("Servis:", temp.servis)

    def tampilkan(self):
        if self.front is None:   # jika antrian kosong
            print("Antrian kosong!")
            return

        current = self.front  # mulai dari depan
        print("=== DAFTAR ANTRIAN ===")
        while current is not None:  # traversal linked list
            print("No:", current.no,
                  "| Nama:", current.nama,
                  "| Servis:", current.servis)
            current = current.next  # pindah ke node berikutnya


def main():
    q = QueueBengkel()
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama      : ")
            servis = input("Servis    : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
