def format_number(bruh):
    hmm = len(bruh) % 3
    count = 0 - hmm + 3
    answer = ""
    for i in range(len(bruh)):
        answer = answer + bruh[i]
        if count %3 == 0:
            answer = answer + ','
    return answer
print(format_number(1000000))

