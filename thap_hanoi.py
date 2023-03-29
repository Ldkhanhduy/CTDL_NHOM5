def thaphanoi(n,cotA, cotB, cotC):
    if n == 1:
        print("chuyen tu",cotA,"sang",cotC )
        return
    else:
        thaphanoi(n-1,cotA, cotC, cotB)
        print("chuyển từ",cotA,"sang",cotC)
        thaphanoi(n-1,cotB,cotA,cotC)

if __name__ == '__main__':
    n = int(input("Nhap so tang cua thap:"))
    thaphanoi(n, "cotA", "cotB", "cotC")
