def tuan_tu(D, x):
    i = 0
    while i < len(D): #Duyệt qua từng phần tử
        if D[i] == x: #Kiểm tra mỗi phần tử có bằng vỡi hay không
            print(x, "nằm ở vị trí", i + 1, "ở trong danh sách") #Nếu bằng
            break
        else:
            i +=1 #Nếu không
    else:
        print(x, "không nằm trong danh sách")

if __name__ == '__main__':
    D = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
    x = int(input("nhập số cần tìm:"))
    tuan_tu(D, x)