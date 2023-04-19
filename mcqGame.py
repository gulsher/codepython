from Question import Question

questions_prompt = [
    "what is apple color?\n(a)Red\n(b)Green\n(c)Blue\n\n",
    "what is banana color?\n(a)Red\n(b)Green\n(c)yellow\n\n",
    "what is strawberry color?\n(a)Red\n(b)Green\n(c)yellow\n\n"
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "a")
]

def run_tests(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        
    print(score)

run_tests(questions)