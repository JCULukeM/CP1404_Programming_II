
sentence = {}

def main():
    word_string = input("Enter a sentence")
    word_list = word_string.split(" ")

    for word in word_list:
        frequency = sentence.get(word,0)
        sentence[word] = frequency +1
    word_list = list(sentence.keys())
    word_list.sort()

    max_length = max((len(word) for word in word_list))
    for word in word_list:
        print("{:{}} : {}".format(word, max_length, sentence[word]))

main()
