def replace():

    sentence = input("Enter a String please: ")

    top = 0
    while top < sentence.count("a") > 0:
        sentence = sentence[0 : sentence.index("a")] + "@" + sentence[sentence.index("a")+1 : len(sentence)]

    print(sentence)

replace()

