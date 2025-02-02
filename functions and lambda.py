import string

def vol(rad):
    return 3.14 * 4 * (rad ** 3) / 3

def ran_check(num,low,high):
    return num in range(low,high+1)

def up_low(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return [upper,lower]

def unique_list(lst):
    return list(set(lst))

def multiply(numbers):
    prod = 1
    for num in numbers:
        prod *= num
    return prod

def ispangram(str1, alphabet = string.ascii_lowercase):
    return len(set(str1.replace(" ","").lower())) == len(alphabet)
print(ispangram("The quick brown fox jumps the lazy dog"))
#print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
#print(vol(2))
