class QuizBrain():

    def __init__(self, questions_list):
        self.qnumber = 0
        self.qList = questions_list
        self.score = 0
    

    def nextQuestion(self):
        current_question = self.qList[self.qnumber]
        self.qnumber += 1
        user_choice = input(f"Otázka č. {self.qnumber}: {current_question.otazka} True/False: ")
        self.check_choice(user_choice, current_question.odpoved)
# 3. current_question dostane objekt dle indexu self.qnumber.. Diky metode .otazka dostaneme otazku (other.py)
    def check_choice(self, user, answer):
        if user.lower() == answer.lower():
            print("Správně")
            self.score += 1
        else:
            print(f"špatně, správná odpověd je {answer}")
        print(f"Vaše score je {self.score} / {self.qnumber}")
# 4. porovnává otázky, samo se spouští a bere si input od uživatele a metodu .odpoved (other.py) jako argumenty.
    def has_question(self):
        if self.qnumber < len(self.qList):
            return True
        else:
            return False