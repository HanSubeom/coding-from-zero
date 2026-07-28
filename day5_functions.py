def calculate_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)


def print_evaluation(scores):
    for score in scores:
        if score >= 80:
            print(score, "-> strong")
        elif score >= 50:
            print(score, "-> keep going")
        else:
            print(score, "-> retry")


def count_strong(scores):
    count = 0
    for score in scores:
        if score >= 80:
            count += 1
    return count


scores = [70, 85, 40, 95, 60]

print_evaluation(scores)

average = calculate_average(scores)
print("Average score:", average)

strong_count = count_strong(scores)
print("Strong count:", strong_count)