# ex1:
from random import random
from statistics import mean

l1: list[int] = [];

for i in range(10):
    l1.append(int(input("enter number:")))
print("len:", len(l1))
print("max:", max(l1))
print("min:", min(l1))
print("mean:", mean(l1))

max_manual: int = l1[0];#not =-1/0, because the value can be negative
for i in range(1,len(l1)):
    if max_manual < l1[i]:
        max_manual = l1[i]
print("max_manual:", max_manual)

# ex2:
from random import choice
from statistics import mean

l2: list = []
for _ in range(10):
    l2.append(choice([1, 4, 9, -2]))
print("mean:", mean(l2))

#DOTO: test
