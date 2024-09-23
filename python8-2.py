from statistics import mean

l2: list[float] = [];
count_2 = 0
while True:
    height: float = float(input("enter height:"))
    if height == -999:
        break;
    if height < 1.60 or height > 3.0:
        continue;
    if height > 2.0:
        count_2 += 1;
    l2.append(height)
print("total:", len(l2))
print("highest:", max(l2))
print("shortest:", min(l2))
print("avg:", mean(l2))
print("higher than 2.0 m:", count_2)
mean: float = mean(l2)
count_mean: int = 0;
for i in range(len(l2)):
    if l2[i] > mean:
        count_mean += 1
print(f"higher than {mean} m:{count_mean}")
