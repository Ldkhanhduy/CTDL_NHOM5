class Node:

    def __init__(self, stt, diem):
        self.stt = stt
        self.diem = diem
        self.next = None
        self.prev = None

class Link:

    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        temp1 = self.tail
        while (temp):
            print(temp.stt, temp.diem)
            temp = temp.next
        else:
            while (temp1):
                print(temp1.stt, temp1.diem)
                temp1 = temp1.prev

if __name__ == '__main__':
    dll = Link()
    dll.head = Node(1,10)
    second = Node(2,9)
    third = Node(3,10)
    fourth = Node(4,8)
    dll.tail = Node(5,9)
    dll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = dll.tail
    dll.tail.prev = fourth
    fourth.prev = third
    third.prev = second
    second.prev = dll.head
    dll.printList()