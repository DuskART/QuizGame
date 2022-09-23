from data import questions_list
from other import Question
from quizbrain import QuizBrain

questions_obs = []

for object in questions_list:
    object = Question(object["question"], object["answer"])
    questions_obs.append(object)
# 2. prevádí dicts na objekty

# 5. potřebuje list objektů jako argument pro init(quizbrain)
quiz = QuizBrain(questions_obs)

while quiz.has_question():
    quiz.nextQuestion()

print(f"konec, Vaše skore je {quiz.score} ze {quiz.qnumber}")