# CUSTOMIZE THE CONTEXT MENU

# Hello World!!

# import modules for gui and for working with file

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeySequence, QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QAction, QFrame, QTextEdit, QMenu, QMenuBar, QDialog, QPushButton, QShortcut
import sys
import json
import os
import codecs


def openStylesListJson(dirname, name_file):
    try:
        with open(f"{os.getcwd()}\\{dirname}\\{name_file}.json", "r", encoding="utf-8") as file:
            text = json.loads(file.read())
            file.close()
        return text
    except:
        return 0


def getTextFromTextsFile(dirname, name_file):
    try:
        with open(f"{os.getcwd()}\\{dirname}\\{name_file}.txt", "r", encoding="utf-8") as file:
            text = file.read()
            file.close()
        return text
    except:
        print("error")


def GetTextfomFile(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
        file.close()
    return text


def getStyles(jsonList, st="custom"): return "".join(
    [f"{style}:{jsonList[st][style]};\n" for style in jsonList[st]])


def createWriteFile(filename, dirname="texttemp", text="", extension="txt"):
    try:
        with open(f"{dirname}/{filename}.{extension}", "w", encoding="utf-8") as file:
            file.write(text)
            file.close()
        return 1
    except:
        return 0


def checkDiffer(main_file_text, temptext):
    main_text = main_file_text.split("\n")
    temp_text = temptext.split("\n")

    if len(main_text) < len(temp_text) or len(main_text) > len(temp_text):
        return True

    for i in temp_text:
        for j in main_text:
            if len(i) != len(j):
                return True

    return False


def doesFileExist(arroffile, namefile):
    return bool([i for i in [i.split(".")[0] for i in arroffile] if i == namefile])


def getListOfFiles(dirname): return os.listdir(dirname)


class Ui_INoteWindow(QMainWindow):
    # class Ui_INoteWindow(object):
    def setupUi(self, INoteWindow):

        INoteWindow.setObjectName("INoteWindow")
        INoteWindow.resize(500, 500)
        INoteWindow.setWindowIcon(QIcon("icons/main_icon_note.ico"))

        INoteWindow_styles = openStylesListJson("pref", "main_window")
        INoteWindow.setStyleSheet(getStyles(INoteWindow_styles))

        self.centralwidget = QWidget(INoteWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_edit.setObjectName("text_edit")

        text_edit_styles = openStylesListJson("pref", "main_input")
        self.text_edit.setStyleSheet(getStyles(text_edit_styles))

        self.verticalLayout.addWidget(self.text_edit)

        self.devision_hline = QFrame(self.centralwidget)
        self.devision_hline.setFrameShape(QFrame.HLine)
        self.devision_hline.setFrameShadow(QFrame.Sunken)
        self.devision_hline.setObjectName("devision_hline")
        self.verticalLayout.addWidget(self.devision_hline)

        main_window_devision_hline_styles = openStylesListJson(
            "pref", "main_window_devision_hline")
        self.devision_hline.setStyleSheet(
            getStyles(main_window_devision_hline_styles))

        self.bottom_help_bar = QHBoxLayout()
        self.bottom_help_bar.setObjectName("bottom_help_bar")

        self.file_path = QLabel(self.centralwidget)
        self.file_path.setAlignment(QtCore.Qt.AlignCenter)
        self.file_path.setObjectName("file_path")
        self.bottom_help_bar.addWidget(self.file_path)

        bottom_menu_bar_main_window_file_path_styles = openStylesListJson(
            "pref", "bottom_menu_bar_main_window_file_path")
        self.file_path.setStyleSheet(
            getStyles(bottom_menu_bar_main_window_file_path_styles))

        self.devision_vline_1 = QFrame(self.centralwidget)
        self.devision_vline_1.setFrameShape(QFrame.VLine)
        self.devision_vline_1.setFrameShadow(QFrame.Sunken)
        self.devision_vline_1.setObjectName("devision_vline_1")
        self.bottom_help_bar.addWidget(self.devision_vline_1)

        devision_vline_1_styles = openStylesListJson(
            "pref", "main_window_bottom_menu_bar_devision_vline_1")
        self.devision_vline_1.setStyleSheet(getStyles(devision_vline_1_styles))

        self.name_file = QLabel(self.centralwidget)
        self.name_file.setAlignment(QtCore.Qt.AlignCenter)
        self.name_file.setObjectName("name_file")
        self.bottom_help_bar.addWidget(self.name_file)

        self.devision_vline_2 = QFrame(self.centralwidget)
        self.devision_vline_2.setFrameShape(QFrame.VLine)
        self.devision_vline_2.setFrameShadow(QFrame.Sunken)
        self.devision_vline_2.setObjectName("devision_vline_2")
        self.bottom_help_bar.addWidget(self.devision_vline_2)

        self.file_extension = QLabel(self.centralwidget)
        self.file_extension.setAlignment(QtCore.Qt.AlignCenter)
        self.file_extension.setObjectName("file_extension")
        self.bottom_help_bar.addWidget(self.file_extension)

        self.verticalLayout.addLayout(self.bottom_help_bar)
        INoteWindow.setCentralWidget(self.centralwidget)

        self.menu_bar = QMenuBar(INoteWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menu_bar.setObjectName("menu_bar")

        main_window_top_menu_bar_styles = openStylesListJson(
            "pref", "main_window_top_menu_bar")
        self.menu_bar.setStyleSheet(getStyles(main_window_top_menu_bar_styles))

        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_file")

        main_window_top_menu_bar_menu_file_styles = openStylesListJson(
            "pref", "main_window_top_menu_bar_menu_file")
        self.menu_file.setStyleSheet(
            getStyles(main_window_top_menu_bar_menu_file_styles))

        self.menu_edit = QMenu(self.menu_bar)
        self.menu_edit.setObjectName("menu_edit")

        main_window_top_menu_bar_menu_edit_styles = openStylesListJson(
            "pref", "main_window_top_menu_bar_menu_edit")
        self.menu_edit.setStyleSheet(
            getStyles(main_window_top_menu_bar_menu_edit_styles))

        self.menu_edit_saved = QMenu(self.menu_edit)
        self.menu_edit_saved.setObjectName("menu_edit_saved")
        self.menu_edit.triggered.connect(self.open_menu_edit)

        self.menu_settins = QMenu(self.menu_bar)
        self.menu_settins.setObjectName("menu_settins")

        self.menu_info = QMenu(self.menu_bar)
        self.menu_info.setObjectName("menu_info")
        self.menu_info.triggered.connect(self.open_menu_info)

        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName("menu_help")
        self.menu_help.triggered.connect(self.open_menu_help)

        self.menu_find = QMenu(self.menu_bar)
        self.menu_find.setObjectName("menu_find")

        INoteWindow.setMenuBar(self.menu_bar)

        self.open_file = QAction(INoteWindow)
        self.open_file.setIcon(QIcon("icons/open_file_icon.ico"))
        self.open_file.setObjectName("open_file")
        self.open_file.triggered.connect(self.Open_file)
        # self.open_file.setStyleSheet("color:red;")

        self.save_file = QAction(INoteWindow)
        self.save_file.setObjectName("save_file")
        self.save_file.setIcon(QIcon("icons/save_file_icon.ico"))
        self.save_file.triggered.connect(self.Save_file)

        self.save_as_file = QAction(INoteWindow)
        self.save_as_file.setObjectName("save_as_file")
        self.save_as_file.triggered.connect(self.Save_as_file)

        self.open_list = QAction(INoteWindow)
        self.open_list.setObjectName("open_list")

        self.clear_list = QAction(INoteWindow)
        self.clear_list.setObjectName("clear_list")

        self.edit = QAction(INoteWindow)
        self.edit.setIcon(QIcon("icons/edit_INote_icon.ico"))
        self.edit.setObjectName("edit")

        self.new_file = QAction(INoteWindow)
        self.new_file.setIcon(QIcon("icons/new_file_icon.ico"))
        self.new_file.setObjectName("new_file")
        self.new_file.triggered.connect(self.New_file)

        self.exit = QAction(INoteWindow)
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(self.Exit)

        self.edit_default = QAction(INoteWindow)
        self.edit_default.setObjectName("edit_default")

        self.settings_preferences = QAction(INoteWindow)
        self.settings_preferences.setIcon(QIcon("icons/preferences_icon.ico"))
        self.settings_preferences.setObjectName("settings_preferences")

        self.settings_default = QAction(INoteWindow)
        self.settings_default.setObjectName("settings_default")

        self.about_note = QAction(INoteWindow)
        self.about_note.setObjectName("about_note")

        self.actionHelp = QAction(INoteWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.help = QAction(INoteWindow)
        self.help.setObjectName("help")

        self.find = QAction(INoteWindow)
        self.find.setObjectName("find")

        self.menu_file.addAction(self.open_file)
        self.menu_file.addAction(self.new_file)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.save_file)
        self.menu_file.addAction(self.save_as_file)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.exit)

        self.menu_edit_saved.addAction(self.open_list)
        self.menu_edit_saved.addAction(self.clear_list)

        self.menu_edit.addAction(self.edit)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menu_edit_saved.menuAction())
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.edit_default)

        self.menu_settins.addAction(self.settings_preferences)
        self.menu_settins.addSeparator()
        self.menu_settins.addAction(self.settings_default)

        self.menu_info.addAction(self.about_note)
        self.menu_help.addAction(self.help)
        self.menu_find.addAction(self.find)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.menu_bar.addAction(self.menu_settins.menuAction())
        self.menu_bar.addAction(self.menu_info.menuAction())
        self.menu_bar.addAction(self.menu_find.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(INoteWindow)
        QtCore.QMetaObject.connectSlotsByName(INoteWindow)

        self.path = ""

    def New_file(self):
        self.text_edit.setText("")
        self.name_file.setText("New File")
        self.file_path.setText(os.getcwd())

    def pressed(self, event):
        print(event.key())

    def open_menu_help(self):
        menu_help_dialog = QDialog()
        menu_help_dialog.setWindowIcon(QIcon("icons/menu_info_icon.ico"))
        menu_help_dialog.setWindowTitle("Help")
        menu_help_dialog.setFixedSize(300, 300)

        help_menu_dialog_hrlayout = QHBoxLayout(menu_help_dialog)
        help_menu_dialog_hrlayout.setObjectName("help_menu_dialog_hrlayout")

        information_field = QTextEdit(menu_help_dialog)
        information_field.setReadOnly(True)

        text = getTextFromTextsFile("texts", "help_modal_window_text")

        information_field.setPlainText(text)

        style_of_help_dialog_window_text_edit = openStylesListJson(
            "pref", "help_dialog_modal_window_text_edit")

        information_field.setStyleSheet(
            getStyles(style_of_help_dialog_window_text_edit))

        help_menu_dialog_hrlayout.addWidget(information_field)

        menu_help_dialog.exec_()

    def open_menu_edit(self):
        menu_edit = QDialog()
        menu_edit.setWindowTitle("Edit")
        menu_edit.setWindowIcon(QIcon("icons/edit_INote_icon.ico"))

        menu_edit.exec_()

    def open_menu_info(self):
        info_dialog = QDialog()
        info_dialog.setWindowIcon(QIcon("icons/menu_info_icon.ico"))
        info_dialog.setWindowTitle("Info")
        info_dialog.setFixedSize(300, 300)

        info_dialog_hrlayout = QHBoxLayout(info_dialog)
        info_dialog_hrlayout.setObjectName("info_dialog_hrlayout")

        information_field = QTextEdit(info_dialog)
        information_field.setReadOnly(True)

        text = getTextFromTextsFile("texts", "info_modal_window_text")

        information_field.setPlainText(text)

        style_of_info_dialog_window_text_edit = openStylesListJson(
            "pref", "info_dialog_modal_window_text_edit")

        information_field.setStyleSheet(
            getStyles(style_of_info_dialog_window_text_edit))

        info_dialog_hrlayout.addWidget(information_field)

        info_dialog.exec_()

    def Exit(self): sys.exit()

    def Open_file(self):
        filename = QFileDialog.getOpenFileName()[0]

        extension = filename.split("/")[-1].split(".")[-1]
        namefile = filename.split("/")[-1].split(".")[0]
        self.file_extension.setText(f"{extension}")
        self.name_file.setText(namefile)
        self.file_path.setText(filename)

        if not filename:
            return

        try:
            with codecs.open(filename, "rb", encoding="utf-8", errors='replace') as file:
                txt = file.read()
                self.text_edit.setPlainText(txt)
                createWriteFile(namefile, extension="iss")
                createWriteFile(namefile, dirname="savedfiles",
                                text=self.text_edit.toPlainText(), extension="inote")
                file.close()
        except FileNotFoundError:
            return
        except UnicodeDecodeError:
            print(UnicodeDecodeError)
            try:
                with open(filename, "rb") as file:
                    txt = file.read()
                    self.text_edit.setPlainText(str(txt))
                    file.close()
            except UnicodeDecodeError:
                return

    def Save_file(self):
        saved = doesFileExist(getListOfFiles(
            "texttemp"), self.name_file.text())
        if saved:
            text_file_name = f"savedfiles/{self.name_file.text()}.inote"

            # firstly rewrite main file which we opend
            with open(self.file_path.text(), "w", encoding="utf-8") as main_file:
                main_file.write(self.text_edit.toPlainText())
                main_file.close()
            # secondly rewrite temp text file which use to compare files if they are similar
            # with open(text_file_name,"w",encoding="utf-8") as temp_text_file:
            #     temp_text_file.write(self.text_edit.toPlainText())
            #     temp_text_file.close()
        else:
            self.Save_as_file()

    def Save_as_file(self):
        filename = QFileDialog.getSaveFileName()[0]

        if not filename:
            return

        extension = filename.split("/")[-1].split(".")[-1]
        namefile = filename.split("/")[-1].split(".")[0]

        try:
            with open(filename, "w", encoding="utf-16") as file:
                txt = self.text_edit.toPlainText()
                file.write(txt)
                self.file_extension.setText(f"{extension}")
                self.name_file.setText(namefile)
                createWriteFile(namefile, text=txt)
                file.close()
            self.file_path.setText(filename)
        except FileNotFoundError:
            return

    def retranslateUi(self, INoteWindow):

        hot_keys = openStylesListJson("pref", "hot_keys")

        # window title

        INoteWindow.setWindowTitle("INote")

        # text edit

        self.text_edit.setPlaceholderText(
            "Hello World! This INote was developed by @Zyabrik10. Support: sasamazurok@gmail.com. ")

        # file state

        self.file_path.setText(os.getcwd())

        # name file

        self.name_file.setText("New File")

        # file extension

        self.file_extension.setText("txt")

        # menu file

        self.menu_file.setTitle("&File")

        # menu edit

        self.menu_edit.setTitle("&Edit")
        self.menu_edit_saved.setTitle("&Saved")

        # menu settings

        self.menu_settins.setTitle("&Settings")

        # menu info

        self.menu_info.setTitle("&Info")

        # menu help

        self.menu_help.setTitle("&Help")

        # menu find

        self.menu_find.setTitle("&Find")

        # open file

        self.open_file.setShortcut(hot_keys["open_file"])
        self.open_file.setText("&Open &File")

        self.open_file_shortcut = QShortcut(
            QKeySequence(hot_keys["open_file"]), self)
        self.open_file_shortcut.activated.connect(self.Open_file)

        # save file

        self.save_file.setText("&Save")
        self.save_file.setShortcut(hot_keys["save_file"])

        self.save_file_shortcut = QShortcut(
            QKeySequence(hot_keys["save_file"]), self)
        self.save_file_shortcut.activated.connect(self.Save_file)

        # save as file

        self.save_as_file_shortcut = QShortcut(
            QKeySequence(hot_keys["save_as_file"]), self)
        self.save_as_file_shortcut.activated.connect(self.Save_as_file)

        self.save_as_file.setShortcut(hot_keys["save_as_file"])
        self.save_as_file.setText("&Save as...")

        # open list

        self.open_list.setText("&Open &List")

        # clear list

        self.clear_list.setText("&Clear &List")

        # edit

        self.edit.setText("&Edit ")

        # new file

        # self.new_file.setShortcut("Ctrl+N")

        self.new_file_shortcut = QShortcut(
            QKeySequence(hot_keys["new_file"]), self)
        self.new_file_shortcut.activated.connect(self.New_file)

        self.new_file.setShortcut(hot_keys["new_file"])
        self.new_file.setText("&New &File")

        # exit

        self.exit.setText("&Exit")

        # edit default

        self.edit_default.setText("Default")

        # settings preferences

        self.settings_preferences.setText("&Preferences...")

        # settings default

        self.settings_default.setText("&Default")

        #  about note

        self.about_note.setText("About INote")

        # action help

        self.actionHelp.setText("Help")

        # help

        self.help.setText("&Help")

        # find

        self.find.setText("&Find")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    INoteWindow = QMainWindow()
    ui = Ui_INoteWindow()
    ui.setupUi(INoteWindow)
    INoteWindow.show()
    sys.exit(app.exec_())
