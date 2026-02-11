class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def marge(self, list2):
        if self.head is None:
            self.head = list2.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head


il = LinkedList()
il.append(1)
il.append(3)
il.append(5)
il.append(7)
print("linked list 1:")
il.print_list()

il_2 = LinkedList()
il_2.append(2)
il_2.append(4)
il_2.append(6)
print("linked list 2:")
il_2.print_list()

print("linked list setelah digabungkan:")
il.marge(il_2)
il.print_list()

print("===================")

print("contoh tampilan #2")
il_3 = LinkedList()
il_3.append(5)
il_3.append(15)
il_3.append(25)

il_4 = LinkedList()

print("linked list setelah digabungkan:")
il_3.marge(il_4)
il_3.print_list()
