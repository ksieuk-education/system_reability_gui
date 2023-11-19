from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 749)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/calculator.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet(
            "QListWidget{\n"
            "    selection-background-color: rgb(129, 136, 188);\n"
            "}\n"
            "\n"
            "QScrollBar:vertical, QScrollBar:horizontal{\n"
            "    border: none;\n"
            "    background-color: rgb(243, 243, 248);\n"
            "    width: 6px;\n"
            "    margin: 0px 0 0px 0;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle::vertical, QScrollBar::handle::horizontal{\n"
            "    background-color: rgb(202, 203, 213);\n"
            "    width: 3px;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle::vertical:hover, QScrollBar::handle::horizontal:hover{\n"
            "    background-color: rgb(202, 203, 213);\n"
            "}\n"
            "\n"
            "QScrollBar::handle::vertical:pressed, QScrollBar::handle::horizontal:pressed{\n"
            "    background-color:rgb(129, 136, 188);\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal{\n"
            "    border: none;\n"
            "    background-color: rgb(243, 243, 248);\n"
            "    height: 8px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-top-left-radius: 3px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line::vertical:hover, QScrollBar::sub-line::horizontal:hover{\n"
            "    background-color: rgb(202, 203, 213);\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line::vertical:pressed, QScrollBar::sub-line::horizontal:pressed{\n"
            "    background-color:rgb(129, 136, 188);\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal{\n"
            "    border: none;\n"
            "    background-color: rgb(243, 243, 248);\n"
            "    height: 8px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-top-left-radius: 3px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line::vertical:hover, QScrollBar::add-line::horizontal:hover{\n"
            "    background-color: rgb(202, 203, 213);\n"
            "}\n"
            "\n"
            "QScrollBar::add-line::vertical:pressed, QScrollBar::add-line::horizontal:pressed{\n"
            "    background-color:rgb(129, 136, 188);\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::ad-page:vertical, QScrollBar::sub-page:vertical, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
            "    background: none;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_labs = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_labs.setStyleSheet(
            "QComboBox {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 18px 1px 3px;\n"
            "    min-width: 6em;\n"
            "    color: black;\n"
            "    selection-background-color: rgb(240, 240, 240);\n"
            "    selection-color: rgb(25, 25, 25);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    color: rgb(240, 240, 240);\n"
            "    background:  rgb(240, 240, 240);\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 18px 1px 3px;\n"
            "    min-width: 6em;\n"
            "}\n"
            "\n"
            "QComboBox:on { /* shift the text when the popup opens */\n"
            "    padding-top: 3px;\n"
            "    padding-left: 4px;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    border: 0px;\n"
            "\n"
            "    border-left-width: 1px;\n"
            "    border-left-color: darkgray;\n"
            "    border-left-style: solid; /* just a single line */\n"
            "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
            "    border-bottom-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
            "    top: 1px;\n"
            "    left: 1px;\n"
            "}"
        )
        self.cb_labs.setObjectName("cb_labs")
        self.horizontalLayout.addWidget(self.cb_labs)
        self.cb_variants = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_variants.setStyleSheet(
            "QComboBox {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 18px 1px 3px;\n"
            "    min-width: 6em;\n"
            "    color: black;\n"
            "    selection-background-color: rgb(240, 240, 240);\n"
            "    selection-color: rgb(25, 25, 25);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    color: rgb(240, 240, 240);\n"
            "    background:  rgb(240, 240, 240);\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 18px 1px 3px;\n"
            "    min-width: 6em;\n"
            "}\n"
            "\n"
            "QComboBox:on { /* shift the text when the popup opens */\n"
            "    padding-top: 3px;\n"
            "    padding-left: 4px;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 0px;\n"
            "    height: 0px;\n"
            "    border: 0px;\n"
            "\n"
            "    border-left-width: 1px;\n"
            "    border-left-color: darkgray;\n"
            "    border-left-style: solid; /* just a single line */\n"
            "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
            "    border-bottom-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
            "    top: 1px;\n"
            "    left: 1px;\n"
            "}"
        )
        self.cb_variants.setObjectName("cb_variants")
        self.horizontalLayout.addWidget(self.cb_variants)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layout_all = QtWidgets.QHBoxLayout()
        self.layout_all.setObjectName("layout_all")
        self.layout_input = QtWidgets.QVBoxLayout()
        self.layout_input.setObjectName("layout_input")
        self.list_methods = QtWidgets.QListWidget(parent=self.centralwidget)
        self.list_methods.setEnabled(True)
        self.list_methods.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.list_methods.setFont(font)
        self.list_methods.setStyleSheet(
            "QListWidget{\n"
            "    color: black;\n"
            "    border: 1px solid black;\n"
            "    border-radius: 10px;\n"
            "    selection-background-color: rgb(140, 200, 218);\n"
            '    font: 14px "Fira Sans", sans-serif;\n'
            "}\n"
            "\n"
            "QScrollBar:horizontal {\n"
            "    border: 2px solid green;\n"
            "    background: cyan;\n"
            "    height: 15px;\n"
            "    margin: 0px 40px 0 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: gray;\n"
            "    min-width: 20px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:horizontal {\n"
            "    background: blue;\n"
            "    width: 16px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "    border: 2px solid black;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    background: magenta;\n"
            "    width: 16px;\n"
            "    subcontrol-position: top right;\n"
            "    subcontrol-origin: margin;\n"
            "    border: 2px solid black;\n"
            "    position: absolute;\n"
            "    right: 20px;\n"
            "}\n"
            "\n"
            "QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
            "    width: 3px;\n"
            "    height: 3px;\n"
            "    background: pink;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            "    background: none;\n"
            "}"
        )
        self.list_methods.setObjectName("list_methods")
        self.layout_input.addWidget(self.list_methods)
        self.layout_input.setStretch(0, 1)
        self.layout_all.addLayout(self.layout_input)
        self.layout_output_pictures = QtWidgets.QVBoxLayout()
        self.layout_output_pictures.setObjectName("layout_output_pictures")
        self.layout_all.addLayout(self.layout_output_pictures)
        self.verticalLayout.addLayout(self.layout_all)
        self.list_input = QtWidgets.QListWidget(parent=self.centralwidget)
        self.list_input.setStyleSheet(
            "QWidget{\n"
            "    color: black;\n"
            "    border: 1px solid black;\n"
            "    border-radius: 10px;\n"
            '    font: 22px "Ubuntu Light", sans-serif, center;\n'
            "}\n"
            ""
        )
        self.list_input.setObjectName("list_input")
        self.verticalLayout.addWidget(self.list_input)
        self.pb_calculate = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_calculate.sizePolicy().hasHeightForWidth())
        self.pb_calculate.setSizePolicy(sizePolicy)
        self.pb_calculate.setMinimumSize(QtCore.QSize(0, 50))
        self.pb_calculate.setStyleSheet(
            "QPushButton{\n"
            "    color: white;\n"
            "    border: 1px solid rgb(77, 83, 139);    \n"
            "    background-color:rgb(0,149,218);\n"
            "    border-radius: 10px;\n"
            '    font: 24px "Fira Sans", sans-serif, center;\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: black;  \n"
            "    background-color: rgb(140, 200, 218);\n"
            '    font: 24px "Fira Sans", sans-serif, center;\n'
            "}"
        )
        self.pb_calculate.setObjectName("pb_calculate")
        self.verticalLayout.addWidget(self.pb_calculate)
        self.layout_output = QtWidgets.QHBoxLayout()
        self.layout_output.setObjectName("layout_output")
        self.text_entry = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_entry.setStyleSheet(
            "QTextBrowser{\n"
            "    text-align: center;\n"
            "    height: 300%;\n"
            "    width: 100%;\n"
            "    color: black;\n"
            "    border: 1px solid rgb(156, 154, 161);\n"
            "    border-radius: 10px;\n"
            '    font: 22px "Fira Sans", sans-serif;\n'
            "}"
        )
        self.text_entry.setReadOnly(True)
        self.text_entry.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse
        )
        self.text_entry.setObjectName("text_entry")
        self.layout_output.addWidget(self.text_entry)
        self.verticalLayout.addLayout(self.layout_output)
        self.lbl_temp = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_temp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet("color: #888;")
        self.lbl_temp.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.lbl_temp.setObjectName("lbl_temp")
        self.verticalLayout.addWidget(self.lbl_temp)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Надежность информационных систем"))
        self.pb_calculate.setText(_translate("MainWindow", "Выполнить"))
        self.text_entry.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Fira Sans','sans-serif'; font-size:22px; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Fira Sans,sans-serif'; font-size:36px;\"><br /></p></body></html>",
            )
        )
