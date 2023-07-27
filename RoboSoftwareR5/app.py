
from view.ListApi import *
from model.ModulesImportApi import * 
from model.DrugDiseaseInteractionApi import *
from model.ResetAPI import *
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from model.SoundApi import *
from model.Variable import *
from model.AnalysisApi import *
from model.ShowMeSympApi import *
from model.Ecg import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(955, 380)
        MainWindow.setMinimumSize(QtCore.QSize(955, 380))
        MainWindow.setMaximumSize(QtCore.QSize(955, 380))
        MainWindow.setStyleSheet("QLabel{font-family: 'Helvetica';}"
            "background-color: rgb(83, 83, 80);\n"
                                 "background-color: rgb(255, 255, 255);")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(390, 0, 561, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.AnalysisBtm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.AnalysisBtm.setStyleSheet(
                                       "\n"
                                       "background-color: rgb(119, 204, 233);")
        self.AnalysisBtm.pressed.connect(self.F_AnalysisBtm)
        self.AnalysisBtm.setObjectName("AnalysisBtm")
        self.gridLayout.addWidget(self.AnalysisBtm, 7, 0, 1, 1)
        self.pushBtm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushBtm.setStyleSheet(
                                   "\n"
                                   "background-color: rgb(119, 204, 233);")
        self.pushBtm.setObjectName("pushBtm")
        self.pushBtm.pressed.connect(self.F_PushBtm)
        self.gridLayout.addWidget(self.pushBtm, 3, 0, 1, 1)
        self.EffectorComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.EffectorComboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(255, 255, 255);\n"
                                            "border-color: rgb(0, 0, 0);")
        self.EffectorComboBox.setObjectName("EffectorComboBox")
        self.EffectorComboBox.addItems(QlistUniqueValue)
        self.gridLayout.addWidget(self.EffectorComboBox, 2, 0, 1, 1)
        
        self.resetBtm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.resetBtm.setStyleSheet(
                                    "\n"
                                    "background-color: rgb(119, 204, 233);")
        self.resetBtm.setObjectName("resetBtm")
        self.resetBtm.pressed.connect(self.F_ResetBtm)
        self.gridLayout.addWidget(self.resetBtm, 5, 0, 1, 1)

        #### ecg
        self.ECGBTM = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ECGBTM.setStyleSheet(
            "\n"
            "background-color: rgb(119, 204, 233);")
        self.ECGBTM.setObjectName("OPEN ECG")
        self.ECGBTM.pressed.connect(self.F_OPENECG)
        self.gridLayout.addWidget(self.ECGBTM, 7, 0, 1, 1)




        ##



        self.ordersScreenList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.ordersScreenList.setStyleSheet("color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(243, 247, 255);\n"
                                            )
        self.ordersScreenList.setObjectName("ordersScreenList")
        self.gridLayout.addWidget(self.ordersScreenList, 0, 0, 2, 1)
        self.tellmeBtm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tellmeBtm.setStyleSheet(
                                     "\n"
                                     "background-color: rgb(119, 204, 233);")
        self.tellmeBtm.setObjectName("tellmeBtm")
        self.tellmeBtm.pressed.connect(self.F_TellMeBtm)
        self.gridLayout.addWidget(self.tellmeBtm, 4, 0, 1, 1)
        self.ShowmeBtm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ShowmeBtm.setStyleSheet(
                                     "\n"
                                     "background-color: rgb(119, 204, 233);")
        self.ShowmeBtm.pressed.connect(self.F_ShowMeBtm)
        self.ShowmeBtm.setObjectName("ShowmeBtm")
        self.gridLayout.addWidget(self.ShowmeBtm, 6, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 391, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AnalysisScreenList = QtWidgets.QListWidget(
            self.horizontalLayoutWidget)
        self.AnalysisScreenList.setStyleSheet("color: rgb(0, 0, 0);\n"
                                              "background-color: rgb(232, 232, 232);\n"
                                              )
        self.AnalysisScreenList.setObjectName("AnalysisScreenList")
        self.horizontalLayout.addWidget(self.AnalysisScreenList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RobotikV1"))
        self.AnalysisBtm.setText(_translate("MainWindow", "Analysis"))
        self.pushBtm.setText(_translate("MainWindow", "push"))
        self.resetBtm.setText(_translate("MainWindow", "reset"))
        self.tellmeBtm.setText(_translate("MainWindow", "tell me"))
        self.ShowmeBtm.setText(_translate("MainWindow", "Show me"))
        
        self.ECGBTM.setText(_translate("MainWindow", "OPEN ECG"))

    def F_PushBtm(self):
       
        self.ordersScreenList.addItem(" {} You Push Effector {} ....".format(datetime.now(),
            self.EffectorComboBox.currentText()))
        InterAct(self.EffectorComboBox.currentText())
        self.ordersScreenList.addItem(" {} Add Done".format(datetime.now()  ))

        return 0
    def F_AnalysisBtm(self):
        AutoCheck(self)
        return 0
    
    def F_ShowMeBtm(self): 
        self.ordersScreenList.addItem(
            " {} Show me the Symptom Order".format(datetime.now()))
        self.ordersScreenList.addItem(
            " {} Show me the Symptom Order Done".format(datetime.now()))
     
        F_ShowMeTheSym()
        return 0

    def F_OPENECG(self):
        self.ordersScreenList.addItem(
            " {} OPEN ECG ORDER".format(datetime.now()))
        self.ordersScreenList.addItem(
            " {} OPEN ECG ORDER".format(datetime.now()))
        openEcg()
     
        
        return 0
    def F_TellMeBtm(self): 
        self.ordersScreenList.addItem("{} Tell me the feeling order".format(datetime.now()))
        self.ordersScreenList.addItem(tell_Me_the_Feeling())
        
        return 0
    
    
    def F_ResetBtm(self):
        
        F_Reset()
        self.ordersScreenList.addItem("{} Reset Done".format(datetime.now()))
        return 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
