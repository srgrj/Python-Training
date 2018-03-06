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


myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'
