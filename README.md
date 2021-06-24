![img](https://github.com/ytWu1314/Ecard/blob/master/readme_images/Logo.png)



 <h3 align = "center"> 院系：计算机学院 专业：计算机科学与技术</h3>

<h3 align = "center"> 姓名：吴宇涛 学号：20192131089</h3>

<h3 align = "center">课程：初级软件实作</h3>

<h3 align = "center"> 项目：制作电子贺卡</h3>

 <h3 align = "center"> 班级：19级 2班</h3>

<h3 align = "center">指导老师：王涛 </h3>





# 开发过程

## 	1.如何设计：

​		本程序由三个.py文件构成，分别为UI界面、信号与槽函数，逻辑功能、主函数。

​		① 使用Qt Designer 将自己头脑中构思的电子贺卡UI界面通过一系列的控件设计出来，并不断调整UI界面使其更美观。在源程序文件夹中通过输入一下命令`pyuic5 -o ui_MainWindow.py  MainWindow.ui`  把designer 设计出来的MainWindow.ui转化成可以运行的ui_MainWindow.py文件。 

​		② 新建myMainWindow.py文件，在VSCODE中实现各个控件的逻辑，通过设置信号与槽函数，实现点击触发事件。

​		③ 新建appMain.py 文件，实现主函数，显示主窗体



​		![设计流程图](https://github.com/ytWu1314/Ecard/blob/master/readme_images/%E8%AE%BE%E8%AE%A1%E6%B5%81%E7%A8%8B%E5%9B%BE.png)



## 	2.如何实现

​		`ui_MainWindow.py` 实现电子贺卡的UI界面

```python
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.imgName =[]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 541)
        #禁止窗口最大化
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        #setWindowFlags(Qt.WindowMinimizeButtonHint)
        #setWindowFlags(Qt.WindowCloseButtonHint)  
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget") 
        #初始化lab1图片
        self.lab1 = QtWidgets.QLabel(self.centralWidget)
        self.lab1.setGeometry(QtCore.QRect(10, 50, 480, 480))
        self.lab1.setText("")
        self.lab1.setObjectName("lab1")
        self.lab1.setPixmap(QPixmap("./extarn/photo1.png"))
        op = QtWidgets.QGraphicsOpacityEffect()
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.lab1.setGraphicsEffect(op)

        font = QtGui.QFont()
        font.setFamily("蝉羽真颜金戈") #括号里可以设置成自己想要的其它字体
        font.setPointSize(20)   #括号里的数字可以设置成自己想要的字体大小

        #文本框
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 480, 480))
        self.textEdit.setPlaceholderText("请输入正文")
        self.textEdit.setStyleSheet("QTextEdit{color: black; background-color: transparent; border:1px solid black;}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        
        #布局
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 20, 741, 511))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAdd = QtWidgets.QPushButton(self.groupBox)

        #按钮控件以及图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/images/316.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 0, 0, 1, 2)
        self.btnRemove = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/images/318.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemove.setIcon(icon1)
        self.btnRemove.setObjectName("btnRemove")
        self.gridLayout.addWidget(self.btnRemove, 0, 2, 1, 3)
        self.btnClear = QtWidgets.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/images/214.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon2)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 0, 5, 1, 3)
        self.selectbtn = QtWidgets.QPushButton(self.groupBox)
        self.selectbtn.setObjectName("selectbtn")
        self.gridLayout.addWidget(self.selectbtn, 0, 8, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")

        #音乐播放列表
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 5)

        #图片播放列表
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 2, 5, 1, 5)
        
        self.btnPlay = QtWidgets.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/images/620.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon3)
        self.btnPlay.setObjectName("btnPlay")
        self.gridLayout.addWidget(self.btnPlay, 3, 0, 1, 1)
        self.btnPause = QtWidgets.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./icons/images/622.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon4)
        self.btnPause.setObjectName("btnPause")
        self.gridLayout.addWidget(self.btnPause, 3, 1, 1, 2)
        self.btnStop = QtWidgets.QPushButton(self.groupBox)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./icons/images/624.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon5)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 3, 3, 1, 1)
        self.btnPrevious = QtWidgets.QPushButton(self.groupBox)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./icons/images/616.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrevious.setIcon(icon6)
        self.btnPrevious.setObjectName("btnPrevious")
        self.gridLayout.addWidget(self.btnPrevious, 3, 4, 1, 2)
        self.btnNext = QtWidgets.QPushButton(self.groupBox)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./icons/images/630.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon7)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 3, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 7, 1, 1)
        self.sliderVolumn = QtWidgets.QSlider(self.groupBox)
        self.sliderVolumn.setMaximum(100)
        self.sliderVolumn.setProperty("value", 100)
        self.sliderVolumn.setOrientation(QtCore.Qt.Horizontal)
        self.sliderVolumn.setObjectName("sliderVolumn")
        self.gridLayout.addWidget(self.sliderVolumn, 3, 9, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #曲目
        self.LabCurMedia = QtWidgets.QLabel(self.groupBox)
        self.LabCurMedia.setMinimumSize(QtCore.QSize(100, 0))
        self.LabCurMedia.setObjectName("LabCurMedia")
        self.horizontalLayout_2.addWidget(self.LabCurMedia)

        #音乐进度条
        self.sliderPosition = QtWidgets.QSlider(self.groupBox)
        self.sliderPosition.setTracking(False)
        self.sliderPosition.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPosition.setObjectName("sliderPosition")
        self.horizontalLayout_2.addWidget(self.sliderPosition)

        #音量进度条
        self.LabRatio = QtWidgets.QLabel(self.groupBox)
        self.LabRatio.setMinimumSize(QtCore.QSize(80, 0))
        self.LabRatio.setObjectName("LabRatio")
        self.horizontalLayout_2.addWidget(self.LabRatio)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 10)

        self.btnSound = QtWidgets.QPushButton(self.groupBox)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./icons/images/volumn.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSound.setIcon(icon8)
        self.btnSound.setFlat(True)
        self.btnSound.setObjectName("btnSound")
        self.gridLayout.addWidget(self.btnSound, 3, 8, 1, 1)

        #标题框
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 480, 35))
        self.lineEdit.setPlaceholderText("请输入标题")
        self.lineEdit.setAlignment(Qt.AlignHCenter)
        self.lineEdit.setStyleSheet("QLineEdit{color: black; background-color: transparent; border:1px solid black;}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo10_1，音乐播放器"))
        self.groupBox.setTitle(_translate("MainWindow", "播放列表"))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnRemove.setText(_translate("MainWindow", "移除"))
        self.btnClear.setText(_translate("MainWindow", "清空"))
        self.selectbtn.setText(_translate("MainWindow", "选择图片"))
        self.label_2.setText(_translate("MainWindow", "音乐播放列表"))
        self.label_3.setText(_translate("MainWindow", "背景图片列表"))
        self.btnPlay.setToolTip(_translate("MainWindow", "播放"))
        self.btnPlay.setText(_translate("MainWindow", "播放"))
        self.btnPause.setToolTip(_translate("MainWindow", "暂停"))
        self.btnPause.setText(_translate("MainWindow", "暂停"))
        self.btnStop.setToolTip(_translate("MainWindow", "停止"))
        self.btnStop.setText(_translate("MainWindow", "停止"))
        self.btnPrevious.setToolTip(_translate("MainWindow", "前一曲目"))
        self.btnPrevious.setText(_translate("MainWindow", "上一首"))
        self.btnNext.setToolTip(_translate("MainWindow", "下一曲目"))
        self.btnNext.setText(_translate("MainWindow", "下一首"))
        self.LabCurMedia.setText(_translate("MainWindow", "无曲目"))
        self.LabRatio.setText(_translate("MainWindow", "进度"))
        self.btnSound.setText(_translate("MainWindow", "音量"))

```

`myMainWindow.py` 

* 使用 QMediaPlayer 和 QMediaPlaylist 播放 mp3 等音频文件。
* 使用 setPixmap 函数实现 listview中的列表映射到lab上
* 使用python json、txt文件读写 实现保存读取功能。

```python
import sys,json,os
from typing import Counter, List
from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.sip import dump
import cv2
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QUndoView,
                             QLabel, QListView, QVBoxLayout, QHBoxLayout,
                             QMenuBar, QMenu, QAction,
                             QUndoStack, QUndoCommand, QStyle)

from PyQt5.QtWidgets import  (QApplication, QMainWindow,QFileDialog,
                         QAbstractItemView,  QMessageBox,QDataWidgetMapper)

from PyQt5.QtCore import  (pyqtSlot, Qt,QItemSelectionModel,
                         QModelIndex,QFile,QIODevice)
                                                      
from PyQt5.QtWidgets import  QApplication, QMainWindow,QFileDialog,QListWidgetItem

from PyQt5.QtCore import  pyqtSlot,QItemSelectionModel,QUrl,QModelIndex,QDir,QFileInfo

from PyQt5.QtGui import QIcon

from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist,QMediaContent
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord  

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow,QUndoCommand):    
   def __init__(self, parent=None):        
      super(QmyMainWindow,self).__init__(parent)   #调用父类构造函数，创建窗体

      self.imgName=[]
      self.fileList=[]
      self.ui=Ui_MainWindow()    #创建UI对象
      self.ui.setupUi(self)      #构造UI界面   
      op1 = QtWidgets.QGraphicsOpacityEffect()
      op1.setOpacity(0.5)
      op2 = QtWidgets.QGraphicsOpacityEffect()
      op2.setOpacity(0.5)
      op3 = QtWidgets.QGraphicsOpacityEffect()
      op3.setOpacity(0.5)
      # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
      self.pushButton = QtWidgets.QPushButton(self)
      self.pushButton.setGeometry(QtCore.QRect(40, 490, 121, 28))
      self.pushButton.setObjectName("pushButton")
      self.pushButton_2 = QtWidgets.QPushButton(self)
      self.pushButton_2.setGeometry(QtCore.QRect(320, 490, 121, 28))
      self.pushButton_2.setObjectName("pushButton_3")
      self.pushButton.setText("读取")

      self.pushButton_2.setText("保存")

      self.pushButton.setGraphicsEffect(op1) 
      self.pushButton_2.setGraphicsEffect(op2)

      self.pushButton.clicked.connect(self.on_pushButton1_clicked)
      self.pushButton_2.clicked.connect(self.on_pushButton2_clicked)
      
      self.ui.listView.setContextMenuPolicy(Qt.CustomContextMenu)#右键菜单
      self.ui.listView.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)
      self.ui.selectbtn.clicked.connect(self.openimage)
      self.ui.listView.doubleClicked.connect(self.clicked)
      self.ui.listView.clicked.connect(self.clicked)

      self.setWindowTitle("电子贺卡")
      self.setWindowIcon(QIcon('ecard.ico'))
      self.player = QMediaPlayer(self)
      self.playlist = QMediaPlaylist(self)
      self.player.setPlaylist(self.playlist)
      self.playlist.setPlaybackMode(QMediaPlaylist.Loop)    #循环模式

      self.__duration=""      #文件总时间长度
      self.__curPos=""        #当前播放到位置

      self.player.stateChanged.connect(self.do_stateChanged)
      
      self.player.positionChanged.connect(self.do_positionChanged)
      
      self.player.durationChanged.connect(self.do_durationChanged)
      
      self.playlist.currentIndexChanged.connect(self.do_currentChanged)

   
    # 按钮一：读取数据
   def on_pushButton1_clicked(self):
      with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto.json','r') as x:
         self.imgName=json.load(x)
      self.slm = QStringListModel()
      self.slm.setStringList(self.imgName)
      self.ui.listView.setModel(self.slm) 

      self.playlist.clear()   #清空播放列表
      self.ui.listWidget.clear()  
      self.player.stop()      #停止播放
      with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savemusic.json','r') as n:
         self.fileList=json.load(n)
      self.count=len(self.fileList)   
      print(self.count)
      curPath=QDir.currentPath()
      dlgTitle="选择音频文件" 
      filt="音频文件(*.mp3 *.wav *.wma);;所有文件(*.*)" 
      count=len(self.fileList)
      if count<1:
         return
      filename=self.fileList[0]
      fileInfo=QFileInfo(filename)  #文件信息
      QDir.setCurrent(fileInfo.absolutePath())  #重设当前路径

      for i in range(count):
         filename=self.fileList[i]
         fileInfo.setFile(filename)
         song=QMediaContent(QUrl.fromLocalFile(filename))
         self.playlist.addMedia(song)  #添加播放媒体
   ##         basename=os.path.basename(filename)    #文件名和后缀
         basename=fileInfo.baseName()
         self.ui.listWidget.addItem(basename)    #添加到界面文件列表

      self.text1=''
      with open("C:/Users/PC_SKY_WYT/Desktop/PyQt/textEdit.txt",encoding='utf-8',mode='r+') as q:
         self.text1=q.read()
      self.ui.textEdit.setText(self.text1)  

      self.line1=''
      with open("C:/Users/PC_SKY_WYT/Desktop/PyQt/textEdit.txt",encoding='utf-8',mode='r+') as z:
         self.line1=z.read()
      self.ui.lineEdit.setText(self.line1)  
          
    # 按钮二：保存功能
   def on_pushButton2_clicked(self):
      self.str1=self.ui.textEdit.toPlainText()
      with open("C:/Users/PC_SKY_WYT/Desktop/PyQt/textEdit.txt",encoding='utf-8',mode='w+') as p:
         p.write(self.str1)
      self.str2=self.ui.lineEdit.text()
      with open("C:/Users/PC_SKY_WYT/Desktop/PyQt/lineEdit.txt",encoding='utf-8',mode='w+') as x:
         x.write(self.str2)   

   def rightMenuShow(self):
      rightMenu = QtWidgets.QMenu(self.ui.listView)
      removeAction = QtWidgets.QAction(u"Delete", self, triggered=self.removeimage)       # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
      rightMenu.addAction(removeAction)
      rightMenu.exec_(QtGui.QCursor.pos())

   def openimage(self):  
        img=[]
        self.imgName,imgType = QtWidgets.QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
        slm = QStringListModel()
        slm.setStringList(self.imgName)
        self.ui.listView.setModel(slm)
        if not os.path.exists('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto.json'):
           templist=[]
           with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto.json','w+') as a:
              json.dump(templist,a)  
        else :      
         with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto.json',mode='r') as x:
            img=json.load(x)

        with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto.json','w+') as a:
           json.dump(self.imgName,a)             
   
        with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto2.json','w+') as m:
           json.dump(img,m)     

   def clicked(self,qModelIndex):
        #QMessageBox.information(self, "QListView", "你选择了: "+ imgName[qModelIndex.row()])
        global path
        pic=QPixmap(QPixmap(self.imgName[qModelIndex.row()]))
        W=self.ui.lab1.width()
        self.ui.lab1.setPixmap(pic.scaledToWidth(W)) #在界面上显示
        path = self.imgName[qModelIndex.row()]

   def removeimage(self):
         selected = self.ui.listView.selectedIndexes()
         selectindex = self.ui.listView.currentIndex()
         itemmodel = self.ui.listView.model()
         x=0
         for i in selected:
            x=i.row()
            itemmodel.removeRow(i.row()) 
            cnt=itemmodel.rowCount()           
         for i in range(x,cnt):
            self.imgName[i]=self.imgName[i+1]    

   def save_quit(self):
      self.save()      
      qApp.quit()

      
##  ==============自定义功能函数============

##  ===============event 处理函数==========
   def closeEvent(self,event):  ##窗体关闭时
##  窗口关闭时不能自动停止播放，需手动停止
      if (self.player.state()==QMediaPlayer.PlayingState):
         self.player.stop()

         
        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
#  播放列表管理
   @pyqtSlot()    ##添加文件
   def on_btnAdd_clicked(self):  
      self.playlist.clear()   #清空播放列表
      self.ui.listWidget.clear()  
      self.player.stop()      #停止播放
      self.List=[] 
      curPath=QDir.currentPath()
      dlgTitle="选择音频文件" 
      filt="音频文件(*.mp3 *.wav *.wma);;所有文件(*.*)" 
      fileList,flt=QFileDialog.getOpenFileNames(self,dlgTitle,curPath,filt)
      count=len(fileList)
      if count<1:
         return
      filename=fileList[0]
      fileInfo=QFileInfo(filename)  #文件信息
      QDir.setCurrent(fileInfo.absolutePath())  #重设当前路径

      for i in range(count):
         filename=fileList[i]
         self.List.append(filename) 
         fileInfo.setFile(filename)
         song=QMediaContent(QUrl.fromLocalFile(filename))
         self.playlist.addMedia(song)  #添加播放媒体
   ##         basename=os.path.basename(filename)    #文件名和后缀
         basename=fileInfo.baseName()
         self.ui.listWidget.addItem(basename)    #添加到界面文件列表

      print(self.List)   
      with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savemusic.json','w+') as f:
         json.dump(self.List,f)         
            
      if (self.player.state()!=QMediaPlayer.PlayingState):
         self.playlist.setCurrentIndex(0)
         self.player.play()    
     
   @pyqtSlot()    ##移除一个文件
   def on_btnRemove_clicked(self): 
      pos=self.ui.listWidget.currentRow()
      item=self.ui.listWidget.takeItem(pos)     #python会自动删除

      if (self.playlist.currentIndex()==pos):   #是当前播放的曲目
         nextPos=0
         if pos>=1:
            nextPos=pos-1

         self.playlist.removeMedia(pos)   #从播放列表里移除
         if self.ui.listWidget.count()>0: #剩余个数
            self.playlist.setCurrentIndex(nextPos)
            self.do_currentChanged(nextPos)  #当前曲目变化
         else:
            self.player.stop()
            self.ui.LabCurMedia.setText("无曲目")
      else:
         self.playlist.removeMedia(pos)
      

   @pyqtSlot()    ##清空播放列表
   def on_btnClear_clicked(self):  
      self.playlist.clear()   #清空播放列表
      self.ui.listWidget.clear()  
      self.player.stop()      #停止播放
      
   ##   @pyqtSlot()    ##双击时切换播放文件
   def on_listWidget_doubleClicked(self,index):  
      rowNo=index.row()  #行号
      self.playlist.setCurrentIndex(rowNo)
      self.player.play()
      

#  播放控制
   @pyqtSlot()    ##播放
   def on_btnPlay_clicked(self):  
      if (self.playlist.currentIndex()<0):
         self.playlist.setCurrentIndex(0)
      self.player.play()

   @pyqtSlot()    ##暂停
   def on_btnPause_clicked(self):  
      self.player.pause()

   @pyqtSlot()    ##停止
   def on_btnStop_clicked(self):  
      self.player.stop()

   @pyqtSlot()    ##上一曲目
   def on_btnPrevious_clicked(self):  
      self.playlist.previous()

   @pyqtSlot()    ##下一曲目
   def on_btnNext_clicked(self):  
      self.playlist.next()

   @pyqtSlot()    ##静音控制
   def on_btnSound_clicked(self):  
      mute=self.player.isMuted()
      self.player.setMuted(not mute)
      if mute:
         self.ui.btnSound.setIcon(QIcon("./images/volumn.bmp"))
         self.ui.btnSound.setText("音量")
      else:
         self.ui.btnSound.setIcon(QIcon("./images/mute.bmp"))
         self.ui.btnSound.setText("静音")
      
   @pyqtSlot(int)    ##调节音量
   def on_sliderVolumn_valueChanged(self,value):  
      self.player.setVolume(value)

   @pyqtSlot(int)    ##文件进度调控
   def on_sliderPosition_valueChanged(self,value):  
      self.player.setPosition(value)
      

##  =============自定义槽函数===============================        
   def do_stateChanged(self,state):    ##播放器状态变化
      self.ui.btnPlay.setEnabled(state!=QMediaPlayer.PlayingState)
      self.ui.btnPause.setEnabled(state==QMediaPlayer.PlayingState)
      self.ui.btnStop.setEnabled(state==QMediaPlayer.PlayingState)

   def do_positionChanged(self,position): ##当前文件播放位置变化，更新进度显示
      if (self.ui.sliderPosition.isSliderDown()): #在拖动滑块调整进度
         return
      self.ui.sliderPosition.setSliderPosition(position)
      secs=position/1000   #秒
      mins=secs/60         #分钟
      secs=secs % 60       #余数秒
      self.__curPos="%d:%d"%(mins,secs)
      self.ui.LabRatio.setText(self.__curPos+"/"+self.__duration)

   def do_durationChanged(self,duration):    ##文件时长变化
      self.ui.sliderPosition.setMaximum(duration)

      secs=duration/1000   #秒
      mins=secs/60         #分钟
      secs=secs % 60       #余数秒
      self.__duration="%d:%d"%(mins,secs)
      self.ui.LabRatio.setText(self.__curPos+"/"+self.__duration)

   def do_currentChanged(self,position):  ##playlist当前曲目变化
      self.ui.listWidget.setCurrentRow(position)
      item=self.ui.listWidget.currentItem()  #QListWidgetItem
      if (item != None):
         self.ui.LabCurMedia.setText(item.text())

##  ============窗体测试程序 ================================
if  __name__ == "__main__":         #用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form=QmyMainWindow()            #创建窗体
    form.show()
    sys.exit(app.exec_())

```

## 	3.如何检查系统功能	

​		通过测试按钮控件，测试音乐的添加，移除，清空，测试图片的选择和删除，程序所有数据的保存读写来检测此程序是否正常运行。



# 设计方案

## 	1.功能组成

（1） 用户可在软件中选择背景:要求能列出可选的背景图片

![image-20210611012218909](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012218909.png)



（2） 用户可在软件中输入标题

![image-20210611012519501](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012519501.png)

（3） 用户可在软件中输入贺卡中的文字

![image-20210611012556140](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012556140.png)

（4） 用户可在软件中选择贺卡的伴奏音乐

![image-20210611012435236](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012435236.png)

（5） 用户可保存贺卡（即保存后关闭程度后，可以重新打开、播放）

![image-20210611012850660](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012850660.png)

## 	2.界面组成

标题框：QLineEdit

![image-20210611012925640](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012925640.png)

正文框：QTextEdit

![image-20210611012914988](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012914988.png)

音乐列表：QListWidget

![image-20210611013006008](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611013006008.png)

背景图片列表：QListView

![image-20210611012944964](https://github.com/ytWu1314/Ecard/blob/master/readme_images/image-20210611012944964.png)

按钮控件：QPushButton

## 	3.算法、数据结构

使用了python的线性结构list列表，存储图片列表以及音乐播放列表。添加删除等功能都是在列表中跌代取出。



# 技术讨论

## 	1.存在问题

没有实现如：”在这里的每一个步骤，都可以回到上一步，并且再设置向前后步骤走时，原来的设置不会被清除“的功能。

控件不够美观，窗口最大化布局会出现乱序导致不美观，所以禁用了窗口最大化功能

## 	2.改进方向

可以加上数据库的技术，使数据持久化。可以修改控件的属性，使控件更加美观。

老师提出的改动要求是只能导入一张图片，做法是将`getOpenFileNames` 改为`getOpenFileName`

```python
self.imgName,imgType = QtWidgets.QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
self.imgName2,imgType = QtWidgets.QFileDialog.getOpenFileName(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
```

在listview的模式中更换为imgName2即可实现

