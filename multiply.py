# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
n1 = '3141592653589793238462643383279502884197169399375105820974944592'
n2 = '2718281828459045235360287471352662497757247093699959574966967627'

def multi(num1, num2):
    n1, n2 = len(num1), len(num2)
    a, b, c, d = num1[:n1//2], num1[n1//2:], num2[:n2//2], num2[n2//2:]
    if min(len(a), len(b), len(c), len(d)) == 1:
        ac = str(int(a)*int(c))
        ad = str(int(a)*int(d))
        bc = str(int(b)*int(c))
        bd = str(int(b)*int(d))
    else:
        ac = multi(a, c)
        ad = multi(a, d)
        bc = multi(b, c)
        bd = multi(b, d)
    return str(int(ac)*int(10**(len(a)*2))+(int(ad)+int(bc))*int(10**len(a))+int(bd))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(multi(n1, n2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/