file=open("data.txt",'w')
for i in range(5):
    file.write("str"+str(i+1)+'\n')
file.close()
file=open("data.txt",'a')
file.write("new info")
file=open('data.txt','r')
print("name file:",file.name)
print("file closed:",file.closed)
print("file mode:",file.mode)
text=file.read(5)
file.seek(0)
print("pos",file.tell())
str1=file.readline()
str2=file.readline()
print(text)
print(str1)
print(str2)
if file.readable():
    for line in file:
        print(line)
file.close()
path2='newdata.txt'
with open(path1) as dataFile,open(path2,'w') as outFile:
    data=dataFile.read()
    outFile.write(data)
def replaceTextInFile(fileName,oldText,newText):
    with open(fileName,'r+') as file:
        data=file.read()
        data=data.lower().replace(oldText,newText)
    with open(fileName, 'w') as file:
        file.write(data)
def readFromFile(fileName):
    with open(fileName) as file:
        print(file.read())
def wordCounter(fileName):
    nWords=0
    with open(fileName)as file:
        data=file.read()
        lines=data.split()
        for word in lines:
            if not word.isnumeric():
                nWords+=1
    return nWords
print(wordCounter(path1))
print("Old data")
readFromFile(path1)
replaceTextInFile(path1,'python','JS')
print("New data")
readFromFile(path1)
#1
with open('data.txt') as file:
    allMark=0
    stud=0
    for i in file:
        lastn,name,mark=i.split()
        if int(mark)<=3:
            print(f"{lastn} {name}: {mark}")
        allMark+=int(mark)
        stud+=1
print(f"Average={allMark/stud}")
#2
with open('data.txt','w') as file:
    while True:
        data=input("Enter something(finish-only enter):")
        if not data:
            break
        file.write(data+'\n')
print('data.txt')
#3
with open('data.txt', 'r') as file:
    read_line = file.readlines()
countLine=len(read_line)
line=0
for i in read_line:
    line+=1
    symbol = len(i)
    word = sum(1 for j in i if j.isalpha())
    print(f"In {line} there are {symbol} symbols and {word} words")
print(f"There are {countLine}")


