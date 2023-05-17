def nhi_phan(min, max, D, x):
    if min < max:
        mid = int((min+max)/2)
        if D[mid] == x: return print(x, "nằm ở vị trí", mid+1, "trong danh sách")
        else:
            if x < D[mid]:
                return nhi_phan(min, mid-1, D, x)
            else:
                return nhi_phan(mid+1, max, D, x)
    else:
        print("Không tìm thấy")

if __name__ == '__main__':
    D = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
    D = sorted(D)
    print(D)
    x = int(input("Nhập số cần tìm:"))
    nhi_phan(0, len(D)-1, D, x)