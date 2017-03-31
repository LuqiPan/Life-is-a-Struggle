from collections import defaultdict

def group_anagrams(word_list):
    dict = defaultdict(list)
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        dict[sorted_word].append(word)

    result = []
    for k, v in dict.iteritems():
        result += v

    return result

print group_anagrams(['abc', 'ab', 'acb', 'cba'])
