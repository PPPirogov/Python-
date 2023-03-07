n,k = map(int, input().split())
def fn(n,k):
    if k == 0 or (n == k) :
        #print(a, b)
        return 1
    else :
        #print(n - 1, k ,") + (" ,n -1,k -1)
        return fn(n - 1, k) + fn(n - 1, k - 1)

print (fn(n,k))