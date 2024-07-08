
# sentence = "hello welcome to my world"
# # sentence_dict = {}
# # _sentence = sentence.split()
# # for i in _sentence:
# #     sentence_dict[i] =len(i)
# # print(sentence_dict)
# sentence_ = sentence.split()
# sentence_dictionary = {sen: len(sen) for sen in sentence_}
# print(sentence_dictionary)

#############################################################################
words = "hello python hello how are you hello world hello python"
words_list = words.split()
# words_dict = {}
#
# for word in words_list:
#     words_dict[word]=words_list.count(word)
#
# print(words_dict)
#
# by using comprehension

words_new = {word: words_list.count(word) for word in words_list}
# print(words_new)

################################################################################################
# words = "hello python hello how are you hello world hello python"
# words_dict = {}
# for letter in words:
#     words_dict[letter] = words.count(letter)
# print(words_dict)

# words_new = {letter: words.count(letter) for letter in words }
# print(words_new)

##############################################################################################################


word = "abcdEQGHBL"
# word_dict = {}
# for letter in word:
#     word_dict[letter] = ord(letter)
# print(word_dict)

#####
# word_ = {w:ord(w) for w in word}
# print(word_)
# w_list = []
# for w in word:
#     w_list =w_list + [w]
# print(w_list)

#########################################################################################################3

buildings = {'burj khalifa':100,'uganda tower':150,'bemuda tower':76,'german tower':53}

# building_ = {}
# for name,height in buildings.items():
#     building_[name] = height *3.28
# print(building_)

building_new = {name:height * 3.28 for name,height in buildings.items()}
# print(building_new)

################################################################################################################

# cities = ["tokyo", "delhi", "bangalore", "noida", "pune"]
# population = [10000, 30000, 23000, 42000, 12348]
# # dict_new = {}
# #
# # for c,p in zip(cities,population):
# #     dict_new[c] = p
# # print(dict_new)
#
# dict_ = {c:p for c,p in zip(cities,population)}
# print(dict_)


###################################################################################################


# dial_codes = [(86,'china'), (91,'india'), (1,'united states'), (62,'indonesia'), (81,'japan'), (7,'russia')]
# dial_dict = {}
#
# for pin,country in dial_codes:
#     # pin = codes[0]
#     # country = codes[1]
#     # pin,country = codes
#     dial_dict[country]=pin

# print(dial_dict)

# dial_ = {country:pin for pin, country in dial_codes}
# print(dial_)

#########################################################################################################
# prices = {'ACME': 156, 'AAPL': 324, 'IBM': 87, 'META': 541, 'IOCL': 119}
#
# prices_ = {}
# for key,value in prices.items():
#     if value > 100:
#         prices_[key]= value
# # print(prices_)
#
# _prices = {key:value for key,value in prices.items() if value>100}
# print(_prices)

###############################################################################################################

##set comprehension

nums = [1, 2, 3, 4, 5, 6, 7]
squares = set()
for n in nums:
    squares.add(n ** 2)

print(squares)

# sq = {n ** 2 for n in nums}
# print(sq)

















