import time

def tron(ls, h, m , t):
    a = []
    h1, t1, h2, t2 = h, m, m+1, t
    gan = h1
    while (h1<t1) and (h2<t2):
        if ls[h1] < ls[h2]:
            a.append(ls[h1])
            gan += 1
            h1 += 1
        else:
            a.append(ls[h2])
            gan += 1
            h2 += 1
    while h1 < t1:
        a.append(ls[h1])
        h1 += 1
        gan += 1
    while h2 < t2:
        a.append(ls[h2])
        h2 += 1
        gan += 1
    for i in range(len(ls)):
        ls[i] = a[i]
    print(ls)

def sap_xep_tron(ls, h, t):
    h = int(h)
    t = int(t)
    while h<t:
        m = int((h+t)/2)
        sap_xep_tron(ls, h, m)
        sap_xep_tron(ls, m+1, t)
        tron(ls, h, m, t)

if __name__ == '__main__':
    ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
    sap_xep_tron(ls, 0, len(ls)-1)

