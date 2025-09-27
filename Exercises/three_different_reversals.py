def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def reverse_words_again(sentence):
    return sentence[::-1]

def reverse_words_returns(sentence):
    li = list(map(lambda x:x[::-1],sentence.split()))
    return ' '.join(li)

print(reverse_words('I love India'))

print(reverse_words_again('I love India'))

print(reverse_words_returns('I love India'))
