import numpy as n
import random as r
from tkinter import *
from tkinter import ttk

# banco = [[0]*8 for i in range(8)]
# banco = n.reshape(banco,[8,8])
# banco[0][0] = 1
# def ok():
#     for i in range(1,8):
#         for j in range(1,8):
#             for a in range(i):
#                 if (banco[j][a] == 1):
#                     return False
#             for b,c in zip(range(j,-1,-1), range(i, -1, -1)):
#                 if banco[b][c] == 1:
#                     return False
#             for b,c in zip(range(j,8,1), range(i,-1,-1)):
#                 if banco[b][c] == 1:
#                     return False
#             banco[j][i] = 1
#
#
# print(banco)

def kiemtra(banco,hang,cot):
    for i in range(cot):
        if banco[hang][i] == 1:
            return False
    for i,j in zip(range(hang, -1, -1), range(cot, -1, -1)):
        if banco[i][j] == 1:
            return False
    for i, j in zip(range(hang, 8, 1), range(cot, -1, -1)):
        if banco[i][j] == 1:
            return False
    return True

def giai(banco, cot):
    if cot >= N:
        return True
    for i in range(N):
        i = r.randint(0,N-1)
        if kiemtra(banco, i , cot) == True:
            banco[i][cot] = 1
            if giai(banco, cot +1) == True:
                return True

            banco[i][cot] = 0
    return False

def giao_dien():
    ban_co = Tk()
    ban_co.title("GIAI BAI TOAN QUAN HAU")
    hinh = N*20//N
    hinh_banco= Canvas(ban_co, width= N*20, height= N*20, bg="white")
    hinh_banco.pack()
    for i in range(N):
        for j in range(N):
            if (i + j + N) % 2 == 1:
                hinh_banco.create_rectangle(i * hinh, j * hinh, i * hinh + hinh, j * hinh + hinh, fill="black")
    for i in range(N):
        for j in range(N):
            if banco[i][j] == 1:
                hinh_banco.create_text(i * hinh + hinh // 2, j * hinh + hinh // 2, text=u'\u265b',
                                       font=('Arial', hinh // 2), fill='red')

    btKhac= Button(ban_co,text="Trường hợp khác",width=20,bg="grey",command=haha)
    btKhac.pack()
    ban_co.mainloop()

def haha():
    if giai(banco, 0) == False:
        print('Khong co loi giai')
    else:
        giao_dien()
        print(banco)


if __name__ == '__main__':
    N = int(input("So quan Hau:"))
    banco = [[0] * N for i in range(N)]
    banco = n.reshape(banco, [N, N])
    haha()
