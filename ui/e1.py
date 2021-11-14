import sys,os,pandas
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi
from caf.copyfiles import copyall
from crw.rwcon import write2config
#from time import sleep
from Run import run


tup=[]
sep,fc,filc,fname='',[],[],[]
class dummy(QMainWindow):
    def __init__(self):
        super(dummy,self).__init__()
        loadUi("ui/3.ui",self)
        self.Runner

    def Runner(self):
        copyall(tup[0],tup[1])
        write2config(tup[0],fc,sep,filc,fname)
        run(tup[0])


class MainWindow2(QMainWindow):
    def __init__(self,csvfile):
        super(MainWindow2,self).__init__()
        self.csv = csvfile
        self.setWindowIcon(QtGui.QIcon('ui/icon.ico'))
        self.setWindowTitle("GOOGLE DRIVE ORGANIZER")
        loadUi("ui/2.ui",self)
        print(self.csv+'\n')
        
        self.pushButton.clicked.connect(self.setfc)
        self.pushButton_2.clicked.connect(self.setsep)
        self.pushButton_3.clicked.connect(self.setfilecn)
        self.pushButton_4.clicked.connect(self.onOK)
        self.pushButton_5.clicked.connect(self.cloose)

    def cloose(self):
        sys.exit()

    def onOK(self):
        global widget
        global window2
        widget.removeWidget(window2)
        sec = dummy()
        widget.addWidget(sec)
        widget.setFixedWidth(500)
        widget.setFixedHeight(150)
        


    def setfc(self):
        global fc
        fc=list(map(int,str(self.lineEdit.text()).split()))
    def setsep(self):
        global sep
        sep=self.lineEdit_2.text()
    def setfilecn(self):
        global filc
        filc=[]
        global fname
        fname=[]
        temp=list(self.textEdit.toPlainText().split('\n'))
        print(temp)

        for i in temp:
            for j in range(len(i)):
                if i[j]==' ':
                    break
            a,b = i[:j],i[j+1:]

            filc.append(int(a))
            fname.append(b)


    def showcol(self):
        data = pandas.read_csv(self.csv, nrows=1)
        print(data)
        self.textBrowser.setText("Column Number and Heading for refrence.\n\n")
        n=1
        for i in data:
            self.textBrowser.setText(self.textBrowser.toPlainText()+str(f'{n}. {i}\n\n'))
            n+=1
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        loadUi("ui/1.ui",self)
        self.setWindowIcon(QtGui.QIcon('ui/icon.ico'))
        self.setWindowTitle("GOOGLE DRIVE ORGANIZER")
        
        self.pushButton.clicked.connect(self.browsefolder)
        self.pushButton_2.clicked.connect(self.browsefiles)
        self.pushButton_3.clicked.connect(self.onOK)
        self.pushButton_4.clicked.connect(self.cloose)

    

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Select CSV File', os.getcwd(), '*.csv')
        #print(fname)
        self.lineEdit_2.setText(fname[0])

    def browsefolder(self):
        fname=QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEdit.setText(fname)

    def onOK(self):
        global tup
        tup=[self.lineEdit.text(),self.lineEdit_2.text()]
        global widget
        global mainwindow
        widget.removeWidget(mainwindow)
        self.opennext(tup)

    def opennext(self,tup):
        global window2
        window2=MainWindow2(tup[1])
        window2.showcol()
        global widget
        widget.addWidget(window2)
        
        widget.setFixedWidth(900)
        widget.setFixedHeight(500)

    def cloose(self):
    	sys.exit()



def main():
    global app
    app=QApplication(sys.argv)
    global mainwindow
    mainwindow=MainWindow()

    global widget
    widget=QtWidgets.QStackedWidget()
    widget.setWindowTitle('GOOGLE DRIVE ORGANIZER')
    widget.setWindowIcon(QtGui.QIcon('ui/icon.ico'))
    widget.addWidget(mainwindow)
    widget.setFixedWidth(350)
    widget.setFixedHeight(250)
    widget.show()
    #widget.removeWidget(mainwindow)
    sys.exit(app.exec_())
    
    
    return tup

print(main())
