def heapify(arr, n, i):
    # Khởi tạo root, left và right
    root = i
    left = 2 * i + 1
    right = 2 * i + 2
  
    # Đảm bảo left child của root tồn tại và lớn hơn root
    if left < n and arr[i] < arr[left]:
        root = left
  
    # Đảm bảo right child của root tồn tại và lớn hơn root và left
    if right < n and arr[root] < arr[right]:
        root = right
  
    # Nếu root không phải là i, hoán đổi giá trị và thực hiện heapify cho root
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, n, root)
  
def heap_sort(arr):
    n = len(arr)
  
    # Xây dựng vun đống (heapify) 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # Sắp xếp mảng bằng cách lấy phần tử lớn nhất từ vun đống
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Hoán đổi giá trị
        heapify(arr, i, 0)
    print(ls)
    
if __name__ == '__main__':
  ls = [int(i) for i in input("Nhập dãy số (mỗi số cách nhau một dấu cách):").split()]
  heap_sort(ls)
