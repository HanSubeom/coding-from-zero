score = int(input("Enter your score: "))

print("Score:", score)

if score >= 80:
    print("Result: strong")
elif score >= 50:
    print("Result: keep going")
else:
    print("Result: retry")
    