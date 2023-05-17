class Cay:
    def __init__(self, data):
        self.data = data
        self.trai = None
        self.phai = None

def tim(so, root,i):
    if (root):
        if so == root.data:
            print("Nằm ở bậc", i)
        else:
            if so < root.data:
                i += 1
                print("Trái")
                tim(so, root.trai,i)
            else:
                i += 1
                print("Phải")
                tim(so, root.phai,i)
    else: print("Không tìm thấy")

if __name__ == '__main__':
    print("Cây nhị phân với khóa là số nguyên")
    x = int(input("Nhập số cần tìm:"))
    root = Cay(69)
    root.trai = Cay(24)
    root.phai = Cay(80)
    root.phai.trai = Cay(72)
    root.phai.phai = Cay(91)
    root.phai.phai.phai = Cay(92)
    root.phai.phai.trai = Cay(87)
    root.trai.trai = Cay(20)
    root.trai.phai = Cay(59)
    root.trai.phai.trai = Cay(30)
    root.trai.phai.trai.phai = Cay(40)
    root.trai.phai.trai.trai = Cay(27)
    tim(x, root, 1)
