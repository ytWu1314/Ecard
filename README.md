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


`myMainWindow.py` 

* 使用 QMediaPlayer 和 QMediaPlaylist 播放 mp3 等音频文件。
* 使用 setPixmap 函数实现 listview中的列表映射到lab上
* 使用python json、txt文件读写 实现保存读取功能。



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

