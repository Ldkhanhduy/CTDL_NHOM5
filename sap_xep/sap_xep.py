def sap_xep(ls):
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    print("danh sách trước khi sắp xếp:",ls)
    for i in range(len(ls)):
        for j in range(i):
            if ls[j] > ls[i]:
                ls[j],ls[i] = ls[i],ls[j]
    print("danh sách sau khi sắp xếp:",ls)

if __name__ == '__main__':
    ls = input("nhập các số cần sắp xếp (ngăn cách nhau bằng dấu cách):").split()
    sap_xep(ls)