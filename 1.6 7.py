import sys
sys.stdin = open("input.txt", "r")
d={}
n = int(input())
i = 0
d = {}
for i in range(n):
    key, *value = input().split()
    d[key] = value
#print (d)
mas = []
q = int(input())
for element in range(0, q):
    mas.append(input())
#print (mas)

