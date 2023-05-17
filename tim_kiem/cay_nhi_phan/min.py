from cautrucdulieuvagiaithuat.tim_kiem.cay_nhi_phan.cay_nhi_phan import Cay

def min(root):
    if (root):
        if root.trai == None:
            print("Giá trị nhỏ nhất là:", root.data)
        else: min(root.trai)

if __name__ == '__main__':
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
    min(root)