class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer # 1 ~ 4
        self.hint = hint

    def show(self): # 문제와 선택지 출력
        print(f"\n{self.question}")

        for i, choice in enumerate(self.choices, start=1):
            print(" "*5 + f"{i}, {choice}")

    def check(self,user_answer): # 정답 확인
        return user_answer == self.answer

    
