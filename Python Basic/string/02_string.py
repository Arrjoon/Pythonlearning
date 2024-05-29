#function to reverse word of string

def rev_sentence(sentence):

    words = sentence.split()
    reversed_sentences = " ".join(reversed(words))
    print(reversed_sentences)


if __name__=="__main__":
    a=str(input("Enter the string"))

rev_sentence(a)