#encoding:utf-8
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

FirstRoleExtend12=[' 魏斯', '   李悝', '  公孙衍', ' 赵奢', '    孙膑', '   乐毅', '    钟离春', '  墨翟', '    屈原', '    田文', '     王诩', '欧冶子',\
                   '嬴渠梁', '   商鞅', '  樗里疾', ' 白起', '    蒙骜', '   王翦', '    芈八子', '  魏冉', '    李冰', '    嫪毐', '     甘茂', ' 卢敖',\
                   ' 刘邦', '   萧何', '   张良', ' 卫青', '    韩信', '   周勃', '     吕雉', '  张骞', '贾谊/司马相如', '   东方朔', '    董仲舒', ' 蔡伦',\
                   '司马炎', '   王导', '   张华', ' 陈骞', '    刘琨', '   陶侃', '    贾南风', '  王敦', '  左思/潘安', '   王羲之', '    王徽之', ' 裴秀', \
                   ' 刘裕', '  刘穆之', '  徐羡之', '王镇恶', '沈田子/朱龄石', '  檀道济', '    刘楚玉', ' 王僧虔', '   祖冲之', '   陆修静', '   范晔/谢朓', '何承天', \
                   ' 苻坚', '   张宾', '   王猛', '慕容恪', '  慕容绍宗', '   石勒', '     冯氏', '鸠摩罗什', '   慕容垂', '    元英', '    郦道元', '慕容评',\
                   ' 杨坚', '   高颎', '  李德林', '贺若弼', '   韩擒虎', '  史万岁', '   独孤伽罗', '  杨勇', '    李密', '    牛弘', '    展子虔', '宇文恺',\
                   '李世民', '  房玄龄', '  杜如晦', ' 李靖', '    李绩', '   秦琼', '李令月/上官婉儿', ' 徐敬业', '   高仙芝', '  李白/杜甫', '     张旭', ' 玄奘',\
                   '赵匡胤', '范仲淹/韩琦', '   赵普', ' 狄青', '    杨业', '   曹彬', '    梁红玉', '  蔡京', ' 欧阳修/苏轼', '    米芾', '     张载', ' 毕昇',\
                   '铁木真', ' 耶律楚材', '  木华黎', ' 哲别', '   者勒蔑', '  速不台', '   脱列那哥', '  拖雷', '   史天泽', '   关汉卿', '    赵孟頫', '丘处机', \
                   '朱元璋', '  李善长', '   解缙', ' 徐达', '    蓝玉', '  常遇春', '     刘瑾', ' 徐有贞', '    郑和', '    唐寅', '    徐光启', '王守仁',\
                   '皇太极', '  多尔衮', '  范文程', ' 施琅', '    多铎', '  年羹尧', '     孝庄', '  胤祥', '   刘铭传', '洪承畴/吴三桂', '纳兰容若/蒲松龄', '林则徐',\
                   ' ——', '   ——','   ——',' ——','    ——','   ——','     ——','  ——','    ——','    ——','     ——',' ——',\
                   ' 陆羽', '  张仲景', '   魏征', ' 荆轲', '    张汤', '马可·波罗', '    高渐离', '  刘徽', '   王昭君', '    冒顿', '    沈万三', ' 张巡', ' 冼英', '   李泌', '   项羽']

JunListExtend12=['魏斯', '嬴渠梁', '刘邦', '司马炎', '刘裕', '苻坚', '杨坚', '李世民', '赵匡胤', '铁木真', '朱元璋', '皇太极']
XiangListExtend12=['李悝', '公孙衍', '商鞅', '樗里疾', '萧何', '张良', '王导', '张华', '刘穆之', '徐羡之', '张宾', '王猛', '高颎', '李德林', '房玄龄', '杜如晦', '范仲淹/韩琦', '赵普', '耶律楚材', '李善长', '解缙', '多尔衮', '范文程']
JiangListExtend12=['赵奢', '孙膑', '乐毅', '白起', '蒙骜', '王翦', '卫青', '韩信', '周勃', '陈骞', '刘琨', '陶侃', '王镇恶', '沈田子/朱龄石', '檀道济', '慕容恪', '慕容绍宗', '石勒', '贺若弼', '韩擒虎', '史万岁', '李靖', '李绩', '秦琼', '狄青', '杨业', '曹彬','木华黎','哲别', '者勒蔑', '速不台', '徐达', '蓝玉', '常遇春', '施琅', '多铎', '年羹尧']
ChenListExtend12=['钟离春', '墨翟', '屈原', '田文', '王诩', '欧冶子', '芈八子', '魏冉', '李冰', '嫪毐', '甘茂', '卢敖', '吕雉', '张骞', '贾谊/司马相如', '东方朔', '董仲舒', '蔡伦', '贾南风', '王敦', '左思/潘安', '王羲之', '王徽之', '裴秀', '刘楚玉', '王僧虔', '祖冲之', '陆修静', '范晔/谢朓', '何承天', '冯氏', '鸠摩罗什', '慕容垂', '元英', '郦道元', '慕容评', '独孤伽罗', '杨勇', '李密', '牛弘', '展子虔', '宇文恺', '李令月/上官婉儿', '徐敬业', '高仙芝', '李白/杜甫', '张旭', '玄奘', '梁红玉', '蔡京', '欧阳修/苏轼', '米芾', '张载', '毕昇', '脱列那哥', '拖雷', '史天泽', '关汉卿', '赵孟頫', '丘处机', '刘瑾', '徐有贞', '郑和', '唐寅', '徐光启', '王守仁', '孝庄', '胤祥', '刘铭传', '洪承畴/吴三桂', '纳兰容若/蒲松龄', '林则徐']
YeList=['陆羽', '张仲景', '魏征', '荆轲', '张汤', '马可·波罗', '高渐离', '刘徽', '王昭君', '冒顿', '沈万三', '张巡', '冼英', '李泌', '项羽']



class MainForm(QWidget):
    global globalPickList
       
    
    _signal=pyqtSignal(list)
    
    def __init__(self):
        super().__init__()        
         
        self.initUI()
        
        self.child=ChildrenForm()
         

    def initUI(self):
        self.banrolelist=[]
        self.banrolestr=[]
        self.banrolelist2=[]
        self.pickrolelist=[]
        self.pickednow=[]

        self.BanListTitle = QLabel('        已ban角色：')
        self.BanListInput=QLineEdit()

        self.BanListTips = QLabel('    Tip:1.点击下方角色名后点击左侧按钮ban将\n        2.完成全部ban将后点击左侧按钮出将面\n        3.点击下方按钮进入BP')
        self.BanListOutput=QLineEdit()
        self.BanListShow = QTextEdit()       
        
        
        self.ButtonConfirm = QPushButton("点击将Ban掉下表中选中角色")
        self.BanTable=QTableWidget(15,12)
        self.BanTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.BanTable.setVerticalHeaderLabels(['战国','秦朝','汉朝','晋朝','南朝','北朝','隋朝','唐朝','宋朝','元朝','明朝','清朝','——','在野','在野'])
        self.BanTable.setHorizontalHeaderLabels(['君','相','相（元将）','将','将','将','臣','臣','臣','臣','臣','臣'])
        self.BanTable.setAlternatingRowColors(True)
        #self.BanTable.horizontalHeader().setVisible(False)
        self.BanTable.setWindowTitle("Role List")
        #self.BanTable.resizeColumnToContents(0)
        #self.BanTable.resizeRowToContents(0)
        for i in range(0,12):
            ItemH = self.BanTable.horizontalHeaderItem(i)
            ItemH.setFont(QFont('song',12,QFont.Bold))

      
        Item0 = self.BanTable.verticalHeaderItem(0)
        Item0.setFont(QFont('song',15,QFont.Bold))
        Item0.setForeground(QBrush(QColor(191,191,191)))
        Item1 = self.BanTable.verticalHeaderItem(1)
        Item1.setFont(QFont('song',15,QFont.Bold))
        Item1.setForeground(QBrush(QColor(89,89,89)))
        Item2 = self.BanTable.verticalHeaderItem(2)
        Item2.setFont(QFont('song',15,QFont.Bold))
        Item2.setForeground(QBrush(QColor(255,0,0)))
        Item3 = self.BanTable.verticalHeaderItem(3)
        Item3.setFont(QFont('song',15,QFont.Bold))
        Item3.setForeground(QBrush(QColor(0,176,80)))
        Item4 = self.BanTable.verticalHeaderItem(4)
        Item4.setFont(QFont('song',15,QFont.Bold))
        Item4.setForeground(QBrush(QColor(168,208,141)))
        Item5 = self.BanTable.verticalHeaderItem(5)
        Item5.setFont(QFont('song',15,QFont.Bold))
        Item5.setForeground(QBrush(QColor(191,143,0)))
        Item6 = self.BanTable.verticalHeaderItem(6)
        Item6.setFont(QFont('song',15,QFont.Bold))
        Item6.setForeground(QBrush(QColor(128,0,0)))
        Item7 = self.BanTable.verticalHeaderItem(7)
        Item7.setFont(QFont('song',15,QFont.Bold))
        Item7.setForeground(QBrush(QColor(255,102,255)))
        Item8 = self.BanTable.verticalHeaderItem(8)
        Item8.setFont(QFont('song',15,QFont.Bold))
        Item8.setForeground(QBrush(QColor(255,192,0)))
        Item9 = self.BanTable.verticalHeaderItem(9)
        Item9.setFont(QFont('song',15,QFont.Bold))
        Item9.setForeground(QBrush(QColor(51,204,204)))
        Item10 = self.BanTable.verticalHeaderItem(10)
        Item10.setFont(QFont('song',15,QFont.Bold))
        Item10.setForeground(QBrush(QColor(0,0,255)))
        Item11 = self.BanTable.verticalHeaderItem(11)
        Item11.setFont(QFont('song',15,QFont.Bold))
        Item11.setForeground(QBrush(QColor(112,48,160)))
        Item14 = self.BanTable.verticalHeaderItem(14)
        Item14.setFont(QFont('song',15,QFont.Bold))
        Item14.setForeground(QBrush(QColor(0,32,96)))
        Item13 = self.BanTable.verticalHeaderItem(13)
        Item13.setFont(QFont('song', 15, QFont.Bold))
        Item13.setForeground(QBrush(QColor(0, 32, 96)))


        self.BanTable.setSelectionMode(QAbstractItemView.MultiSelection)

        row=0
        line=0
        strtmp=""
        for i in FirstRoleExtend12:

            if row==12:
                row=0
                line=line+1
                strtmp=strtmp+"\n"
            self.BanTable.setItem(line,row,QTableWidgetItem(str(i)))
            self.BanTable.setFont(QFont('kai',11,QFont.Bold))
            strtmp=strtmp+" "+str(i)
            row=row+1
            self.BanTable.resizeColumnsToContents()

            #self.BanTable.resizeRowsToContents()

       
        #BanTable.itemDoubleClicked.connect(self.outSelect)
        self.BanTable.itemClicked.connect(self.outSelect)
        #BanTable.itemDoubleClicked.connect(self.banShow)
     
        vbox2 = QVBoxLayout()

        
        vbox2.addWidget(self.BanListTitle)
        vbox2.addWidget(self.BanListInput)

        #小横箱
        hbox3=QHBoxLayout()
        hbox3.addWidget(self.BanListTips)
        hbox3.addWidget(self.BanListOutput)

        vbox2.addLayout(hbox3)
       
        vbox2.addWidget(self.BanListShow)
        vbox2.addWidget(self.ButtonConfirm)
        vbox2.addWidget(self.BanTable)

            

        #9朝12朝选择
        
        self.Button12 = QPushButton("点击出将面")
        
        self.ButtonBP = QPushButton("清除Ban将名单")
        self.ButtonBegin =QPushButton("开始BP")

        hboxbutton = QHBoxLayout()        
        hboxbutton.addWidget(self.Button12)
        hboxbutton.addWidget(self.ButtonConfirm)
        hboxbutton.addWidget(self.ButtonBP)
        
        self.Button12.clicked.connect(self.button12Clicked)
        self.ButtonConfirm.clicked.connect(self.buttonConfirm)
        self.ButtonBP.clicked.connect(self.buttonBPClicked)
        self.ButtonBegin.clicked.connect(self.childShow)
        
        
        #大垂直箱
        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hboxbutton)
        vbox.addWidget(self.ButtonBP)


        ggrid=QGridLayout()
        ggrid.setColumnStretch(1,1)
        ggrid.setColumnStretch(1,1)
        ggrid.setColumnStretch(2,1)
        ggrid.setColumnStretch(3,1)
        
        
        ggrid.addWidget(self.BanListTitle,1,0,1,1)
        ggrid.addWidget(self.BanListInput,1,1,1,1)
        ggrid.addWidget(self.BanListTips,2,1,2,1)
        #ggrid.addWidget(self.BanListOutput,2,1,1,2)
        ggrid.addWidget(self.BanListShow,1,2,2,2)
        ggrid.addWidget(self.ButtonBegin,4,1,1,1)
        #ggrid.addWidget(self.Button9,5,0,1,1)
        ggrid.addWidget(self.Button12,3,0,1,1)
        ggrid.addWidget(self.ButtonBP,4,0,1,1)
        ggrid.addWidget(self.ButtonConfirm,2,0,1,1)
        
        ggrid.addWidget(self.BanTable,5,0,4,4)
        self.setLayout(ggrid)
        self.setGeometry(70, 60, 1180, 640)
        self.show()
        

    def outSelect( self, item2=None):
           banrolelisttmp=self.banrolelist[:]
           if item2!=None:
                  rolename=item2.text()
                  flag1=0
                  for i in self.banrolelist:
                         if i==rolename:
                                flag1=1
                                banrolelisttmp.remove(i)
                                break
                  if flag1==0:
                        banrolelisttmp.append(item2.text())
                  self.banrolelist=banrolelisttmp[:]
        

    def buttonConfirm(self):
        strtmp=""
        for i in self.banrolelist:
            strtmp=strtmp+str(i)+" "
        self.BanListInput.setText(strtmp)
        self.BanListOutput.setText(strtmp)
        

        
    def button12Clicked(self):
        #调用12朝bp
        self.BanPick1v1Extend12()



    def BanPick1v1Extend12(self):

       banrole=self.banrolelist[:]
       temp=self.BanListInput.text()

       try:            
            banrole=[str(i) for i in temp.split(' ')]
            isint=0
       except:
            print("error")
            

       isint=0;
       self.banrolelist2=[]
       
       for i in banrole:
            try:
                i=int(i)
                isint=1;
            except:
                isint=0;
            if isint==0:
                for j in FirstRoleExtend12:                
                    if i==j:
                        self.banrolelist2.append(i);
                        break
            else:
                if i>=0 and i<len(FirstRoleExtend12):
                    for j in FirstRoleExtend12:                
                        if FirstRoleExtend12[i]==j:                            
                            self.banrolelist2.append(j);
                            break
                else:
                    continue                


       strtmp=""
       for i in self.banrolelist2:
            strtmp=strtmp+str(i)+" "
       self.BanListInput.setText(strtmp)
       self.BanListOutput.setText(strtmp)
        
       for i in self.banrolelist2:
            for j in JunListExtend12:
                if i==j:
                    JunListExtend12.remove(i);
                    break
            for j in XiangListExtend12:
                if i==j:
                    XiangListExtend12.remove(i);
                    break
            for j in JiangListExtend12:
                if i==j:
                    JiangListExtend12.remove(i);
                    break
            for j in ChenListExtend12:
                if i==j:
                    ChenListExtend12.remove(i);
                    break
            for j in YeList:
                if i==j:
                    YeList.remove(i);
                    break


       random.shuffle(JunListExtend12)
       random.shuffle(XiangListExtend12)
       random.shuffle(JiangListExtend12)
       random.shuffle(ChenListExtend12)
       random.shuffle(YeList)

       picklist=[]


       for i in range(0,3):
            picklist.append(JunListExtend12[i]);
       for i in range(0,6):
            picklist.append(XiangListExtend12[i]);
       for i in range(0,6):
            picklist.append(JiangListExtend12[i]);
       for i in range(0,12):
            picklist.append(ChenListExtend12[i]);
       for i in range(0,3):
            picklist.append(YeList[i]);


       flag1=1
       while (flag1):
            random.shuffle(picklist)

            xiang=0
            for i in range(0,15):
                for j in XiangListExtend12:
                    if picklist[i]==j:
                        xiang=xiang+1
            if xiang<2:
                flag1=1;
            else:
                flag1=0;
            
       j=1
       strtmp=""
       for i in picklist:
            strtmp=strtmp+str(j)+str(i)+" "        
            j=j+1
            if j==16:
                strtmp=strtmp+"\n"
       self.BanListShow.setText(strtmp)
       self.pickrolelist=picklist[:]
      
        
    def buttonBPClicked(self):
        self.banrolelist=[]
        self.BanListInput.setText("")
        self.BanListOutput.setText("")
        self.BanTable.clearSelection()

    def childShow(self):

        #self._signal.connect(self.child.childDraw)
        self._signal.emit(self.pickrolelist)
        globalPickList=self.pickrolelist[:]
        
        #self.child.childShow()
        
        
        
         

class ChildrenForm(QWidget):    
    
    def __init__(self):        
        super(ChildrenForm,self).__init__()
        self.initUI()

    def initUI(self):
        self.pickrolelist=[]
        self.picklist1=[]
        self.picklist2=[]
        self.pickedlist=[]
        self.pickednow=[]
        self.rollbacknow=[]
       
        self.BTable=QTableWidget(15,2)
        self.PTable=QTableWidget(15,2)
        self.PName1=QLabel("先手玩家")
        self.PickName1=QLineEdit("先手")
        self.PName2=QLabel("后手玩家")
        self.PickName2=QLineEdit("后手")
        self.PickNameButton=QPushButton("修改玩家id")

        self.BTable.setSelectionMode(QAbstractItemView.MultiSelection)
        self.PTable.setSelectionMode(QAbstractItemView.MultiSelection)

        self.PickRoleTitle=QLabel("正被选取的角色：")
        self.PickRole=QLineEdit()        

        self.Pick1Button=QPushButton("先手选择")
        self.Pick2Button=QPushButton("后手选择")

        self.PickSort=QPushButton("整理选择")
        self.Rollback=QPushButton("取消选择")
        
        self.BTable.itemClicked.connect(self.tablePick)
        self.PTable.itemClicked.connect(self.tableRollback)
        
        self.PickShow=QTextEdit()
        self.PickShow.setText("")

        self.RemainShow=QTextEdit()
        self.RemainShow.setText("")

        
        self.PickShow2=QTextEdit()
        self.PickShow2.setText("")

        self.PickNameButton.clicked.connect(self.nameModified)
        self.Pick1Button.clicked.connect(self.pick1)
        self.Pick2Button.clicked.connect(self.pick2)
        self.PickSort.clicked.connect(self.pickSort)
        self.Rollback.clicked.connect(self.rollbackPicked)
        
        ggrid=QGridLayout()
        ggrid.addWidget(self.BTable,1,0,15,2)
        ggrid.addWidget(self.PName1,1,3,1,1)
        ggrid.addWidget(self.PName2,1,4,1,1)
        ggrid.addWidget(self.PickName1,2,3,1,1)
        ggrid.addWidget(self.PickName2,2,4,1,1)
        ggrid.addWidget(self.PickNameButton,3,3,1,1)
        ggrid.addWidget(self.PickRoleTitle,4,3,1,1)
        ggrid.addWidget(self.PickRole,4,4,1,1)
        ggrid.addWidget(self.Pick1Button,5,3,1,1)
        ggrid.addWidget(self.Pick2Button,5,4,1,1)
        ggrid.addWidget(self.PickSort,6,3,1,1)
        ggrid.addWidget(self.Rollback,6,4,1,1)
        ggrid.addWidget(self.PickShow,7,3,2,2)
        ggrid.addWidget(self.RemainShow,8,3,2,2)
        ggrid.addWidget(self.PickShow2,9,3,2,2)
        ggrid.addWidget(self.PTable,1,5,15,1)
        
        self.setLayout(ggrid)
        self.setGeometry(70, 70, 900, 600)


    def pickSort(self):
        firstpicklist=[]
        secondpicklist=[]
        junTemp=[]
        xiangTemp=[]
        jiangTemp=[]
        chenTemp=[]
        yeTemp=[]

        if len(self.picklist1)<15 and len(self.picklist2)<15:
            return                  
        
        for i in range(0,15):
            roleitem=self.PTable.takeItem(i,0)
            
            if roleitem!=None:
                rolename=roleitem.text()
                flagJun=0
                try:
                    JunListExtend12.index(rolename)
                    flagJun=1
                    junTemp.append(rolename)                    
                    continue
                except:
                    flagJun=0

                flagXiang=0
                try:
                    XiangListExtend12.index(rolename)
                    flagXiang=1
                    xiangTemp.append(rolename)                    
                    continue
                except:
                    flagXiang=0
                    
                flagJiang=0
                try:
                    JiangListExtend12.index(rolename)
                    flagJiang=1
                    jiangTemp.append(rolename)                    
                    continue
                except:
                    flagJiang=0

                flagChen=0
                try:
                    ChenListExtend12.index(rolename)
                    flagChen=1
                    chenTemp.append(rolename)                    
                    continue
                except:
                    flagChen=0

                flagYe=0
                try:
                    YeList.index(rolename)
                    flagYe=1
                    yeTemp.append(rolename)                    
                    continue
                except:
                    flagYe=0
            
        for i in junTemp:
            firstpicklist.append(i)
        junTemp=[]
        
        for i in xiangTemp:
            firstpicklist.append(i)
        xiangTemp=[]

        for i in jiangTemp:
            firstpicklist.append(i)
        jiangTemp=[]

        for i in chenTemp:
            firstpicklist.append(i)
        chenTemp=[]

        for i in yeTemp:
            firstpicklist.append(i)
        yeTemp=[]
                
        for i in range(0,15):
            roleitem=self.PTable.takeItem(i,1)
            if roleitem!=None:
                rolename=roleitem.text()
                
                flagJun=0
                try:
                    JunListExtend12.index(rolename)
                    flagJun=1
                    junTemp.append(rolename)                    
                    continue
                except:
                    flagJun=0

                flagXiang=0
                try:
                    XiangListExtend12.index(rolename)
                    flagXiang=1
                    xiangTemp.append(rolename)                    
                    continue
                except:
                    flagXiang=0
                    
                flagJiang=0
                try:
                    JiangListExtend12.index(rolename)
                    flagJiang=1
                    jiangTemp.append(rolename)                    
                    continue
                except:
                    flagJiang=0

                flagChen=0
                try:
                    ChenListExtend12.index(rolename)
                    flagChen=1
                    chenTemp.append(rolename)                    
                    continue
                except:
                    flagChen=0

                flagYe=0
                try:
                    YeList.index(rolename)
                    flagYe=1
                    yeTemp.append(rolename)                    
                    continue
                except:
                    flagYe=0
            
        for i in junTemp:
            secondpicklist.append(i)
        junTemp=[]
        
        for i in xiangTemp:
            secondpicklist.append(i)
        xiangTemp=[]

        for i in jiangTemp:
            secondpicklist.append(i)
        jiangTemp=[]

        for i in chenTemp:
            secondpicklist.append(i)
        chenTemp=[]

        for i in yeTemp:
            secondpicklist.append(i)
        yeTemp=[]

        
        str1=""
        str2=""
        for i in range(0,15):
            self.PTable.setItem(i,0,QTableWidgetItem(str(firstpicklist[i])))
            str1=str1+str(firstpicklist[i])+" "
            self.PTable.setItem(i,1,QTableWidgetItem(str(secondpicklist[i])))
            str2=str2+str(secondpicklist[i])+" "

        str1=self.PickName1.text()+"：\n"+str1+"\n\n"+self.PickName2.text()+"：\n"+str2+"\n"
        self.PickShow2.setText(str1)       
        

    def rollbackPicked(self):
        pickedlisttmp=self.pickedlist[:]      

        picktmp="取消选择："
        for i in self.rollbacknow:
            flag=0
            picktmp=picktmp+i+" "
            for j in self.pickedlist:
                if str(i)==str(j):
                    flag=1                    
                    pickedlisttmp.remove(j)                    
                    break
        self.pickedlist=pickedlisttmp[:]

        listtmp=self.picklist1[:]
        for i in self.rollbacknow:
            for j in self.picklist1:
                if str(j)==str(i):
                    listtmp.remove(j)
                    break
        self.picklist1=listtmp[:]

        listtmp=self.picklist2[:]
        for i in self.rollbacknow:
            for j in self.picklist2:
                if str(j)==str(i):
                    listtmp.remove(j)
                    break
        self.picklist2=listtmp[:]

        for i in range(0,15):
            for j in range(0,2):
                tableItem=self.PTable.takeItem(i,j)
        
        for i in self.picklist1:
            pos=self.picklist1.index(i)
            self.PTable.setItem(pos,0,QTableWidgetItem(str(i)))

        for i in self.picklist2:
            pos=self.picklist2.index(i)
            self.PTable.setItem(pos,1,QTableWidgetItem(str(i)))

        
            

        strtmp=""
        pos=0
        for i in self.pickrolelist:
            pos=pos+1
            if pos==16:
                strtmp=strtmp+"\n"
            flag=0
            for j in self.pickedlist:
                if str(j)==str(i):
                    flag=1
                    break       
            if flag==0:
                if pos<16:
                    strtmp=strtmp+str(pos)+str(i)+" "
                else:
                    strtmp=strtmp+str(pos)+" "

        self.rollbacknow=[]
        self.RemainShow.setText(strtmp)
        self.PTable.clearSelection()
        self.PickShow.append(picktmp)

    def tableRollback(self, item2=None):
        pickedlisttmp=self.pickedlist[:]
        
        if item2!=None:
            rolename=item2.text()
            flag1=0
            for i in self.pickedlist:
                 if i==rolename:
                        flag1=1
                        break
            if flag1==1: #已选择的列表有这个id
                pickedlisttmp.remove(i)
                self.rollbacknow.append(i)   

        self.pickedlist=pickedlisttmp[:]
        
        
    def tablePick(self, item2=None):        
        pickedlisttmp=self.pickedlist[:]
        
        if item2!=None:
            #item2.setBackgroundColor(QColor(0,60,10))
            '''
            for ri in range(0,15):
                for ci in range(0,2):
                    tableItem=self.PTable.takeItem(ri,ci)
                    print(tableItem.text())
                    if tableItem.text()==item2.text():
                        tableItem.setTextColor(QColor(200,111,30))
                    self.BTable.setItem(ri,ci,tableItem)
            '''
            rolename=item2.text()            
            templist=[str(j) for j in rolename.split(' ')]
            rolename=templist[1]
            flag1=0
            for i in self.pickedlist:
                 if i==rolename:
                        flag1=1
                        break
            if flag1==0:
                pickedlisttmp.append(rolename)
                self.pickednow.append(rolename)            
            self.pickedlist=pickedlisttmp[:]
            strtmp=""
            for j in self.pickednow:
                strtmp=strtmp+str(j)+" "
            self.PickRole.setText(strtmp)
            self.PickRole.show()

                 
        
        
    def pick1(self):

        
        strtmp=""      
        strtmp=strtmp+self.PickName1.text()+"选择："
        
                
        j=0
        findflag=0
        
        #检查是否超过15个
        totalpicked=0
        for t in range(0,15):
            tableItem=self.PTable.takeItem(t,0)
            if tableItem!=None:
                self.PTable.setItem(t,0,tableItem)
                totalpicked=totalpicked+1
                
        for i in self.pickednow:
            
            findflag=0
            totalpicked=totalpicked+1            
            
            if totalpicked<16:
                self.picklist1.append(i)
                strtmp=strtmp+str(i)+" "
                while((findflag==0) and (j<15)):
                    tableItem=self.PTable.takeItem(j,0)
                    
                    if tableItem==None:
                        self.PTable.setItem(j,0,QTableWidgetItem(str(i)))                             
                        findflag=1
                    else:
                        self.PTable.setItem(j,0,tableItem)
                    j=j+1
            else:
                self.pickedlist.remove(i)
                totalpicked=totalpicked-1
                strtmp=strtmp+"超出个数"
            
        
        self.PickShow.append(strtmp)
        self.pickednow=[]
        self.BTable.clearSelection()
        self.PickShow.show()

        strtmp=""
        pos=0
        for i in self.pickrolelist:
            pos=pos+1
            if pos==16:
                strtmp=strtmp+"\n"
            flag=0
            for j in self.pickedlist:
                if str(j)==str(i):
                    flag=1
                    break       
            if flag==0:
                if pos<16:
                    strtmp=strtmp+str(pos)+str(i)+" "
                else:
                    strtmp=strtmp+str(pos)+" "
        
        self.RemainShow.setText(strtmp)    

    def pick2(self):
        
        strtmp=""        
        strtmp=strtmp+self.PickName2.text()+"选择："
                       
        j=0
        findflag=0
        
        #检查是否超过15个
        totalpicked=0
        for t in range(0,15):
            tableItem=self.PTable.takeItem(t,1)
            if tableItem!=None:
                self.PTable.setItem(t,1,tableItem)
                totalpicked=totalpicked+1
                
        for i in self.pickednow:                       
            findflag=0
            totalpicked=totalpicked+1            
            
            if totalpicked<16:
                self.picklist2.append(i)
                strtmp=strtmp+str(i)+" "  
                while(findflag==0):
                    tableItem=self.PTable.takeItem(j,1)                
                    if tableItem==None:
                        self.PTable.setItem(j,1,QTableWidgetItem(str(i)))                             
                        findflag=1
                    else:
                        self.PTable.setItem(j,1,tableItem)
                    j=j+1
            else:
                self.pickedlist.remove(i)
                totalpicked=totalpicked-1
                strtmp=strtmp+"超出个数"
        
        self.PickShow.append(strtmp)
        self.pickednow=[]
        self.BTable.clearSelection()
        self.PickShow.show()

        strtmp=""
        pos=0
        for i in self.pickrolelist:
            pos=pos+1
            if pos==16:
                strtmp=strtmp+"\n"
            flag=0
            for j in self.pickedlist:
                if str(j)==str(i):
                    flag=1
                    break       
            if flag==0:
                if pos<16:
                    strtmp=strtmp+str(pos)+str(i)+" "
                else:
                    strtmp=strtmp+str(pos)+" "
        
        self.RemainShow.setText(strtmp)   
        
        
    def nameModified(self):
        name1=self.PickName1.text()
        if name1=="":
            name1="先手"
        name2=self.PickName2.text()
        if name2=="":
            name2="后手"
        self.PTable.setHorizontalHeaderLabels([name1,name2])
        
    @pyqtSlot(list) 
    def _signalSlot(self,picklist):
        pass
     
    def childShow(self,picklist=[]):
        self.pickrolelist=picklist[:]
        self.pickedlist=[]

        row=0
        strtmp=""
        pos=0
        for i in self.pickrolelist:
            pos=pos+1            
            if pos<16:
                strtmp=strtmp+str(self.pickrolelist.index(i)+1)+str(i)+" "
            if pos==16:
                strtmp=strtmp+"\n"+str(pos)+" "                
            if pos>16:
                strtmp=strtmp+str(pos)+" "
            
            for j in range(0,2):
                self.BTable.setItem(j,row,QTableWidgetItem(str(self.pickrolelist.index(i)+1)+" "+str(i)))                              
                if j==1:
                    row=row+1
            
        self.RemainShow.setText(strtmp)
        self.show()

    def childDram(self):
        pickrolelist=globalPickList[:]
        print(pickrolelist)
        
    
        
    
        
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = MainForm()    
    ex.show()
    ex._signal.connect(ex.child.childShow)
    sys.exit(app.exec_())
    

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    w = QWidget()
    w.resize(750, 550)
    w.move(300, 300)
    w.setWindowTitle('1v1 BanPick')
    w.show()
    sys.exit(app.exec_())
'''
