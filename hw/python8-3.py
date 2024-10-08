l3: list[int] = []
MULTI_10 = 10
SENTINEL: int = -999
for i in range(MULTI_10, MULTI_10 ** 2 + 1, MULTI_10):
    l3.append(i)
print(l3)

while True:
    number: int = int(input("Enter number:"))
    if number == SENTINEL:  # break point
        break;
    if number > l3[len(l3) - 1]:
        index = len(l3);
        l3.insert(index, number);
        print(l3)
        continue;
    elif number <= 10:
        index = 0
    else:
        index = number // MULTI_10 - 1  # since the values are in multiples 10,
    while l3[index] < number:  # find the right index
        index += 1
    l3.insert(index, number)  # when find the right index add to the list
    print(l3)
