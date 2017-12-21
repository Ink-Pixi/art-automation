# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 769)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel\n"
"{\n"
"/*    color: rgb(170, 0, 0);*/\n"
"    color: rgb(0, 0, 0);\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #d7801a;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QListView\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(ui/images/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(ui/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(ui/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}            ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(510, 80, 71, 41))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.vlay_variable_count = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.vlay_variable_count.setContentsMargins(0, 0, 0, 0)
        self.vlay_variable_count.setObjectName("vlay_variable_count")
        self.lbl_variable_count = QtWidgets.QLabel(self.layoutWidget_5)
        self.lbl_variable_count.setObjectName("lbl_variable_count")
        self.vlay_variable_count.addWidget(self.lbl_variable_count)
        self.sbox_variables = QtWidgets.QSpinBox(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sbox_variables.setFont(font)
        self.sbox_variables.setObjectName("sbox_variables")
        self.vlay_variable_count.addWidget(self.sbox_variables)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(103, 81, 252, 42))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.vlay_sku_name = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.vlay_sku_name.setContentsMargins(0, 0, 0, 0)
        self.vlay_sku_name.setObjectName("vlay_sku_name")
        self.lbl_root_sku_name = QtWidgets.QLabel(self.layoutWidget_3)
        self.lbl_root_sku_name.setObjectName("lbl_root_sku_name")
        self.vlay_sku_name.addWidget(self.lbl_root_sku_name)
        self.le_root_sku_name = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.le_root_sku_name.setMinimumSize(QtCore.QSize(250, 0))
        self.le_root_sku_name.setAlignment(QtCore.Qt.AlignCenter)
        self.le_root_sku_name.setObjectName("le_root_sku_name")
        self.vlay_sku_name.addWidget(self.le_root_sku_name)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(16, 81, 71, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vlay_sku = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vlay_sku.setContentsMargins(0, 0, 0, 0)
        self.vlay_sku.setObjectName("vlay_sku")
        self.lbl_root_sku = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_root_sku.setObjectName("lbl_root_sku")
        self.vlay_sku.addWidget(self.lbl_root_sku)
        self.le_root_sku = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_root_sku.setAlignment(QtCore.Qt.AlignCenter)
        self.le_root_sku.setObjectName("le_root_sku")
        self.vlay_sku.addWidget(self.le_root_sku)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(370, 80, 121, 42))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.vlay_root_color = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.vlay_root_color.setContentsMargins(0, 0, 0, 0)
        self.vlay_root_color.setObjectName("vlay_root_color")
        self.lbl_root_color = QtWidgets.QLabel(self.layoutWidget_2)
        self.lbl_root_color.setObjectName("lbl_root_color")
        self.vlay_root_color.addWidget(self.lbl_root_color)
        self.le_root_color = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.le_root_color.setAlignment(QtCore.Qt.AlignCenter)
        self.le_root_color.setObjectName("le_root_color")
        self.vlay_root_color.addWidget(self.le_root_color)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 821, 52))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.hlay_header = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.hlay_header.setContentsMargins(0, 0, 0, 0)
        self.hlay_header.setObjectName("hlay_header")
        self.hlay_search_bar = QtWidgets.QHBoxLayout()
        self.hlay_search_bar.setObjectName("hlay_search_bar")
        self.lbl_search = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_search.setObjectName("lbl_search")
        self.hlay_search_bar.addWidget(self.lbl_search)
        self.le_search_sku = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_search_sku.setText("")
        self.le_search_sku.setObjectName("le_search_sku")
        self.hlay_search_bar.addWidget(self.le_search_sku)
        self.btn_test = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_test.setObjectName("btn_test")
        self.hlay_search_bar.addWidget(self.btn_test)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_search_bar.addItem(spacerItem)
        self.hlay_header.addLayout(self.hlay_search_bar)
        self.lbl_logo = QtWidgets.QLabel(self.layoutWidget1)
        self.lbl_logo.setMinimumSize(QtCore.QSize(165, 50))
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap(":/images/images/pixi_logo_new.png"))
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_logo.setObjectName("lbl_logo")
        self.hlay_header.addWidget(self.lbl_logo)
        self.btn_img = QtWidgets.QToolButton(self.centralwidget)
        self.btn_img.setGeometry(QtCore.QRect(30, 160, 95, 125))
        self.btn_img.setText("")
        self.btn_img.setObjectName("btn_img")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(140, 220, 101, 18))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_mask = QtWidgets.QLabel(self.layoutWidget_4)
        self.lbl_mask.setObjectName("lbl_mask")
        self.horizontalLayout_3.addWidget(self.lbl_mask)
        self.sbox_mask = QtWidgets.QSpinBox(self.layoutWidget_4)
        self.sbox_mask.setObjectName("sbox_mask")
        self.horizontalLayout_3.addWidget(self.sbox_mask)
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(140, 190, 101, 18))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_highlight = QtWidgets.QLabel(self.layoutWidget_6)
        self.lbl_highlight.setObjectName("lbl_highlight")
        self.horizontalLayout_2.addWidget(self.lbl_highlight)
        self.sbox_highlight = QtWidgets.QSpinBox(self.layoutWidget_6)
        self.sbox_highlight.setObjectName("sbox_highlight")
        self.horizontalLayout_2.addWidget(self.sbox_highlight)
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(140, 160, 151, 20))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_7)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbox_ink_type = QtWidgets.QComboBox(self.layoutWidget_7)
        self.cbox_ink_type.setObjectName("cbox_ink_type")
        self.horizontalLayout.addWidget(self.cbox_ink_type)
        self.layoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(140, 310, 121, 18))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_ink_vol = QtWidgets.QLabel(self.layoutWidget_8)
        self.lbl_ink_vol.setObjectName("lbl_ink_vol")
        self.horizontalLayout_4.addWidget(self.lbl_ink_vol)
        self.sbox_ink_vol = QtWidgets.QSpinBox(self.layoutWidget_8)
        self.sbox_ink_vol.setObjectName("sbox_ink_vol")
        self.horizontalLayout_4.addWidget(self.sbox_ink_vol)
        self.chk_background = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_background.setGeometry(QtCore.QRect(140, 250, 141, 16))
        self.chk_background.setStyleSheet("font-weight: bold;\n"
"font-size: 12px;\n"
"")
        self.chk_background.setObjectName("chk_background")
        self.chk_multi_pass = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_multi_pass.setGeometry(QtCore.QRect(140, 280, 181, 16))
        self.chk_multi_pass.setStyleSheet("font-weight: bold;\n"
"font-size: 12px;\n"
"")
        self.chk_multi_pass.setObjectName("chk_multi_pass")
        self.layoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_9.setGeometry(QtCore.QRect(140, 340, 121, 18))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_dbl_print = QtWidgets.QLabel(self.layoutWidget_9)
        self.lbl_dbl_print.setObjectName("lbl_dbl_print")
        self.horizontalLayout_5.addWidget(self.lbl_dbl_print)
        self.sbox_dbl_print = QtWidgets.QSpinBox(self.layoutWidget_9)
        self.sbox_dbl_print.setObjectName("sbox_dbl_print")
        self.horizontalLayout_5.addWidget(self.sbox_dbl_print)
        self.chk_transparent = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_transparent.setGeometry(QtCore.QRect(140, 370, 141, 16))
        self.chk_transparent.setStyleSheet("font-weight: bold;\n"
"font-size: 12px;\n"
"")
        self.chk_transparent.setObjectName("chk_transparent")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(740, 680, 75, 23))
        self.btn_update.setObjectName("btn_update")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(600, 80, 80, 41))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_alt_sweat = QtWidgets.QCheckBox(self.widget)
        self.chk_alt_sweat.setStyleSheet("font-weight: bold;\n"
"font-size: 12px;\n"
"")
        self.chk_alt_sweat.setObjectName("chk_alt_sweat")
        self.verticalLayout.addWidget(self.chk_alt_sweat)
        self.chk_active = QtWidgets.QCheckBox(self.widget)
        self.chk_active.setStyleSheet("font-weight: bold;\n"
"font-size: 12px;\n"
"")
        self.chk_active.setObjectName("chk_active")
        self.verticalLayout.addWidget(self.chk_active)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(700, 80, 131, 40))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.cbox_garm_types = QtWidgets.QComboBox(self.widget1)
        self.cbox_garm_types.setObjectName("cbox_garm_types")
        self.cbox_garm_types.addItem("")
        self.verticalLayout_2.addWidget(self.cbox_garm_types)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.le_search_sku, self.btn_test)
        MainWindow.setTabOrder(self.btn_test, self.le_root_sku)
        MainWindow.setTabOrder(self.le_root_sku, self.le_root_sku_name)
        MainWindow.setTabOrder(self.le_root_sku_name, self.le_root_color)
        MainWindow.setTabOrder(self.le_root_color, self.sbox_variables)
        MainWindow.setTabOrder(self.sbox_variables, self.chk_active)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Products, products, products for everyone."))
        self.lbl_variable_count.setText(_translate("MainWindow", "Variables:"))
        self.lbl_root_sku_name.setText(_translate("MainWindow", "Design Name:"))
        self.lbl_root_sku.setText(_translate("MainWindow", "SKU:"))
        self.lbl_root_color.setText(_translate("MainWindow", "Root Color:"))
        self.lbl_search.setText(_translate("MainWindow", "Search:"))
        self.btn_test.setText(_translate("MainWindow", "   Get   "))
        self.lbl_mask.setText(_translate("MainWindow", "Mask:"))
        self.lbl_highlight.setText(_translate("MainWindow", "Highlight:"))
        self.label.setText(_translate("MainWindow", "Ink Type:"))
        self.lbl_ink_vol.setText(_translate("MainWindow", "Ink Volume"))
        self.chk_background.setText(_translate("MainWindow", "Background Color"))
        self.chk_multi_pass.setText(_translate("MainWindow", "Color Multi Pass Printing"))
        self.lbl_dbl_print.setText(_translate("MainWindow", "Double Print"))
        self.chk_transparent.setText(_translate("MainWindow", "Transparent Color"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.chk_alt_sweat.setText(_translate("MainWindow", "Alt Sweat"))
        self.chk_active.setText(_translate("MainWindow", "Active"))
        self.label_2.setText(_translate("MainWindow", "Garment:"))
        self.cbox_garm_types.setItemText(0, _translate("MainWindow", "-- choose garment --"))

import resources_rc
