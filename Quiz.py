questions = {
    "What is the capital of France? ": "Paris",
    "What is 5 * 7? ": "35",
    "What is the boiling point of water? ": "100"
}

score = 0
for q, a in questions.items():
    answer = input(q)
    if answer.strip().lower() == a.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong. Answer was: {a}")

print(f"Your score: {score}/{len(questions)}")