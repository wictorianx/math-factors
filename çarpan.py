def carpanlar(t,primes)
    factors = []
    a = 0
    while(t!=1):
        print(t)
        if t%primes[a] == 0:
            factors.append(primes[a])
            t/=primes[a]
        else:
            a+=1
    return(factors)
#carpanlar(y,[2,3,5,7,9,11,13])
def ebob(x,y):
    xf = carpanlar(x,[2,3,5,7,9,11,13])
    yf = carpanlar(y,[2,3,5,7,9,11,13])

    allf = set()

    for i in xf:
        allf.append(i)
    for i in yf:
        allf.append(i)
    return(max(allf))
def product(elements):
    sum_ = 1
    for i in elements:
        sum_*=i
    return(sum)
def ekok(x,y)
    xf = carpanlar(x,[2,3,5,7,9,11,13])
    yf = carpanlar(y,[2,3,5,7,9,11,13])
    for i in xf:
        if i in yf:
            yf.remove(i)
            xf.remove(i)
    return(product(product(yf),product(xf)))
