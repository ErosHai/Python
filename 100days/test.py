# 斐波那契数列 第三个数等于前两个数的和
a, b = 0, 1
for _ in range(20):
    a , b = b, a + b
    print(a,b)


# 求阶乘的函数  当前数步长为1的总和
def fac(num):
    result = 1
    for x in range(2, num +1):
        result += x
    return result

print(fac(3))
