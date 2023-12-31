from collections import Counter, defaultdict


def practice():
    strs =  ['tea','eat','ate','tan','ant']
    res = defaultdict(list)
    for word in strs:
        count = [0]*26
        for letter in word:
            count[ord(letter)-ord('a')] += 1
        res[tuple(count)].append(word)
        print(res)
    return res.values()
practice()


