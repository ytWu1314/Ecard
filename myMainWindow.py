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
      '''
      self.imglist=[]
      with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto.txt',mode='r+',encoding='utf-8') as x:
         line=x.readline().strip()
         linestr=line.split()
         print(linestr)
         print("**************")   
      for i in linestr:
         self.imglist.append(i)   
      print(self.imglist) 
      slm = QStringListModel()
      slm.setStringList(self.imglist)
      self.ui.listView.setModel(slm) 
      '''
      '''
      with open('C:/Users/PC_SKY_WYT/Desktop/PyQt/savephoto2.json','r') as x:
         self.imgName=json.load(x)
      self.slm = QStringListModel()
      self.slm.setStringList(self.imgName)
      self.ui.listView.setModel(self.slm) 


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

      self.str1=self.ui.textEdit.toPlainText()
      with open("C:/Users/PC_SKY_WYT/Desktop/PyQt/textEdit.txt",'w') as p:
         p.write(self.str1)
      '''   
   
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
      with open("C:/Users/PC_SKY_WYT/Desktop/PyQt/lineEdit.txt",encoding='utf-8',mode='r+') as z:
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
