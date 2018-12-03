a = 1
b = 2
sum_ = 2

def fibo(a,b, sum_):
    c = a + b
    if c%2==0: sum_ += c
    print(sum_)
    a, b = b, c
    if b < 4000000:
       fibo(a,b, sum_)
    else:
        return sum_

print(fibo(a,b,sum_))
