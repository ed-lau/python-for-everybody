fname = input("Enter file name: ")
fh = open(fname)
data=[]
for each in fh:
    words=each.split()
    for word in words:
        if word not in data:
            data.append(word)
print(sorted(data))
