from PySide6.QtWidgets import QApplication
# from PySide6.QtQuick import QQuickView
# from PySide6.QtCore import QUrl
from PySide6.QtUiTools import QUiLoader

from PySide6.QtWidgets import (
                                QLCDNumber,
                                QLineEdit, 
                                QMenu,
                                QPushButton,
                                QMessageBox,
                                QApplication,
                                QVBoxLayout, 
                                QDialog,
                                QListWidget,
                                QListWidgetItem,
                                QLabel,
                                QTableWidget,
                                QHBoxLayout,
                                QMessageBox,
                                QTableWidgetItem,
                                QWidget)
from PySide6.QtCore import Slot
from PySide6.QtCore import QFile
from PySide6.QtCore import Qt


import sys
import re
import random

class CB():
    def __init__(self, parent=None):
        #load ui
        ui_file = QFile("mainwindow.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        #init game
        self.gameInit()
        self.window.actionrule.triggered.connect(self.helpText)
        self.window.btnCheck.clicked.connect(self.CheckNum)
        self.window.btnRetry.clicked.connect(self.gameInit)
        self.window.show()

    def gameInit(self):         
        """
        
        """
     
        self.life =7
        self.window.tableWidget.clear()
        self.window.lcdNumber.display(self.life)
        self.Num0 = self.CreateNum()
        self.window.LEditResult.setText("")


    @staticmethod
    def CreateNum():
        """
        docstring
        """
        a = []
        while (len(a) < 4):
            x = random.randint(0, 9)
            if x not in a:
                a.append(x)
        print("New Num has created")
        return a
    @Slot()
    def helpText(self):
        print("Button clicked, Hello!")
        Qmsgb= QMessageBox.about(self.window,
        'rule',
'''        游戏规则很简单,就是猜数字游戏，直到猜对位置，随机给出四个数，且不重复。
根据系统的提示，猜对数字和数字位置则为A,猜对数字而没猜对位置则为B。\n
如：如果给出的数字为5246，你猜的数为5678，则会报出1A1B，因为5是位
置和数字都猜对了，另一个是6只猜对了数字没猜对位置，其他是位置和数字
都没猜对，所以为0A0B。\n
聪明的你明白规则了吗？明白了咱们就开始吧''')


    @Slot()
    def CheckNum(self):
        '''

        '''
        #enter check
        print(self.window.LEditNum.text())
        FourNumStr = self.window.LEditNum.text()
        str1 =  re.findall(r'\d+',FourNumStr)
        if(not self.IsInputNumOK(FourNumStr)):
            QMessageBox.about(self.window,'error','please enter again')
            return 
        FourNum=[]
        for num in str1:
            FourNum.append( int(num));
        Num1 = FourNum

      
        #compare and output    
        [a,b] = self.ABNum(self.Num0,Num1)  
       
        abstr = str(a)+'A'+str(b)+'B'
        entercell = QTableWidgetItem(FourNumStr)
    
        resultcell = QTableWidgetItem(abstr)
        self.window.tableWidget.setItem(7-self.life, 0, entercell)
        self.window.tableWidget.setItem(7-self.life, 1, resultcell)
        self.window.LEditResult.setReadOnly(False)
        self.window.LEditResult.setText( abstr)
        self.window.LEditResult.setReadOnly(True)

        if(self.ABNum(self.Num0,Num1)[0]==4):
            print("Win")
            QMessageBox.about(self.window,'win','game win\n')
            self.gameInit()
            return
               
        self.life=self.life-1
        self.window.lcdNumber.display(self.life)
        if(self.life==0):
            QMessageBox.about(self.window,'lose','game lose\nplease try again')
            self.gameInit
  

    @staticmethod
    def IsInputNumOK(str0):
        
        str1 =  re.findall(r'\d+',str0)
        print(str1)
        if( str1==[]):return False
        if (len(str1)!=4):
            return False
        for i in str1:
            if len(re.findall(i,str0)) >1:
                return False
        return True
    @staticmethod
    def ABNum(a,b):
        A= 0
        B=0
        for i in range(4):
            if(a[i]==b[i]):
                A = A+1
            if b[i] in a:
                B=B+1
        B= B-A
        print(A,"A",B,"B")
        return [A,B]
   
  
        

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    cb = CB()
    
 
    # Run the main Qt loop
    sys.exit(app.exec_())
