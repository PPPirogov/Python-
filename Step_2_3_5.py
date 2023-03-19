import itertools

def primes():
    a = 1
    while True:
        b = 0
        i = 1
        while i <= a:
            if a % i == 0:
                b+=1
            i+=1
        a += 1
        if b == 2:
            yield a-1

# def primes():
#     a = 1
#     while True:  # просто пример
#         a += 1
#
#         yield a

print(list(itertools.takewhile(lambda x : x <= 31, primes())))