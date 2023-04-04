import numpy as n
import random as r
from tkinter import *
from tkinter import ttk

#Hàm kiểm tra vị trí đặt quân hậu
def kiemtra(banco,hang,cot): #Kiểm tra phía bên trái hàng đang đứng
    for i in range(cot):
        if banco[hang][i] == 1:
            return False 
    for i,j in zip(range(hang, -1, -1), range(cot, -1, -1)): #Kiểm tra phía bên trái đường chéo cộng
        if banco[i][j] == 1:
            return False
    for i, j in zip(range(hang, 8, 1), range(cot, -1, -1)): #Kiểm tra phía bên trái đường chéo trừ
        if banco[i][j] == 1:
            return False
    return True #Nếu hợp lệ trả về giá trị TRUE

#Hàm đặt quân Hậu
def giai(banco, cot):
    if cot >= N: #Kiểm tra đã đủ số quân Hậu chưa
        return True
    for i in range(N):
        i = r.randint(0,N-1) #đặt vị trí bất kì ở cột 1
        if kiemtra(banco, i , cot) == True: #Sử dụng hàm kiemtra để kiểm tra vị trí đứng
            banco[i][cot] = 1 #Nếu hợp lệ gán vị trí đứng là 1
            if giai(banco, cot +1) == True: #Sử dụng giải thuật đệ quy, gọi lại hàm để giải cho quân hậu tiếp theo
                return True #Nếu đặt được quân tiếp theo trả về giá trị TRUE

            banco[i][cot] = 0 # trả về giá trị ban đầu nếu không tìm được lời giải và trả về giá trị FALSE
    return False

def giao_dien(): #Vẽ bàn cờ và các quân Hậu
    ban_co = Tk()
    ban_co.title("GIAI BAI TOAN QUAN HAU") #Tạo tiêu đề
    hinh = N*20//N
    hinh_banco= Canvas(ban_co, width= N*20, height= N*20, bg="white") #Tạo khung bàn cờ nền trắng
    hinh_banco.pack()
    #Tạo các vùng đen
    for i in range(N):
        for j in range(N):
            if (i + j + N) % 2 == 1:
                hinh_banco.create_rectangle(i * hinh, j * hinh, i * hinh + hinh, j * hinh + hinh, fill="black")
    #Tại các vị trí đặt được quân Hậu, ta vẽ hình quân Hậu 
    for i in range(N):
        for j in range(N):
            if banco[i][j] == 1:
                hinh_banco.create_text(i * hinh + hinh // 2, j * hinh + hinh // 2, text=u'\u265b',
                                       font=('Arial', hinh // 2), fill='red')

    btKhac= Button(ban_co,text="Trường hợp khác",width=20,bg="grey",command=haha)
    btKhac.pack()
    ban_co.mainloop()

def haha(): #Hàm chạy trương trình in ra màn hình
    if giai(banco, 0) == False:
        print('Khong co loi giai')
    else:
        giao_dien()
        print(banco)


if __name__ == '__main__': 
    N = int(input("So quan Hau:")) #Nhập số quân Hậu bất kì từ bàn phím
    banco = [[0] * N for i in range(N)] #Vẽ bàn cờ bằng thư viện NumPy sử dụng mảng
    banco = n.reshape(banco, [N, N])
    haha() #Chạy trương trình với các tham số đã nhập
