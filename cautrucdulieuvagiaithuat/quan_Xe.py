import numpy as n
import random as r

def kiemtra(banco, hang, cot):
    for i in range(cot):
        #kiemtra en trai cua hang
        if banco[hang][i] == 1:
            return False
        #kiem tra cot phia tren tuong ung voi hang
        # for j in range(hang):
        #     if banco[j][cot] == 1:
        #         return False
        #     if banco[hang+j][cot] == 1:
        #         return False
    return True

def giai(banco, cot):
    if cot >= N:
        return True
    for i in range(N):
        i = r.randint(0,N-1)
        if kiemtra(banco, i, cot) == True:
            banco[i][cot] = 1
            if giai(banco, cot+1) == True:
                return True
            banco[i][cot] = 0
    return False

if __name__ == '__main__':
    N = int(input('Nhap so quan xe:'))
    banco = [[0]*N for i in range(N)]
    banco = n.reshape(banco, [N,N])
    # m= int(input('nhap quan xe dau tien:'))
    # n= int(input())
    if giai(banco,0) == False:
        print('Khong co loi giai')
    else:
        print(banco)
