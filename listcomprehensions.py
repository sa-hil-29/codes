"""mylist = [num for num in range(1,51) if num%3==0]
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print("even")

for num in range(1,101):
    if(num%3 == 0)and(num%5==0):
        print("FizzBuzz")
    elif(num%3 == 0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    else:
        print(num)"""

st = 'Create a list of the first letters of every word in this string'
lst = [word[0] for word in st.split()]
print(lst)
