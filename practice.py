with open("practice.txt","w") as f:
    f.write("Hello World.\nI'm learning File I/O.\n")
    f.write("Using Java.\nI like programming in Java.")
def check_word_line(word:str):
    linecount = 0
    with open("practice.txt","r") as f:
        for line in f.readlines():
            linecount += 1
            if (word in line):
                return linecount

        return -1

word = str(input("Enter a word to check in file: "))
result = check_word_line(word)
if (result == -1):
    print("Word not found")

else:
    print("Word found in line number ",result)
