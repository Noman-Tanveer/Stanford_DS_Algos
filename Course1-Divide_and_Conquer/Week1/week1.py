
def multiply(x, y):
    a = x[:len(x)//2]
    b = x[len(x)//2:]
    c = y[:len(y)//2]
    d = y[len(y)//2:]

    if min(len(a), len(b), len(c), len(d)) == 1:
        ac = str(int(a)*int(c))
        bd = str(int(b)*int(d))
        ad = str(int(a)*int(d))
        bc = str(int(b)*int(c))
        return (str(int( str(ac) + '0'* (len(b) + len(d))) + int(str(int(ad) + int(bc)) +'0'* ((len(c)))) + int(bd)))
    else:
        ac = multiply(a,c)
        bd = multiply(b,d)
        ad = multiply(a,d)
        bc = multiply(b,c)
    return (str(int( str(ac) + '0'* (len(b) + len(d))) + int(str(int(ad) + int(bc)) +'0'* ((len(c)))) + int(bd)))
print(multiply('1100', '1100'))