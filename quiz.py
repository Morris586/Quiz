
print("Welcome to my first ever quiz game!")

print("Answer the following questions by typing the correct multiple choice ")


quiz = [
    {"question": "Which month is christmas day on?", "options":["1. January", "2. April", "3. December", "4. July"], "answer": 3 },

    {"question": "Which programming language are you currently learning?", "options":["1.Python", "2.HTML", "3. CSS", "4. Java"], "answer": 1 },

    {"question": "What is the chemical symbol of water?", "options":["1. H2O, ", "2. H2", "3. CO2", "4. H2SO4"], "answer": 1},

    {"question": "Which is capital city of Japan?", "options":["1. Russia", "2. Helsinki", "3. Tokyo", "4. Nairobi"], "answer": 3},

    {"question": "Who is the most corrupt president in world?", "options":["1. Trump", "2.Putin", "3.Ruto aka kasongo", "4.Museveni"], "answer": 3},

    {"question": "Who is the most decorated author in Kenya", "options": ["1. Ken Walibora", "2.Ngugi wa thiongo", "3. Shakespear", "4. Musyoki"], "answer": 1},

]

def quiz_run():

    score = 0

    for i, q in enumerate(quiz):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        try:
            answer = int(input("What is your answer: "))
            if answer == q['answer']:
                print("Correct answer!")
                score += 1
            else:
                print("INvalid answer! The correct answer is", q['answer'], )

        except ValueError:
            print("Invalid input! Please input an integer")
    
    print(f"Your score is{score}")
    
    if score == len(quiz):
        print("Good work! You got all the questions correct.")
    elif score == len(quiz)/2:
        print("You can do better next time.")
    else:
        print("Be seriuos!")


if __name__ == '__main__':
    quiz_run()


