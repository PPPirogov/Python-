def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   print (b)
   return res


#print(s(10))
#print(s(b=31, 0))

print(s(11, b=20))