def get_scores():
    raw_input = input("Enter scores separated by spaces: ")
    parts = raw_input.split()

    scores = []
    for part in parts:
        scores.append(int(part))

    return scores


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


scores = get_scores()

print_evaluation(scores)

average = calculate_average(scores)
print("Average score:", average)

strong_count = count_strong(scores)
print("Strong count:", strong_count)