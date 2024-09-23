l1:list[int]=[];
for i in range(1,101):
    l1.append(i)
print("first value:",l1[0])
print("last value:",l1[-1])
print("length:",len(l1))
# l2:list[int]=[];
# for i in range(3,13)
print("3-12:",l1[2:12])
print("80-end:",l1[79::])
print("start-17",l1[:17])
print("reverse:",l1[::-1])
print("evens:",l1[1::2])
print("div 3:",l1[2::3])
print("div 7:",l1[6::7])
print("div 10:",l1[9::10])
print("99-66 step 3:",l1[98:62:-3])

l1.insert(len(l1)//2,999)
print("after insert:",l1[:])

l1.pop();
print("after pop last:",l1[:])