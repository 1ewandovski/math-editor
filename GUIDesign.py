# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:11:11 2020

@author: yaoyizhou
"""

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon,QPalette,QPixmap,QFont, QColor
import matplotlib.pyplot as plt
import sys
import os

from new_widget import Textbench

class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.init_UI()
    def init_UI(self):
        self.Vbox = QtWidgets.QVBoxLayout() #QVBoxLayout 类将各部件垂直排列        
        self.Hboxs = {
            'button1_hbox' : QtWidgets.QHBoxLayout(),
            'button2_hbox' : QtWidgets.QHBoxLayout(),
            'input_hbox' : QtWidgets.QHBoxLayout(),
            'potential_hbox' : QtWidgets.QHBoxLayout(),
        } #QHBoxLayout 类将各部件水平排列
        self.resulttable=QtWidgets.QWidget()
        self.instructtable=QtWidgets.QTextBrowser(self)
        self.id_item_table=QtWidgets.QWidget()
        self.table_img = QtWidgets.QLabel()
        
        self.iface_label = QtWidgets.QLabel('Choose formula kind:')
        self.iface_label.setFont(QFont("Roman times",12,QFont.Bold))
        self.formula_comb = QtWidgets.QComboBox(self) #QComboBox称做下拉列表框
        self.formula_comb.setFont(QFont("Ubuntu Mono", 10))
        
        self.lineEidt = QtWidgets.QLineEdit(self) #QLineEdit是一个小部件，允许输入和编辑单行纯文本
        self.lineEidt.setClearButtonEnabled(True)
        self.input_but = QtWidgets.QPushButton("Enter")
        self.input_but.setShortcut(QtCore.Qt.Key_Return)
        #self.but1_1 = QtWidgets.QPushButton("下标")
        #self.but1_2 = QtWidgets.QPushButton("上标")
        #self.but1_3 = QtWidgets.QPushButton("分数")
        #self.but2_1 = QtWidgets.QPushButton("分式")
        #self.but2_2 = QtWidgets.QPushButton("开平方")
        #self.but2_3 = QtWidgets.QPushButton("开n次方")
        
        self.Hboxs['input_hbox'].addWidget(self.formula_comb)        
        self.Hboxs['input_hbox'].addStretch(1) #平分布局，它所带的参数就是所占的比例
        #self.Hboxs['input_hbox'].addWidget(self.instructtable)
        self.Hboxs['input_hbox'].addWidget(self.lineEidt)
        self.Hboxs['input_hbox'].addWidget(self.input_but)
        
        #self.Hboxs['button1_hbox'].addWidget(self.but1_1)
        #self.Hboxs['button1_hbox'].addWidget(self.but1_2)
        #self.Hboxs['button1_hbox'].addWidget(self.but1_3)
        
        #self.Hboxs['button2_hbox'].addWidget(self.but2_1)
        #self.Hboxs['button2_hbox'].addWidget(self.but2_2)
        #self.Hboxs['button2_hbox'].addWidget(self.but2_3)
        
        #self.tmp1Widget=QtWidgets.QWidget()
        #self.tmp1Widget.setLayout(self.Hboxs['button1_hbox'])
        
        #self.tmp2Widget=QtWidgets.QWidget()
        #self.tmp2Widget.setLayout(self.Hboxs['button2_hbox'])
        
        self.tmp3Widget=QtWidgets.QWidget()
        self.tmp3Widget.setLayout(self.Hboxs['input_hbox'])
        
        #self.Vbox.addWidget(self.tmp1Widget)
        #self.Vbox.addWidget(self.tmp2Widget)
        self.Vbox.addWidget(self.tmp3Widget)
        self.Vbox.addWidget(self.instructtable)
        self.Vbox.addWidget(self.id_item_table)
        self.Vbox.addWidget(self.resulttable)
        
        self.setLayout(self.Vbox)
    def get_inputword(self):
        return self.lineEidt.text()
    def Set_formula_Comb(self, formula_texts, text): #猜测用于构建端口列表
        self.formula_comb.addItems(formula_texts)        
        self.formula_comb.setCurrentText(text)

class My_Main_window(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(My_Main_window,self).__init__(parent)
        # 重新调整大小
        self.resize(800, 659)
        self.dic=Textbench()
        self.instruction=""
        self.ins_signal=0
        self.mode_id=0
        self.state_id=0
        self.fraction_symbol=0
        self.text="Hello World!"
        self.text_stack=[]        
        self.initUI()
    def initUI(self):
        self.setWindowIcon(QIcon('img/timg.jpg'))
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('ready')
        #tool action
        self.uper_Act = QtWidgets.QAction(QIcon('img/uper.png'), '&上标', self)       
        self.uper_Act.setShortcut('Ctrl+u')
        self.uper_Act.setStatusTip('write superscript')
        self.uper_Act.triggered.connect(self.uper_input)
        
        self.lower_Act = QtWidgets.QAction(QIcon('img/lower.png'), '&下标', self)       
        self.lower_Act.setShortcut('Ctrl+l')
        self.lower_Act.setStatusTip('write subscript')
        self.lower_Act.triggered.connect(self.lower_input)
        
        self.frac_Act = QtWidgets.QAction(QIcon('img/frac.png'), '&分式', self)       
        self.frac_Act.setShortcut('Ctrl+f')
        self.frac_Act.setStatusTip('write fraction')
        self.frac_Act.triggered.connect(self.frac_input)
        
        self.sqrt_Act = QtWidgets.QAction(QIcon('img/sqrt.png'), '&开根', self)       
        self.sqrt_Act.setShortcut('Ctrl+r')
        self.sqrt_Act.setStatusTip('write radical expression')
        self.sqrt_Act.triggered.connect(self.sqrt_input)
        
        self.Nsqrt_Act = QtWidgets.QAction(QIcon('img/Nsqrt.png'), '&开n次方根', self)       
        self.Nsqrt_Act.setShortcut('Ctrl+n')
        self.Nsqrt_Act.setStatusTip('write N radical expression')
        self.Nsqrt_Act.triggered.connect(self.sqrt_input)
        
        self.exit_Act = QtWidgets.QAction(QIcon('img/Exit.png'), '&quit', self)  #退出动作     
        self.exit_Act.setShortcut('Ctrl+q')
        self.exit_Act.setStatusTip('Exit application')
        self.exit_Act.triggered.connect(self.close)
        
        self.openFile = QtWidgets.QAction(QIcon('img/OpenFile.png'), '&open', self) #打开文件动作
        self.openFile.setShortcut('Ctrl+o')
        self.openFile.setStatusTip('Open Saved File')
        self.openFile.triggered.connect(self.OpenFile)

        self.saveFile = QtWidgets.QAction(QIcon('img/SaveFile.png'), '&save', self )
        self.saveFile.setShortcut('Ctrl+s')
        self.saveFile.setStatusTip('Save File')
        self.saveFile.triggered.connect(self.SaveFile)
        # menu action
        self.menu_action1 = QtWidgets.QAction(QIcon('img/StartAct.png'),"display",self)
        self.menu_action1.setShortcut('Ctrl+d')
        self.menu_action1.setStatusTip('display math formula')
        self.menu_action1.triggered.connect(self.plot_)
        
        self.menu_action2 = QtWidgets.QAction(QIcon('img/ShowHistory.png'),"back",self)
        self.menu_action2.setShortcut('Ctrl+t')
        self.menu_action2.setStatusTip('trace back')
        self.menu_action2.triggered.connect(self.pop_stack)
        
        self.menu_action3 = QtWidgets.QAction(QIcon('img/ClearAct.png'),"clear",self)
        self.menu_action3.setShortcut('Ctrl+c')
        self.menu_action3.setStatusTip('clear the input and output')
        self.menu_action3.triggered.connect(self.clear)
        
        #menu
        self.menubar = self.menuBar()
        
        self.menu1 = self.menubar.addMenu("File(&F)")                
        self.menu1.addAction(self.exit_Act)
        self.menu1.addAction(self.openFile)
        self.menu1.addAction(self.saveFile)
        
        self.menu2 = self.menubar.addMenu("Tool(&T)")                
        self.menu2.addAction(self.uper_Act)
        self.menu2.addAction(self.lower_Act)
        self.menu2.addAction(self.frac_Act)
        self.menu2.addAction(self.sqrt_Act)
        self.menu2.addAction(self.Nsqrt_Act)
        
        self.menu3 = self.menubar.addMenu("View(&V)")                
        self.menu3.addAction(self.menu_action1)
        self.menu3.addAction(self.menu_action2)
        self.menu3.addAction(self.menu_action3)
        
        #tools
        self.toolbar = self.addToolBar('Tools')
        
        self.toolbar.addAction(self.uper_Act)
        self.toolbar.addAction(self.lower_Act)
        self.toolbar.addAction(self.frac_Act)
        self.toolbar.addAction(self.sqrt_Act)
        self.toolbar.addAction(self.Nsqrt_Act)
        self.toolbar.addAction(self.menu_action1)
        self.toolbar.addAction(self.menu_action2)
        self.toolbar.addAction(self.menu_action3)
        self.toolbar.addAction(self.exit_Act)
        
        self.central_Widget = CentralWidget()
        self.set_Initial_fomula("normal mode")
        self.initial_table()
        #self.central_Widget.Set_formula_Comb(self.dic.formula_dic,"normal mode")
        self.central_Widget.formula_comb.activated[str].connect(self.Change_formula_from_combo)
        self.central_Widget.input_but.clicked.connect(self.input_confirm)
        #self.central_Widget.but1_1.clicked.connect(self.lower_input)
        #self.central_Widget.but1_2.clicked.connect(self.uper_input)
        #self.central_Widget.but1_3.clicked.connect(self.frac_input)
        #self.central_Widget.but2_1.clicked.connect(self.cfrac_input)
        #self.central_Widget.but2_2.clicked.connect(self.sqrt_input)
        #self.central_Widget.but2_3.clicked.connect(self.Nsqrt_input)
        
        self.initial_plot_()
        
        self.renew_instruction()
        self.setCentralWidget(self.central_Widget)
        
        self.setWindowTitle('Galois\' Math Editor v1.1.0')

    def initial_plot_(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        self.fig = plt.figure()
        self.fig.text(0.1,0.4,'$'+self.text+'$',fontsize=20,color="black")
        #self.fig.show()
        self.cavans = FigureCanvas(self.fig)
        self.tmpLayout=QtWidgets.QHBoxLayout()
        self.tmpLayout.addWidget(self.cavans)        
        self.central_Widget.resulttable.setLayout(self.tmpLayout)
    def plot_(self):
        plt.cla()
        fig=plt.figure()
        fig.text(0.1,0.4,'$'+self.text+'$',fontsize=20,color="black")          
        self.tmpLayout.removeWidget(self.cavans)
        self.cavans=FigureCanvas(fig)
        self.tmpLayout.addWidget(self.cavans)
        
        #fig.show()
        
    def renew_instruction(self):
        self.switch_instruction()
        self.central_Widget.instructtable.setText(self.instruction)
        
    def switch_instruction(self):
        if self.ins_signal==0:
            self.instruction="normal input,you can choose a kind of formula"
        elif self.ins_signal==1:
            self.instruction="please enter an number"
        elif self.ins_signal==2:
            self.instruction="please enter an numberator"
        elif self.ins_signal==3:
            self.instruction="please enter an denominator"
        elif self.ins_signal==4:
            self.instruction="please enter an index of sqrt"
        elif self.ins_signal==5:
            self.instruction="please enter superscript"
        elif self.ins_signal==6:
            self.instruction="please enter subscript"
        elif self.ins_signal==7:
            self.instruction="cannot trace back any more"
        elif self.ins_signal==8:
            self.instruction="nothing to clear"
        else:
            self.instruction="please push finish button"
            
    def set_Initial_fomula(self, text): #设置接口                
        formula_texts = [ self.dic.formula_dic[item] for item in self.dic.formula_dic ]
        self.central_Widget.Set_formula_Comb(formula_texts, text)
        
    def Change_formula_from_combo(self,text):
        if text =="normal mode":
            self.mode_id = 0
        elif text =="calculas mode":
            self.mode_id = 1
        elif text =="set mode":
            self.mode_id = 2
        elif text =="latter mode":
            self.mode_id = 3
        elif text =="relation mode":
            self.mode_id = 4
        elif text =="function mode":
            self.mode_id = 5
        self.switch_table()
        
    def initial_table(self):
        self.central_Widget.table_img.setPixmap(QPixmap('img/normal.png'))          
        table_layout = QtWidgets.QHBoxLayout()
        table_layout.addWidget(self.central_Widget.table_img)
        self.central_Widget.id_item_table.setLayout(table_layout)
    def switch_table(self):
        if self.mode_id == 0:
            self.central_Widget.table_img.setPixmap(QPixmap('img/normal.png'))
        elif self.mode_id == 1:
            self.central_Widget.table_img.setPixmap(QPixmap('img/calculas_table.png'))
        elif self.mode_id == 2:
            self.central_Widget.table_img.setPixmap(QPixmap('img/set_table.png'))
        elif self.mode_id == 3:
            self.central_Widget.table_img.setPixmap(QPixmap('img/latter_table.png'))
        elif self.mode_id == 4:
            self.central_Widget.table_img.setPixmap(QPixmap('img/relation_table.png'))
        elif self.mode_id == 5:
            self.central_Widget.table_img.setPixmap(QPixmap('img/func_table.png'))
    def index_To_word(self,index):
        if self.mode_id == 0:
            return ' '+index+' '
        elif self.mode_id == 1:
            return self.dic.caculas_dic[index]
        elif self.mode_id == 2:
            return self.dic.set_dic[index]
        elif self.mode_id == 3:
            return self.dic.latter_dic[index]
        elif self.mode_id == 4:
            return self.dic.relation_dic[index]
        elif self.mode_id == 5:
            return self.dic.func_dic[index]
    
    def lower_input(self):
        self.state_id = 1
        self.ins_signal = 6
        self.renew_instruction()
    def uper_input(self):
        self.state_id = 2
        self.ins_signal = 5
        self.renew_instruction()
    def frac_input(self):
        self.state_id = 3
        self.fraction_symbol = 1
        self.ins_signal = 2
        self.renew_instruction()
    def cfrac_input(self):
        self.state_id = 4
        self.fraction_symbol = 1
        self.ins_signal = 2
        self.renew_instruction()
    def sqrt_input(self):
        self.state_id = 5
        self.renew_instruction()
    def Nsqrt_input(self):
        self.state_id = 6
        self.fraction_symbol = 1
        self.ins_signal = 4
        self.renew_instruction()
    
    def input_confirm(self):
        index=self.central_Widget.get_inputword()
        if self.text == "Hello World!":
            self.text = ""
        if self.state_id == 0:
            self.text_stack.append(self.text)
            self.text=self.text+self.index_To_word(index)
            self.plot_()            
        elif self.state_id ==1:    #下标内容需要一次性输入完毕
            self.text_stack.append(self.text)
            self.text=self.text+'_{'+self.index_To_word(index)+'}'
            self.state_id = 0
            self.ins_signal = 0
            self.plot_()            
        elif self.state_id ==2:    #上标需要一次性输入完毕
            self.text_stack.append(self.text)
            self.text=self.text+'^{'+self.index_To_word(index)+'}'
            self.state_id = 0
            self.ins_signal = 0
            self.plot_()            
        elif self.state_id ==3:    #分数的上部下部需要一次性输入完毕
            if self.fraction_symbol == 1:
                self.text_stack.append(self.text)
                self.text=self.text+r'\frac{'+self.index_To_word(index)+'}'
                self.fraction_symbol = 0
                self.ins_signal = 3
            else:
                self.text=self.text+'{'+self.index_To_word(index)+'}'
                self.state_id = 0
                self.ins_signal = 0
                self.plot_()                
        elif self.state_id == 4:
            if self.fraction_symbol == 1:
                self.text_stack.append(self.text)
                self.text=self.text+r'\frac{'+self.index_To_word(index)+'}'
                self.fraction_symbol = 0
                self.ins_signal = 3
            else:
                self.text=self.text+'{'+self.index_To_word(index)+'}'
                self.state_id = 0
                self.ins_signal = 0
                self.plot_()                
        elif self.state_id == 5:
            self.text_stack.append(self.text)
            self.text=self.text+'\sqrt{'+self.index_To_word(index)+'}'
            self.state_id = 0
            self.plot_()            
        elif self.state_id == 6:
            if self.fraction_symbol == 1:
                self.text_stack.append(self.text)
                self.text=self.text+'\sqrt['+self.index_To_word(index)+']'
                self.fraction_symbol =0
                self.ins_signal = 0
            else:
                self.text=self.text+'{'+self.index_To_word(index)+'}'
                self.state_id = 0
                self.plot_()                        
        self.renew_instruction()

    def pop_stack(self):        
        if len(self.text_stack) > 0:
            self.text = self.text_stack.pop()                            
        else:
            self.text = "Hello World!"
            self.ins_signal=7
            self.renew_instruction()
        if self.text == "":
            self.text = "Hello World!"        
        self.plot_()
    def clear(self):
        if len(self.text_stack)> 0:
            self.text_stack.clear()
        else:
            self.ins_signal=8
            self.renew_instruction()
        self.text = "Hello World!"
        self.plot_()
    def OpenFile(self):
        fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "Choose file", "./",  "*.txt;;All Files (*);;") 
        f=open(fileName)
        self.text_stack.append(self.text)
        self.text = f.read()
        self.plot_()
        f.close()
    def SaveFile(self):
        save_path, ok2 = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "./", "*.txt;;All Files (*)")
        f=open(save_path,'w')
        f.write(self.text)
        f.close()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()     
    main_window.show()
    app.exec()