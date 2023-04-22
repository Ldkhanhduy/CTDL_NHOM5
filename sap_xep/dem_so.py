def dem_so(ls):
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    ls1 = set(ls.copy())
    ls1 = list(ls1)
    print("Có dãy số:", ls)
    print("Số lần xuất hiện của các số trong dãy số")
    for i in range(len(ls1)):
        dem = 0
        for j in range(len(ls)):
            if ls[j] == ls1[i]:
                dem +=1
        print("(",ls1[i],",",dem,")")

if __name__ == '__main__':
    ls = input("nhập các số cần sắp xếp (ngăn cách nhau bằng dấu cách):").split()
    dem_so(ls)