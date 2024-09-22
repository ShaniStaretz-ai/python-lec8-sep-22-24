# Ex1:
from statistics import mean
grade: int = -1;
grades: list[int] = [];
max_g = -1;
min_g = 100
SENTINEL = -999
while True:
    grade = int(input("enter number:"));
    if grade == SENTINEL:
        break;
    if not 0 <= grade <= 100:
        continue;
    grades.append(grade);

if grades:
    print("avg:", sum(grades) / len(grades))
    print("mean:", mean(grades))
    print("max:", max(grades))
    print("min:", min(grades))
