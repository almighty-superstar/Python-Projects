class Question:
   def __init__(self, prompt, answer):
       self.prompt=prompt
       self.answer=answer
        


question_prompts=[
    "What color are apples?\n(a) Red/green\n(b) Purple \n(c) Orange\n\n",
    "What is 3 times 3? \n(a) 5\n(b) 9\n(c) 15\n\n",
    "How many arms does a human have? \n(a) 2\n(b) 17\n(c) Octupus\n\n "
    ]
Question1=Question(question_prompts[0],"a")
Question2=Question(question_prompts[1],"b")
Question3=Question(question_prompts[2],"a")

def run_test(questions):
    print("Please answer with the choice letter only.")
    score=0
    answer=input(Question1.prompt)
    if answer==Question1.answer:
        score+=1
    answer=input(Question2.prompt)
    if answer==Question2.answer:
        score+=1
    answer=input(Question3.prompt)
    if answer==Question3.answer:
        score+=1
    print("You got "+ str(score)  +  " question(s) right!")
    if score==3:
        print("Congratulations you aced the quiz!")
run_test(question_prompts)