from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import randint, shuffle

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [
    Question('Official language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'),
    Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'),
    Question('Yakut national house', 'Urasa', 'Yurta', 'Igloo', 'Khata')]

app = QApplication([])
btn_OK = QPushButton('Reply')
lb_Question = QLabel('The most difficult question in the world!')
RadioGroupBox = QGroupBox('Answer options')
rbtn_1, rbtn_2, rbtn_3, rbtn_4 = [QRadioButton('Option ' + str(i)) for i in range(1, 5)]
RadioGroup = QButtonGroup()
for button in (rbtn_1, rbtn_2, rbtn_3, rbtn_4):
    RadioGroup.addButton(button)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Test results')
lb_Result = QLabel('are you right or not?')
lb_Correct = QLabel('answer will be here!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Reply')
    RadioGroup.setExclusive(False)
    for button in (rbtn_1, rbtn_2, rbtn_3, rbtn_4):
        button.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
    shuffle(answers)
    for button, answer in zip(answers, (q.right_answer, q.wrong1, q.wrong2, q.wrong3)):
        button.setText(answer)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Right!')
        window.score += 1
        print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
        print('Rating: ', window.score / window.total * 100, '%')
    elif any(button.isChecked() for button in answers[1:]):
        show_correct('Wrong answer!')
        print('Rating: ', window.score / window.total * 100, '%')

def next_question():
    window.total += 1
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)
    ask(questions_list[randint(0, len(questions_list) - 1)])

def click_OK():
    if btn_OK.text() == 'Reply':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
