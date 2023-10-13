class QuizBrain:

    def __init__(self , qus_l ):
        self.qus_number = 0
        self.qus_list = qus_l
        self.score = 0

    def still_has_qus(self):
        return self.qus_number < len(self.qus_list)


    def next_qus(self) :
        current_qus= self.qus_list[self.qus_number]
        self.qus_number += 1
        user_answer=input(f"Q.{self.qus_number}:{current_qus.text} (True/False)")
        self.check_answer(user_answer,current_qus.answer)

    def check_answer(self , user_answer , correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it Right!")
        else:
            print("your dumb")  
        print(f"the correct answer was:{correct_answer}")   
        print(f"your current score is : {self.score}/{self.qus_number}") 
