import grammer

msgData = open("msg.txt", "r")
lines = msgData.readlines()
msgData.close

keyData = open("samples.txt", "r")
rawkeys = keyData.readlines()
keyData.close
keys = list(map(lambda key: key[:-1], rawkeys))

nouns = []


for line in lines:
    words = line.split()
    for word in words:
        if(grammer.checkNoun(word)):
            print(word)
