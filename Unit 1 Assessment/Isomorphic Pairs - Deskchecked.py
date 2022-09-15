def isomorphic_pairs(word):
    pairs = ""
    lc = 0
    for letter in word:
        lc += 1
        for check in range(len(word)):
            if letter == word[check] and check >= lc:
                pairs += "+" + str(check-lc+1) + " "
                break
            elif check+1 == len(word):
                pairs += "0 "
    return pairs
word1 = input("Please input a word: ")
word2 = input("Please input a second word of the same length: ")
while len(word1) != len(word2):
    print("These words are not of the same length. Please input 2 words of the same length")
    word1 = input("Please input a word: ")
    word2 = input("Please input a second word of the same length: ")
compare1 = isomorphic_pairs(word=word1)
compare2 = isomorphic_pairs(word=word2)
if compare1 == compare2:
    print(f"{word1} and {word2} are isomorphic pairs with a pattern of {compare1}")
else:
    print(f"{word1} and {word2} are not isomorphic pairs")
