word = input("Enter a word please: ")
stop = len(word)
start = 0

def tree(word, start, stop):
    if start <= stop:
        print("{:>20}".format(word[0:start]))
        start = start + 1
        return tree(word, start, stop)

tree(word, start, stop)

