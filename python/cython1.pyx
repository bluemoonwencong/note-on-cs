print("Hello World")

def f1(x):
    return x ** 2 - x

cpdef long f2(long x):
    return x ** 2 - x

cdef long f3(long x):
    return x ** 2 - x


def primes(int kmax):
    cdef int n, k, i
    cdef int p[1000]
    result = []
    if kmax > 1000: kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i += 1
        if i == k:
            p[k] = n
            k += 1
            result.append(n)
        n += 1
    return result

def primes_fast(int kmax):
    cdef int n, k, i
    cdef int p[1000]
    if kmax > 1000: kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i += 1
        if i == k:
            p[k] = n
            k += 1
        n += 1
    return p


print("Hello World -- ")


