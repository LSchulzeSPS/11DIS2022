#Capital Indexes
def capital_indexes(lol):
    nlist = []
    for i in range(len(lol)):
        if lol[i].isupper():
            nlist.append(i)
    return nlist
print(capital_indexes("HeLlO"))

#Middle Letter
def mid(abc):
    if 0 == len(abc)%2:
        return("")
    else:
        return(abc[int(len(abc)/2)])
print(mid("abc"))

#Online Status
def online_count(statuses):
    count = 0
    for words in statuses:
        if statuses[words] == "online":
            count += 1
    return(count)
print(online_count(statuses = {"Alice": "online", "Bob": "offline", "Eve": "online"}))

#Randomness
import random
def random_number():
    return(random.randint(1,100))
print(random_number())
