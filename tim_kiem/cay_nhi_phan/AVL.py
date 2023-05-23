# Định nghĩa lớp Node để biểu diễn nút trong cây AVL
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Lớp cây AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # Phương thức để lấy chiều cao của một nút
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # Phương thức để cập nhật chiều cao của một nút
    def update_height(self, node):
        if node is None:
            return 0
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # Phương thức để tính chỉ số cân bằng (balance factor) của một nút
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Phương thức để xoay sang trái tại nút x
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Thực hiện xoay
        y.left = x
        x.right = T2

        # Cập nhật chiều cao
        self.update_height(x)
        self.update_height(y)

        return y

    # Phương thức để xoay sang phải tại nút y
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Thực hiện xoay
        x.right = y
        y.left = T2

        # Cập nhật chiều cao
        self.update_height(y)
        self.update_height(x)

        return x

    # Phương thức chèn một khóa vào cây AVL
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        # Thực hiện chèn như trong cây nhị phân tìm kiếm
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # Cập nhật chiều cao của nút cha
        self.update_height(root)

        # Kiểm tra chỉ số cân bằng và thực hiện cân bằng lại nếu cần
        balance = self.get_balance(root)

        # Trường hợp 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Trường hợp 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Trường hợp 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Trường hợp 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

if __name__ == '__main__':
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    
