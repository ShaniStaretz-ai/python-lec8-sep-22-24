# python-lec8-sep-22-24

## Subjects learnt today:

1) Lists: a collection of values under 1 parameter
   * list.append(newValue): add more values to the end of the list
   * list.pop: to extract the **last** value from the list
   * len(list)- return the length of the list
   * list.clear()- empty the list
   * list+3: append the value 3 to the list
   * function works only on non-empty lists: max(list), min(list), min(list), sum(list)- simple math functions on the list
   * to define and init list: 
    ```
    grades:list[int]=[] - the list grades contains int values and init to empty list []
    ```
   * if grades == if len(grades) ==if len(grades)
   * grades[-1]= when give the last value in the list
   * grades[length+1]= will ERROR list index out of range
## Extra:

1)  keyword pass: can be used in order to make preparation without getting compilation errors.

    For example:
    ```
    while <condition>:
        pass
    else: 
        pass
    ```
2) sentinel parameters: like constant numbers but usually used to represent some terminating (end) condition or have a special, symbolic meaning. 
3) #DOTO: a keyword: to remainder later that some then is left to implement. 
4) statistics.mean():
   *    Is a function that calculate average of list:
   *  see explanation difference between sum/total and mean:
    https://byjus.com/maths/difference-between-average-and-mean/
 ```
from statistics import mean 
print(mean([1,2,3])
 ```
1) random.choices(ranges(1,10),k=10) =will return a list of 10 random numbers
2) number ** 2= number^2, square 2= number**(0.5)