import sys
from PyQt5.QtWidgets import(
    QWidget,
    QApplication,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5 import QtCore
from PyQt5.QtGui import QColor

class calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle('Calculator')
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.black)
        self.setPalette(p)
        

        self.display=QLineEdit(self)
        self.display.setAlignment(QtCore.Qt.AlignRight)

        self.zero_btn=QPushButton('0')
        self.zero_btn.setStyleSheet("background-color : blue")
        self.one_btn=QPushButton('1')
        self.one_btn.setStyleSheet("background-color : blue")
        self.two_btn=QPushButton('2')
        self.two_btn.setStyleSheet("background-color : blue")
        self.three_btn=QPushButton('3')
        self.three_btn.setStyleSheet("background-color : blue")
        self.four_btn=QPushButton('4')
        self.four_btn.setStyleSheet("background-color : blue")
        self.five_btn=QPushButton('5')
        self.five_btn.setStyleSheet("background-color : blue")
        self.six_btn=QPushButton('6')
        self.six_btn.setStyleSheet("background-color : blue")
        self.seven_btn=QPushButton('7')
        self.seven_btn.setStyleSheet("background-color : blue")
        self.eight_btn=QPushButton('8')
        self.eight_btn.setStyleSheet("background-color : blue")
        self.nine_btn=QPushButton('9')
        self.nine_btn.setStyleSheet("background-color : blue")
        self.divide_btn=QPushButton('/')
        self.divide_btn.setStyleSheet("background-color : red")
        self.multi_btn=QPushButton('*')
        self.multi_btn.setStyleSheet("background-color : red")
        self.add_btn=QPushButton('+')        
        self.add_btn.setStyleSheet("background-color : red")
        self.div_btn=QPushButton('-')   
        self.div_btn.setStyleSheet("background-color : red")
        self.equal_btn=QPushButton('=')
        self.equal_btn.setStyleSheet("background-color : red")
        
        self.v_box=QVBoxLayout()
        self.h_box=QHBoxLayout()
        self.h_box2=QHBoxLayout()
        self.h_box3=QHBoxLayout()
        self.h_box4=QHBoxLayout()
        self.h_boxl=QHBoxLayout()
    
        self.h_boxl.addWidget(self.display)
        
        self.h_box.addWidget(self.one_btn)  
        self.h_box.addWidget(self.two_btn)  
        self.h_box.addWidget(self.three_btn)  
        self.h_box.addWidget(self.divide_btn)
        
        self.h_box2.addWidget(self.four_btn)
        self.h_box2.addWidget(self.five_btn)
        self.h_box2.addWidget(self.six_btn)
        self.h_box2.addWidget(self.multi_btn)
        
        self.h_box3.addWidget(self.seven_btn)
        self.h_box3.addWidget(self.eight_btn)
        self.h_box3.addWidget(self.nine_btn)
        self.h_box3.addWidget(self.div_btn)
        
        self.h_box4.addWidget(self.zero_btn)
        self.h_box4.addWidget(self.equal_btn)
        self.h_box4.addWidget(self.add_btn)
        
        self.v_box.addLayout(self.h_boxl)
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        
        self.setLayout(self.v_box)
        
        self.one_btn.clicked.connect(self.one_click)
        self.two_btn.clicked.connect(self.two_click)
        self.three_btn.clicked.connect(self.three_click)
        self.four_btn.clicked.connect(self.four_click)
        self.five_btn.clicked.connect(self.five_click)
        self.six_btn.clicked.connect(self.six_click)
        self.seven_btn.clicked.connect(self.seven_click)
        self.eight_btn.clicked.connect(self.eight_click)
        self.nine_btn.clicked.connect(self.nine_click)
        self.zero_btn.clicked.connect(self.zero_click)
        self.divide_btn.clicked.connect(self.divide_click)
        self.multi_btn.clicked.connect(self.multi_click)
        self.add_btn.clicked.connect(self.add_click)
        self.div_btn.clicked.connect(self.div_click)
        self.equal_btn.clicked.connect(self.equal_click)
        
        self.strr=str()
        self.strr2=str()
        
    def one_click(self):
        self.strr+='1'
        self.strr2+='1'
        self.display.setText(self.strr)
        
    def two_click(self):
        self.strr+='2'
        self.strr2+='2'
        self.display.setText(self.strr)
        
    def three_click(self):
        self.strr+='3'
        self.strr2+='3'
        self.display.setText(self.strr)
        
    def four_click(self):
        self.strr+='4'
        self.strr2+='4'
        self.display.setText(self.strr)
        
    def five_click(self):
        self.strr+='5'
        self.strr2+='5'
        self.display.setText(self.strr)
        
    def six_click(self):
        self.strr+='6'
        self.strr2+='6'
        self.display.setText(self.strr)
        
    def seven_click(self):
        self.strr+='7'
        self.strr2+='7'
        self.display.setText(self.strr)
        
    def eight_click(self):
        self.strr+='8'
        self.strr2+='8'
        self.display.setText(self.strr)
        
    def nine_click(self):
        self.strr+='9'
        self.strr2+='9'
        self.display.setText(self.strr)
        
    def zero_click(self):
        self.strr+='0'
        self.strr2+='0'
        self.display.setText(self.strr)    
        
    def divide_click(self):
        if len(self.strr)>1:
            if self.strr[len(self.strr)-1] not in ['*','/','+','-']:
                self.strr+='/'
                self.strr2+=',/,'
                self.display.setText(self.strr)
        elif len(self.strr)==1: 
            if self.strr[0]!='-':
                self.strr+='/'
                self.strr2+=',/,'
                self.display.setText(self.strr)
            
    def multi_click(self):
        if len(self.strr)>1:
            if self.strr[len(self.strr)-1] not in ['*','/','+','-']:
                self.strr+='*'
                self.strr2+=',*,'
                self.display.setText(self.strr)
        elif len(self.strr)==1:
            if self.strr[0]!='-':
                self.strr+='*'
                self.strr2+=',*,'
                self.display.setText(self.strr)
            
        
    def add_click(self):
        if len(self.strr)>1: 
            if self.strr[len(self.strr)-1] not in ['*','/','+','-']:
                self.strr+='+'
                self.strr2+=',+,'
                self.display.setText(self.strr)
        elif len(self.strr)==1:
            if self.strr[0]!='-':
                self.strr+='+'
                self.strr2+=',+,'
                self.display.setText(self.strr)
            
        
    def div_click(self):
        if len(self.strr)>0:
            if len(self.strr)==1:
                if self.strr[0]!='-':
                    self.strr+='-'
                    self.strr2+=',-,'
                    self.display.setText(self.strr)
            elif self.strr[len(self.strr)-2] not in ['-', '+', '*', '/'] or self.strr[len(self.strr)-1] not in ['-', '+', '*', '/']:
                if self.strr[len(self.strr)-1] in ['-', '+', '*', '/']:
                    self.strr2+='-'
                else:
                    self.strr2+=',-,'
                self.strr+='-'
                self.display.setText(self.strr)
        elif len(self.strr)==0:
            self.strr+='-'
            self.strr2+='-'
            self.display.setText(self.strr)
        
    def equal_click(self):
        self.temp1=self.strr2.split(',')
        while self.temp1.count(''):
            self.temp1.remove('')
            
        if len(self.temp1)<3: 
            self.display.setText('')
            self.strr=str()
            self.strr2=str()
            return
        elif len(self.temp1)==3 and self.temp1[2] in ['+', '-', '*', '-']:
            self.display.setText('')
            self.strr=str()
            self.strr2=str()
            return
            
        while self.temp1[len(self.temp1)-1] in ['-', '*', '/', '+']:
            self.temp1.pop(-1)
            
        while self.temp1.count('/'):
            ind=self.temp1.index('/')
            try:
                self.temp1[ind]=float(self.temp1[ind-1])/float(self.temp1[ind+1])
            except ZeroDivisionError: 
                self.display.setText("0 ga bo'lib bo'lmaydi!")
                self.strr=str()
                self.strr2=str()
                return 
            self.temp1.pop(ind-1)
            self.temp1.pop(ind)
            
        while self.temp1.count('*'):
            ind=self.temp1.index('*')
            self.temp1[ind]=float(self.temp1[ind-1])*float(self.temp1[ind+1])
            self.temp1.pop(ind-1)
            self.temp1.pop(ind)
        
        while self.temp1.count('-'):
            ind=self.temp1.index('-')
            self.temp1[ind]=float(self.temp1[ind-1])-float(self.temp1[ind+1])
            self.temp1.pop(ind-1)
            self.temp1.pop(ind)
        
        while self.temp1.count('+'):
            ind=self.temp1.index('+')
            self.temp1[ind]=float(self.temp1[ind-1])+float(self.temp1[ind+1])
            self.temp1.pop(ind-1)
            self.temp1.pop(ind)
        
        calculation=self.temp1[0]

        self.display.setText(str(calculation))
        self.strr2=str()
        self.strr=str()
        
        
app=QApplication([])
win=calculator()
win.show()
app.exec_()
sys.exit()
    

    

