import time

def sap_xep_bot(ls):
    start = time.time()
    sort = False
    for i in range(len(ls)):
        if sort == False:
            sort = True
            for j in range(len(ls)-i-1):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
                    sort = False
    print(ls)
    end = time.time() - start
    print("Thời gian thực thi:", end)

if __name__ == '__main__':
    ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
    sap_xep_bot(ls)