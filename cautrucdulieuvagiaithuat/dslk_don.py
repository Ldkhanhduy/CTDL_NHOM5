class Node:
    def __init__(self, data):
        self.data = data  # Dữ liệu
        self.next = None  # Gán cho con trỏ tiếp theo là None
#Đối tượng Linkedlist gồm các Node
class LinkedList:
    # Gán cho con trỏ là None
    def __init__(self):
        self.head = None
    # In dữ liệu của Node bắt đầu từ con trỏ đầu tiên
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
# Chạy trương trình
if __name__ == '__main__':
    # Danh sách liên kết rỗng
    llist = LinkedList()
    llist.head = Node("Danh") # Gán cho con trỏ đầu có dữ liệu là "Danh"
    second = Node("sách liên kết") # Nút thứ hai có dữ liệu là "sách liên kết"
    third = Node("Nhóm 3") # Nút thứ ba có dữ liệu là "Nhóm 3"
    llist.head.next = second  # Liên kết nút 1 với 2
    second.next = third  # Liên kết 2 với 3
    llist.printList() # In dữ liệu của từ nút của danh sách liên kết
