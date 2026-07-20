scores = [70, 85, 40, 95, 60]

total = 0

for score in scores:
    total = total + score
    if score >= 80:
        print(score, "-> strong")
    elif score >= 50:
        print(score, "-> keep going")
    else:
        print(score, "-> retry")

average = total / len(scores)
print("Average score:", average)