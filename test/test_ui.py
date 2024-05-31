#纯粹的ui测试文件

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from sys import exit, argv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 667)
        self.actionaaa = QAction(MainWindow)
        self.actionaaa.setObjectName(u"actionaaa")
        self.actionaaa.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.statue = QLabel(self.centralwidget)
        self.statue.setObjectName(u"statue")
        self.statue.setMinimumSize(QSize(140, 0))
        self.statue.setCursor(QCursor(Qt.ForbiddenCursor))
        self.statue.setFrameShape(QFrame.Panel)
        self.statue.setFrameShadow(QFrame.Sunken)
        self.statue.setLineWidth(2)
        self.statue.setTextFormat(Qt.AutoText)
        self.statue.setAlignment(Qt.AlignCenter)
        self.statue.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.statue)

        self.record = QPushButton(self.centralwidget)
        self.record.setObjectName(u"record")

        self.verticalLayout_2.addWidget(self.record)

        self.end_record = QPushButton(self.centralwidget)
        self.end_record.setObjectName(u"end_record")

        self.verticalLayout_2.addWidget(self.end_record)

        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")

        self.verticalLayout_2.addWidget(self.play)

        self.end_play = QPushButton(self.centralwidget)
        self.end_play.setObjectName(u"end_play")

        self.verticalLayout_2.addWidget(self.end_play)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 4, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(720, 540))
        self.label.setMaximumSize(QSize(720, 540))
        self.label.setCursor(QCursor(Qt.ForbiddenCursor))
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.lineEdit.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.capture = QRadioButton(self.centralwidget)
        self.capture.setObjectName(u"capture")

        self.horizontalLayout_3.addWidget(self.capture)

        self.readFiles = QRadioButton(self.centralwidget)
        self.readFiles.setObjectName(u"readFiles")

        self.horizontalLayout_3.addWidget(self.readFiles)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.summit = QPushButton(self.centralwidget)
        self.summit.setObjectName(u"summit")

        self.gridLayout.addWidget(self.summit, 2, 4, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.actionaaa.setText(QCoreApplication.translate("MainWindow", u"aaa", None))
#if QT_CONFIG(statustip)
        self.statue.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.statue.setText("")
        self.record.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236", None))
        self.end_record.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u5f55\u5236", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.end_play.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u64ad\u653e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"opencvLabel", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"sss", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34\u8def\u5f84\u4ee5\u53d1\u9001\u81f3topic", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u6355\u6349", None))
        self.readFiles.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u6587\u4ef6", None))
        self.summit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u8868\u5355", None))
    # retranslateUi


if __name__=="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show() 
    exit(app.exec_())