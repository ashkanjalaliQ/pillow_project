def Processing_sentence(sentence):
    return sentence.split()


def find_max(ls):
    _max_ = max(ls)
    for i in range(len(ls)):
        if ls[i] == _max_:
            return i

def recommender(word, options):
    p = []
    word = word.strip()
    for option in options:
        t = 0
        for letter in option.strip():
            if letter in word:
                t += 1
        p.append(t / len(option))

    return options[find_max(p)]


#def Check_command(command):
    #image_address =

#print(recommender('negabla', ['grayscale', 'negative', 'blackandwhite']))
#print(find_max([1.0, 1.625, 0.46153846153846156]))