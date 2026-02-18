# ==========================================
# Implementasi Dasar : Node pada linked list
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : B2
# ==========================================

# instantiasi itu adalah variabel yang menyambungkan variabel dengan class supaya def didalam class bisa di akses
# konstruktor itu otomatis terpanggil saat class dipanggil
# dalam class ini bisa banyak def ditaruh sesuai listnya mau diapain
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai
        self.next = None  # pointer ke node berikutnya


# 1) membuat node(data) satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) menghungkan node : A -> B -> C -> None (linked list)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

# 3) menentukan node pertama (head)
head = nodeA

# Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)  # menampilkan data satu per satu (pada node saat ini)
    current = current.next  # memindahkan ke node selanjutnya

# ======================================================
# Implementasi dasar : linked list + insert awal
# class untuk menyimpan fungsi operasional pada nodes

# node baru, nd ada hubungannya sama A,B,C

# contoh implementasi stack


class linkedList:
    def __init__(self):
        self.head = None  # awalnya kosong

    def insert_awal(self, data):  # push dalam stack
        # taruh node/data baru di AWAL bukan di akhir, paling awal ditaruh paling akhir
        # 1) buat node baru
        nodeBaru = Node(data)  # panggil class node untuk taruh di var data
        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head
        # 3) head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self):  # pop dalam stack
        # program akan membaca node dari head jadi kalau ada data A,B,C tapi kita inisiasikan B jadi head, otomatis A nya nd ditampilkan, jadi seakan akan terhapus padahal tidak ditampilkan ji-_-
        data_terhapus = self.head.data  # pick
        self.head = self.head.next
        print(f"data yang terhapus adalah {data_terhapus}")

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


ll = linkedList()
print("====List Baru====")
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
