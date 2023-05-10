# Cai dat Thuat toan Sap xep nhanh Quick Sort


# Doi cho gia tri cua 2 bien
def doicho(m, n):
    return n, m


# Thuat toan Quick Sort
def quicksort(L, R):
    global ls
    if L >= R:
        return
    i = L
    j = R
    x = ls[(L + R)//2]

    while True:
        while ls[i] < x:
            i = i+1
        while ls[j] > x:
            j = j - 1
        if i <= j:
            ls[i], ls[j] = doicho(a[i], a[j])
            i = i + 1
            j = j - 1
        else:
            break
    quicksort(L, j)
    quicksort(i, R)


# CHUONG TRINH CHINH
if __name__ == '__main__':
  ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
  quicksort(0, len(ls) - 1)

  print("Day so khi duoc sap xep la: ", ls)
