f=open("test.py","r")
count=0
linecount=0
for line in f.readlines():
    linecount+=1
    for char in line:
        count+=1

print(count)
print(linecount)
f.close()
