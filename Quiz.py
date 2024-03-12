# Quiz Questions, Options, and Correct Answers
questions = [
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the chemical symbol for water?",
    "What is the tallest mammal?",
    "What is the powerhouse of the cell?"
]

options = [
    ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
    ["A. Harper Lee", "B. J.K. Rowling", "C. Stephen King", "D. Mark Twain"],
    ["A. H", "B. O", "C. H2O", "D. HO"],
    ["A. Elephant", "B. Giraffe", "C. Hippopotamus", "D. Rhino"],
    ["A. Nucleus", "B. Cell membrane", "C. Mitochondria", "D. Chloroplast"]
]

answers = ["B", "A", "C", "B", "C"]

# Function to present questions with options and collect answers
def present_question(question, options, answer):
    print(question)
    for option in options:
        print(option)
    user_answer = input("Your Answer (A/B/C/D): ").strip().upper()
    if user_answer == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect! The correct answer is:", answer)
        return 0

# Function to run the quiz
def run_quiz(questions, options, answers):
    score = 0
    for i in range(len(questions)):
        score += present_question(questions[i], options[i], answers[i])
    print("Quiz Complete! You scored {}/{}.".format(score, len(questions)))

# Run the quiz
if __name__ == "__main__":
    run_quiz(questions, options, answers)

