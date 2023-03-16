def chiathuong(m,n):
    if (m==0):
        return 1
    if (n==0):
        return 0
    else:
        if (m<n):
            return chiathuong(m,m)
        else:
            return chiathuong(m-n,n)+chiathuong(m,n-1)

def dem(m,n):
    print(m, 'phan thuong,', n, 'hoc sinh se co', chiathuong(m,n)
          , 'cach chia.')

if __name__ == '__main__':
    m= int(input('so phan thuong:'))
    n= int(input('so hoc sinh:'))
    dem(m,n)