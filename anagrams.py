# **54 Grouping anagrams.**
words = ['eat', 'ate', 'tea', 'fear', 'hello', 'silent', 'fare', 'listen']
anagram = {}
for word in words:
    w ="".join(sorted(word))
    print(w)

    if w not in anagram:
        anagram[w]=[word]

    else:
        anagram[w]= anagram[w]+[word]
# print(anagram)

###################################################################################################################
# **16 Write a program to get the below output**
# sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# sentence = "hello world welcome to python programming hi there"
# sentence_list = sentence.split()
# dic = {}
# for word in sentence_list:
#     if


########################################################################################################





