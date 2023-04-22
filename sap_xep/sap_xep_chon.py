def sap_xep_chon(ls):
    for i in range(len(ls)):
        minn = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[minn]:
                minn = j
                ls[i], ls[minn] = ls[minn], ls[i]
    print(ls)

if __name__ == '__main__':
    ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
    sap_xep_chon(ls)