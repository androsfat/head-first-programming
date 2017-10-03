highest_score = 0

result_f = open("results.txt")
scores = []
for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    # if float(score) > highest_score:
    #     highest_score = float(score)
    # print(line)
result_f.close()
scores.sort()
scores.reverse()
print("The top scores were:")
# print(highest_score)
print(scores[0])
print(scores[1])
print(scores[2])
