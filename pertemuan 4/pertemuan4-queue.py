# ==========================================
# Implementasi Dasar : queue berbasis linked list
# Nama : Nabila Salsabila Badaruddin
# NIM : J0403251032
# Kelas : B2
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai
        self.next = None  # pointer ke node berikutnya

# queue dengan 2 pointer : head dan tail


class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        nodeBaru = Node(data)

        if self.is_empty():
            self.head = nodeBaru
            self.tail = nodeBaru
            return

        # untuk menambah data/node ke next tail yang lama
        self.tail.next = nodeBaru
        self.tail = nodeBaru
        # artinya tail nya sekarang nempel ke node baru

    def dequeue(self):
        # 1)ambil data paling depan
        data_hapus = self.head.data
        # 2)geser head ke data selanjutnya
        self.head = self.head.next
        # 3) jika setelah digeser ternyata none,maka queue kosong, tail juga jadi none
        if self.head is None:
            self.tail = None
        return data_hapus

    def tampilkan(self):
        current = self.head
        print("head", end="-> ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print("tail")


q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
# sampai none
q.dequeue()
q.dequeue()
q.tampilkan()
