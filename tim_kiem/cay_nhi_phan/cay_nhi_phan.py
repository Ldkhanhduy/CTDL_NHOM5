class Cay: #Tạo cây
    def __init__(self, data):
        self.data = data #dữ liệu của khóa
        self.trai = None #con trỏ trái
        self.phai = None #con trỏ phải

def tim(so, root,i): #Tìm kiếm một số trong cây
    if (root):
        if so == root.data:
            print("Nằm ở bậc", i) #Số cần tìm nằm ở gốc
        else:
            if so < root.data: #số cần tìm nhỏ hơn khóa tại con trỏ đang đứng
                i += 1
                print("Trái")
                tim(so, root.trai,i)
            else: #số cần tìm lớn hơn khóa tại con trỏ đang đứng
                i += 1
                print("Phải")
                tim(so, root.phai,i)
    else: print("Không tìm thấy") #số cần tìm không có trong cây

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
    tim(x, root, 1) #khi tìm sẽ in ra màn hình đường đi của thuật toán và chỉ ra tầng của số cần tìm
