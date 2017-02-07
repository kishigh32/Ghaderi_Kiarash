mathOrWords = int(input("Would you like to..." +
                        "\n 1. Do a math problem?" +
                        "\n 2. Answer a question?"))

if mathOrWords == 1:
    mathAnswer = int(input("What is 2 X 2?"))
    if mathAnswer == 4:
        print("Correct")
    else:
        print("Wrong")
else:
    wordAnswer = input("Who said the phrase \"Whatever you are, be a good one.\"?")
    if wordAnswer == "Abraham Lincoln":
        print("Correct")
    else:
        print("Wrong")
        

