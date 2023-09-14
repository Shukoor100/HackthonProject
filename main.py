msgData = open("msg.txt", "r")

lines = msgData.readlines()
print(lines)

for line in lines:
    words = line.split()
    for word in words:
        print(word)
