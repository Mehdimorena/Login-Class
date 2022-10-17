import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLabel
from PyQt5.uic import loadUi

#load login ui
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)

        # set and aconnect Button and LineEdit
        self.loginbutton.clicked.connect(self.loginfunction)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    #send login information to backend
    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Successfully logged in with email: ", email, "and password:", password)

    # go to creat account function
    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

#load creataccount ui
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)

        # set and connect Button and LineEdit
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    # send creat acount information to backend
    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()