class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("list is empty")
            return

        print("circular linked list traversal:")
        temp = self.head
        print(temp.data, end="->")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end="->")
            temp = temp.next

        print("...(back to head)")

    def search(self, key):
        if self.head is None:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False


cll = CircularLinkedList()
cll.insert(3)
cll.insert(7)
cll.insert(12)
cll.insert(19)
cll.insert(25)

print("elemen dalam circular linked list :")
cll.display()

el = int(input("masukkan elemen yang ingin dicari: "))
cll.search(el)

if cll.search(el):
    print(f"elemen {el} ditemukan dalam circular linked list")
else:
    print("not found")
