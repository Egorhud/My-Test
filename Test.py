from PyQt5 import Qt
from PyQt5.QtWidgets import*

app = QApplication([])



window = QWidget()
window.setWindowTitle('Окошко для горошка')
window.move(300,5)
window.resize(300,300)
name = QLabel('Введіть імя')
name2 = QLineEdit()

label = QLabel('что такое Scratch?')
r1=QRadioButton('еда ')
r2=QRadioButton('человек')
r3=QRadioButton('для создания проєктов')
q1=QButtonGroup()
q1.addButton(r1)
q1.addButton(r2)
q1.addButton(r3)
labell = QLabel('Де в Харкові знаходиться пам’ятник програмісту?')
ch1=QRadioButton('Перед входом в Харківський національний університет радіоелектроніки')
ch2=QRadioButton('В Росии')
ch3=QRadioButton('На луне')
q2=QButtonGroup()
q2.addButton(ch1)
q2.addButton(ch2)
q2.addButton(ch3)
labelll = QLabel('Что такое Java?')
b1=QRadioButton('язик прогромирования')
b2=QRadioButton('что это вообще?')
b3=QRadioButton('заклинание')
q3=QButtonGroup()
q3.addButton(b1)
q3.addButton(b2)
q3.addButton(b3)

button=QPushButton('Відповісти')



h=QHBoxLayout()
h1=QHBoxLayout()
h2=QHBoxLayout()
h3=QHBoxLayout()

v=QVBoxLayout()

h.addWidget(name)
h.addWidget(name2)

h1.addWidget(r1)
h1.addWidget(r2)
h1.addWidget(r3)

h2.addWidget(ch1)
h2.addWidget(ch2)
h2.addWidget(ch3)

h3.addWidget(b1)
h3.addWidget(b2)
h3.addWidget(b3)

v.addLayout(h)
v.addWidget(label)
v.addLayout(h1)
v.addWidget(labell)
v.addLayout(h2)
v.addWidget(labelll)
v.addLayout(h3)
v.addWidget(button)
window.setLayout(v)
def test():
    save =0
    if r3.isChecked():
        save = save+4
    if ch1.isChecked():
        save=save+4
    if b1.isChecked():
        save=save+4
    answer = QMessageBox()
    answer.setWindowTitle('Результат')
    answer.setText(name2.text()+" - "+str(save))
    with open('resaut.txt', 'a' ,encoding='UTF-8') as file:
        file.write(name2.text()+" - "+str(save)+"\n")
    answer.show()
    answer.exec()
button.clicked.connect(test)

window.show()
app.exec_()
