"""
Quiz Application in Python
Created by: AMAN DEEEP
"""

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. define", "B. def", "C. function", "D. fun"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A. HighText Machine Language", "B. HyperText and links Markup Language", 
                    "C. HyperText Markup Language", "D. None of these"],
        "answer": "C"
    },
    {
        "question": "Which is a Python web framework?",
        "options": ["A. Laravel", "B. Angular", "C. Django", "D. React"],
        "answer": "C"
    }
]

def run_quiz():
    print("\n🎉 Welcome to the Python Quiz App by AMAN DEEEP 🎉\n")
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! Correct answer is: {q['answer']}\n")

    print(f"🏁 Quiz Finished! Your final score is: {score}/{len(questions)}")
    print("📚 Thank you for playing! - AMAN DEEEP\n")

if __name__ == "__main__":
    run_quiz()
