import time

def sap_xep_chen(ls):
    start = time.time()
    for i in range(len(ls)):
        temp = ls[i]
        pos = i
        while (pos>0) and (ls[pos-1] >temp):
            ls[pos] = ls[pos-1]
            pos -= 1
        ls[pos] = temp
    print(ls)
    end = time.time() - start
    print("Thời gian thực hiện:", end)


if __name__ == '__main__':
    ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
    sap_xep_chen(ls)