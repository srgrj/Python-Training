def myfunc(word):
    op = ""
    for a, b in enumerate(word):
        if a == 0:
            op += b.lower()
        elif a % 2 == 0:
            op += b.lower()
        else:
            op += b.upper()
    return op


# myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'

n = "how are you doing"


# print(n.split())


def word_lengths(phrase):
    return phrase, len(phrase)


# print(dict(map(word_lengths, n.split())))

# print(dict(map(lambda phrase: (phrase, len(phrase)), n.split())))

from functools import reduce


def digits_to_num(digits):
    print(reduce(lambda x, y: x * 10 + y, digits))


# digits_to_num([3,4,3,2,1])

def filter_words(word_list, letter):
    print(list(filter(lambda word: word[0] == letter, word_list)))


l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']


# filter_words(l,'h')

# ['hello', 'ham', 'hi', 'heart']


def concatenate(L1, L2, connector):
    lst = [x[0] + '-' + x[1] for x in list(zip(L1, L2))]
    print(lst)


# concatenate(['A', 'B'], ['a', 'b'], '-')


def d_list(l):
    print({key: value for value, key in enumerate(l)})


# d_list(['a', 'b', 'c'])


def count_match_index(l):
    print(len([num for count, num in enumerate(l) if num == count]))


# count_match_index([0, 2, 2, 1, 5, 5, 6, 10])

def gensquares(N):
    for i in range(0, N):
        yield i ** 2


# lst = gensquares(4)
# print(next(lst))
# for x in gensquares(10):
#    print(x)

import random


def rand_num(low, high, n):
    for i in range(0, n + 1):
        yield random.randint(1, 10)
