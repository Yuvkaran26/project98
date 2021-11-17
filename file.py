# file = open("data.txt", "r")
# print(file.read())


# file = open("data.txt", "r")
# print(file.readlines())
# file.close()

# file = open("data2.txt", "a+")
# file.write("I like video games,\n and chocolate")
# file.close()

# file=open("image0.png", "rb")
# con = file.read()
# print(con)

# file=open("my.png", "wb")
# file.close()

# data = "hi, how r u? im doing good."
# word = data.split(" ")
# print(word)

def words():
    filename = input("enter the file name: ")
    numofwords=0
    file=open(filename, "r")
    for i in file:
        words = i.split()
        numofwords=numofwords+len(words)
    print(numofwords)
words()