def UCLN(a,b):
    if (b==0):
        return a
    else:
        return UCLN(b,a%b)
if __name__ == '__main__':
    a= int(input('a='))
    b= int(input('b='))
    print('UCLN của', a, 'va', b, 'la:', UCLN(a,b))