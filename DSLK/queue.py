# Cách 1: cài đặt Queue bằng mảng Array
class QueueArr:

    def __init__(self):             # Khởi tạo một mảng động, rỗng
        self.arr = []

    def is_empty(self):             # Phương thức is_empty => kiểm tra xem hàng đợi có trống hay không
        return self.arr == []

    def enqueue(self, element):     # Phương thức enqueue => Thêm một phần tử vào cuối hàng đợi
        self.arr.append(element)

    def dequeue(self):              # Phương thức dequeue => Lấy và loại bỏ phần tử đầu tiên ra khỏi hàng đợi
        if self.is_empty():         # nếu hàng đợi rỗng
            return None             # thì trả về None
        else:                       # nếu hàng đợi không rỗng
            return self.arr.pop(0)  # thì lấy ra và xóa

    def size(self):                 # Phương thức size => trả về số lượng phần thử trong hàng đợi
        return len(self.arr)


# Cách 2: Cài đặt hàng đợi dùng danh sách liên kết Linked List

class Node:     # lớp Node để đại diện cho một nút trong hàng đợi
    def __init__(self, data=None):
        self.data = data            # Thuộc tính data => lưu trữ giá trị của nút
        self.next = None            # Thuộc tính next => lưu trữ vị trí tiếp theo của nút trong hàng đợi


class QueueLinkList:        # Quản lý hàng đợi
    def __init__(self):
        self.head = None    # Thuộc tính head => trỏ đến phần tử đầu tiên
        self.tail = None    # Thuộc tính tail => trỏ đến phần tử cuối cùng
        self.size = 0       # Thuộc tính size => là số lượng phần tử trong danh sách hàng đợi

    def is_empty(self):     # Phương thức is_empty => kiểm tra xem hàng đợi có còn trống hay không
        return self.head is None

    def enqueue(self, data):    # Phương thức enqueue => thêm một phần tử vào cuối hàng đợi
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.size += 1

    def dequeue(self):         # Phương thức dequeue => Lấy và xóa bỏ phần thử đầu tiên ra khỏi hàng đợi
        if self.head is None:               # nếu head = None => hàng đợi rỗng
            return None                     # => trả về None
        data = self.head.data
        self.head = self.head.next          # cập nhật next để trỏ tới nút kế tiếp
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data

    def __len__(self):          # Thuộc tính len => trả về số lượng phần tử trong hàng đợi
        return self.size
