import pandas,sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi

sep,fc,filc,fname='',[],[],[]
class MainWindow(QMainWindow):
    def __init__(self,csvfile):
        super(MainWindow,self).__init__()
        self.csv=csvfile
        self.sep=""
        self.fc=[]
        self.filc=[]
        self.fname=[]
        loadUi("2.ui",self)
        print(self.csv+'\n')
        
        self.pushButton.clicked.connect(self.setfc)
        self.pushButton_2.clicked.connect(self.setsep)
        self.pushButton_3.clicked.connect(self.setfilecn)
        self.pushButton_4.clicked.connect(self.onOK)
        self.pushButton_5.clicked.connect(self.close)

    def close(self):
    	sys.exit()

    def onOK(self):
    	self.close()

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
	    
   
def main(csvd):
	app=QApplication(sys.argv)
	mainwindow=MainWindow(csvd)
	mainwindow.showcol()
	widget=QtWidgets.QStackedWidget()
	widget.addWidget(mainwindow)
	widget.setFixedWidth(900)
	widget.setFixedHeight(500)
	widget.show()
	sys.exit(app.exec_())

#main("C:/Users/Del/Desktop/GFO/temp/Enrollment Data CS-A2L, 2020-21.csv")


