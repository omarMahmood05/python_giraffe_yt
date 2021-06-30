from questions import questionClass

questions_List = [
    "What color are Apples? \n(a)Red \n(b)Pink \n(c)Black \n\n",
    "What color are Bananas? \n(a)Red \n(b)Pink \n(c)Yellow \n\n",
    "What color are Strawberries? \n(a)Red \n(b)Pink \n(c)Black \n\n",
]

questionsOList = [
    questionClass(questions_List[0], "a"),
    questionClass(questions_List[1], "c"),
    questionClass(questions_List[2], "a"),
]

def run_test(questionsOlist):
    score = 0
    for questionClass in questionsOlist:
        answer = input(questionClass.prompt)
        if answer == questionClass.answer:
            score += 1
    print("You got " + str(score) + " out of " +  str(len(questionsOlist)))


run_test(questionsOList)