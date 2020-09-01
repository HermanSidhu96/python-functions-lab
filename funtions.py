#1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
def sum_to(n):
    result = 0
    for i in range(0,n + 1):
        result = result + i
    return result

answer = sum_to(10)
print(answer)

#2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.

def largest(*args):
    myMax = args[0]
    for num in args:
        if myMax < num:
            myMax = num
    return myMax


print (largest(10,9,8,7,6,5,4,3,22,111))

#3. Write a function named `occurances` that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(string,word):
    count = 0
    for i in range(0,len(string)):
        if (word == string[i]):
            count = count + 1
    return count

print (occurances('torontoraptors', 'o'))
