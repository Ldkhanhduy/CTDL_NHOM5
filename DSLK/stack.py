# Mã nguồn python về thuật toán ngăn xếp(Stack)
# Cách 1: Cài đặt stack dùng mảng Array

class StackArray:

    def __init__(self):
        self.stack = []             # Thuộc tính stack để lưu trữ các phần tử trong ngăn xếp dưới dạng một mảng

    def push(self, data):           # Phương thức push được sử dụng để thêm phần tử vào đỉnh của ngăn xếp
        self.stack.append(data)     # bằng phương thức append(có sẵn của mảng)

    def pop(self):                  # Phương thức pop được sử dụng để lấy ra phần tử trên cùng ra khỏi ngăn xếp
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):                 # Phương thức peek được sử dụng để xem giá trị của phần tử trên cùng của ngăn xếp
        if not self.is_empty():     # mà không xóa nó bằng cách truy cập vào phần tử cuối cùng của mảng
            return self.stack[-1]
        else:
            return None

    def is_empty(self):             # Phương thức is_empty được sử dụng để kiểm tra xem ngăn xếp có rỗng hay không
        return len(self.stack) == 0 # bằng cách kiểm tra độ dài của màng (len(stack) = 0 => mãng rỗng)


# Cách 2: Cài đặt stack dùng danh sách liên kết đơn Linked List

class Node:     # Sử dụng lớp Node để đại diện cho một nút trong ngắn xếp

    def __init__(self, data):
        self.data = data    # Thuộc tính data lưu trữ giá trị của nút
        self.next = None    # Thuộc tính next lưu trữ vị trí tiếp theo của nút trong ngăn xếp


class StackLinkedList:    # Quản lý ngăn xếp
    def __init__(self):
        self.top = None     # Thuộc tính top để lưu trữ nút trên cùng trong ngăn xếp

    def push(self, data):   # Phương thức push được sử dụng để thêm một nút mới vào đỉnh của ngăn xếp, bằng cách
        new_node = Node(data)           # tạo một nút mới với giá trị truyền vào
        new_node.next = self.top        # và đặt nút này làm nút đầu tiên trong ngăn xếp
        self.top = new_node

    def pop(self):      # Phương thức pop được sử dụng để lấy phần tử trên cùng ra khỏi ngăn xếp, bằng cách
        if self.top is None:
            return None                 # trả về giá trị nút trên cùng
        else:
            popped_node = self.top
            self.top = self.top.next    # và cập nhật top để trỏ tới nút tiếp theo trong danh sách
            popped_node.next = None
            return popped_node.data

    def peek(self):  # Phương thức peek được sử dụng để xem giá trị của phần tử trên cùng của ngăn xếp mà không xóa nó
        if self.top is None:
            return None
        else:
            return self.top.data