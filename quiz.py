def ask_question(q, a):
    answer = input(q + "\n> ")
    if answer.lower() == a.lower():
        print("✅ Correct!\n")
        return 1
    else:
        print("❌ Wrong!\n")
        return 0

def quiz():
    score = 0
    print("🎉 Welcome to the Quiz 🎉\n")

    score += ask_question("1. What is the capital of Nepal?", "Kathmandu")
    score += ask_question("2. What is 5 + 7?", "12")
    score += ask_question("3. What color is the sky on a clear day?", "Blue")
    score += ask_question("4. Who created Python?", "Guido van Rossum")
    score += ask_question("5. What does CPU stand for?", "Central Processing Unit")

    print(f"🏁 You got {score} out of 5!")

# Start the quiz
quiz()
