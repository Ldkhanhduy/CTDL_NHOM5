class Node:
    def __init__(self, ten):
        self.ten = ten
        self.contrai = None
        self.ngangphai = None
def inorder(node):
    if (node):
        inorder(node.contrai)
        print(node.ten)
        inorder(node.ngangphai)

if __name__ == '__main__':
    root = Node("Ông")
    con1 = Node("Con 1")
    con2 = Node("Con 2")
    con3 = Node("Con 3")
    chau1 = Node("Cháu 1")
    chau2 = Node("Cháu 2")
    chau3 = Node("Cháu 3")
    chau4 = Node("Cháu 4")
    chau5 = Node("Cháu 5")
    chat1 = Node("Chắt 1")
    chat2 = Node("Chắt 2")
    root.contrai = con1
    con1.contrai = chau1
    con1.ngangphai = con2
    chau1.ngangphai = chau2
    chau2.contrai = chat1
    chat1.ngangphai = chat2
    con2.contrai = chau3
    con2.ngangphai = con3
    chau3.ngangphai = chau4
    chau4.ngangphai = chau5
    inorder(root)