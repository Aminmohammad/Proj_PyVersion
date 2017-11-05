import ast
import timeit

from tkinter import filedialog, Tk

import os

from GeneralTools.PickleLoader.pickle_file_loader import pickle_file_loader
from GeneralTools.PickleSaver.pickle_file_saver import pickle_file_saver
from GeneralTools.RootProjectFolderAddressExtractor.root_project_folder_address_extractor import \
    root_project_folder_address_extractor

from PyQt5 import QtCore, QtGui, QtWidgets

from Start.PythonStarter.main_GUI import main_GUI

class Ui_GUIStart(object):
    def setupUi(self, GUIStart):
        GUIStart.setObjectName("GUIStart")
        GUIStart.resize(1237, 1066)
        GUIStart.setToolTip("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(GUIStart)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TabsLayout = QtWidgets.QVBoxLayout()
        self.TabsLayout.setObjectName("TabsLayout")
        self.Program_Tabs = QtWidgets.QTabWidget(GUIStart)
        self.Program_Tabs.setEnabled(True)
        self.Program_Tabs.setObjectName("Program_Tabs")
        self.tab_general = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_general.sizePolicy().hasHeightForWidth())
        self.tab_general.setSizePolicy(sizePolicy)
        self.tab_general.setObjectName("tab_general")
        self.et_project_name = QtWidgets.QPlainTextEdit(self.tab_general)
        self.et_project_name.setGeometry(QtCore.QRect(299, 30, 181, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.et_project_name.sizePolicy().hasHeightForWidth())
        self.et_project_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_project_name.setFont(font)
        self.et_project_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.et_project_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_project_name.setCenterOnScroll(True)
        self.et_project_name.setObjectName("et_project_name")
        self.st0 = QtWidgets.QPlainTextEdit(self.tab_general)
        self.st0.setGeometry(QtCore.QRect(50, 30, 201, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st0.setFont(font)
        self.st0.setAutoFillBackground(False)
        self.st0.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st0.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st0.setCenterOnScroll(True)
        self.st0.setObjectName("st0")
        self.mdarea_general = QtWidgets.QMdiArea(self.tab_general)
        self.mdarea_general.setGeometry(QtCore.QRect(0, 10, 1411, 1051))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdarea_general.sizePolicy().hasHeightForWidth())
        self.mdarea_general.setSizePolicy(sizePolicy)
        brush = QtGui.QBrush(QtGui.QColor(111, 186, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdarea_general.setBackground(brush)
        self.mdarea_general.setObjectName("mdarea_general")
        self.mdarea_general.raise_()
        self.et_project_name.raise_()
        self.st0.raise_()
        self.Program_Tabs.addTab(self.tab_general, "")
        self.tab_data_set = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_data_set.sizePolicy().hasHeightForWidth())
        self.tab_data_set.setSizePolicy(sizePolicy)
        self.tab_data_set.setObjectName("tab_data_set")
        self.data_set_address_groupBox = QtWidgets.QGroupBox(self.tab_data_set)
        self.data_set_address_groupBox.setGeometry(QtCore.QRect(30, 19, 181, 91))
        self.data_set_address_groupBox.setObjectName("data_set_address_groupBox")
        self.rbtn_data_set_name = QtWidgets.QRadioButton(self.data_set_address_groupBox)
        self.rbtn_data_set_name.setGeometry(QtCore.QRect(20, 21, 141, 21))
        self.rbtn_data_set_name.setChecked(True)
        self.rbtn_data_set_name.setObjectName("rbtn_data_set_name")
        self.rbtn_data_set_address = QtWidgets.QRadioButton(self.data_set_address_groupBox)
        self.rbtn_data_set_address.setGeometry(QtCore.QRect(20, 56, 151, 21))
        self.rbtn_data_set_address.setChecked(False)
        self.rbtn_data_set_address.setObjectName("rbtn_data_set_address")
        self.st1 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st1.setGeometry(QtCore.QRect(30, 176, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st1.setFont(font)
        self.st1.setAutoFillBackground(False)
        self.st1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st1.setCenterOnScroll(True)
        self.st1.setObjectName("st1")
        self.et_zero_conversion_threshold = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_zero_conversion_threshold.setGeometry(QtCore.QRect(350, 176, 141, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.et_zero_conversion_threshold.sizePolicy().hasHeightForWidth())
        self.et_zero_conversion_threshold.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_zero_conversion_threshold.setFont(font)
        self.et_zero_conversion_threshold.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.et_zero_conversion_threshold.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_zero_conversion_threshold.setCenterOnScroll(True)
        self.et_zero_conversion_threshold.setObjectName("et_zero_conversion_threshold")
        self.et_No_sR = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_No_sR.setGeometry(QtCore.QRect(350, 226, 141, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_No_sR.setFont(font)
        self.et_No_sR.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_No_sR.setCenterOnScroll(True)
        self.et_No_sR.setObjectName("et_No_sR")
        self.st2 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st2.setGeometry(QtCore.QRect(30, 226, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st2.setFont(font)
        self.st2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st2.setCenterOnScroll(True)
        self.st2.setObjectName("st2")
        self.et_No_chips_in_sR = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_No_chips_in_sR.setGeometry(QtCore.QRect(350, 326, 141, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_No_chips_in_sR.setFont(font)
        self.et_No_chips_in_sR.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_No_chips_in_sR.setCenterOnScroll(True)
        self.et_No_chips_in_sR.setObjectName("et_No_chips_in_sR")
        self.et_No_Symbols_preamb = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_No_Symbols_preamb.setGeometry(QtCore.QRect(350, 276, 141, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_No_Symbols_preamb.setFont(font)
        self.et_No_Symbols_preamb.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_No_Symbols_preamb.setCenterOnScroll(True)
        self.et_No_Symbols_preamb.setObjectName("et_No_Symbols_preamb")
        self.st4 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st4.setGeometry(QtCore.QRect(30, 326, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st4.setFont(font)
        self.st4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st4.setCenterOnScroll(True)
        self.st4.setObjectName("st4")
        self.st3 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st3.setGeometry(QtCore.QRect(30, 276, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st3.setFont(font)
        self.st3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st3.setCenterOnScroll(True)
        self.st3.setObjectName("st3")
        self.et_sampling_frequency = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_sampling_frequency.setGeometry(QtCore.QRect(350, 426, 141, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_sampling_frequency.setFont(font)
        self.et_sampling_frequency.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_sampling_frequency.setCenterOnScroll(True)
        self.et_sampling_frequency.setObjectName("et_sampling_frequency")
        self.et_chip_length = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_chip_length.setGeometry(QtCore.QRect(350, 376, 141, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_chip_length.setFont(font)
        self.et_chip_length.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_chip_length.setCenterOnScroll(True)
        self.et_chip_length.setObjectName("et_chip_length")
        self.st7 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st7.setGeometry(QtCore.QRect(30, 476, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st7.setFont(font)
        self.st7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st7.setCenterOnScroll(True)
        self.st7.setObjectName("st7")
        self.st6 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st6.setGeometry(QtCore.QRect(30, 426, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st6.setFont(font)
        self.st6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st6.setCenterOnScroll(True)
        self.st6.setObjectName("st6")
        self.st5 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st5.setGeometry(QtCore.QRect(30, 376, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st5.setFont(font)
        self.st5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st5.setCenterOnScroll(True)
        self.st5.setObjectName("st5")
        self.et_communication_frequency = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_communication_frequency.setGeometry(QtCore.QRect(350, 476, 141, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.et_communication_frequency.setFont(font)
        self.et_communication_frequency.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.et_communication_frequency.setCenterOnScroll(True)
        self.et_communication_frequency.setObjectName("et_communication_frequency")
        self.st12 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st12.setGeometry(QtCore.QRect(30, 750, 291, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st12.setFont(font)
        self.st12.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st12.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st12.setCenterOnScroll(True)
        self.st12.setObjectName("st12")
        self.st8 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st8.setGeometry(QtCore.QRect(30, 536, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st8.setFont(font)
        self.st8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st8.setCenterOnScroll(True)
        self.st8.setObjectName("st8")
        self.rbgroup_data_set_save = QtWidgets.QGroupBox(self.tab_data_set)
        self.rbgroup_data_set_save.setGeometry(QtCore.QRect(351, 530, 141, 41))
        self.rbgroup_data_set_save.setTitle("")
        self.rbgroup_data_set_save.setObjectName("rbgroup_data_set_save")
        self.rbtn_save_data_set = QtWidgets.QRadioButton(self.rbgroup_data_set_save)
        self.rbtn_save_data_set.setGeometry(QtCore.QRect(15, 7, 61, 31))
        self.rbtn_save_data_set.setChecked(True)
        self.rbtn_save_data_set.setObjectName("rbtn_save_data_set")
        self.rbtn_dont_save_data_set = QtWidgets.QRadioButton(self.rbgroup_data_set_save)
        self.rbtn_dont_save_data_set.setGeometry(QtCore.QRect(85, 6, 61, 31))
        self.rbtn_dont_save_data_set.setObjectName("rbtn_dont_save_data_set")
        self.st9 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st9.setGeometry(QtCore.QRect(30, 600, 270, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st9.setFont(font)
        self.st9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st9.setCenterOnScroll(True)
        self.st9.setObjectName("st9")
        self.st10 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st10.setGeometry(QtCore.QRect(880, 280, 201, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st10.setFont(font)
        self.st10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st10.setCenterOnScroll(True)
        self.st10.setObjectName("st10")
        self.et_data_set_extractor_methods = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.et_data_set_extractor_methods.setGeometry(QtCore.QRect(353, 660, 471, 151))
        self.et_data_set_extractor_methods.setPlaceholderText("")
        self.et_data_set_extractor_methods.setObjectName("et_data_set_extractor_methods")
        self.btn_dat_set_extractor_method_ex = QtWidgets.QPushButton(self.tab_data_set)
        self.btn_dat_set_extractor_method_ex.setGeometry(QtCore.QRect(90, 790, 75, 23))
        self.btn_dat_set_extractor_method_ex.setObjectName("btn_dat_set_extractor_method_ex")
        self.et_data_set_name = QtWidgets.QTextEdit(self.tab_data_set)
        self.et_data_set_name.setGeometry(QtCore.QRect(242, 30, 1146, 30))
        self.et_data_set_name.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.et_data_set_name.setPlaceholderText("")
        self.et_data_set_name.setObjectName("et_data_set_name")
        self.et_data_set_address = QtWidgets.QTextEdit(self.tab_data_set)
        self.et_data_set_address.setGeometry(QtCore.QRect(320, 70, 1071, 30))
        self.et_data_set_address.setDocumentTitle("")
        self.et_data_set_address.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.et_data_set_address.setPlaceholderText("")
        self.et_data_set_address.setObjectName("et_data_set_address")
        self.btn_brows_data_set = QtWidgets.QPushButton(self.tab_data_set)
        self.btn_brows_data_set.setGeometry(QtCore.QRect(240, 70, 75, 31))
        self.btn_brows_data_set.setObjectName("btn_brows_data_set")
        self.mdiArea_3 = QtWidgets.QMdiArea(self.tab_data_set)
        self.mdiArea_3.setGeometry(QtCore.QRect(20, 10, 1401, 111))
        brush = QtGui.QBrush(QtGui.QColor(223, 149, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea_3.setBackground(brush)
        self.mdiArea_3.setObjectName("mdiArea_3")
        self.mdarea_make_data_set_1 = QtWidgets.QMdiArea(self.tab_data_set)
        self.mdarea_make_data_set_1.setGeometry(QtCore.QRect(22, 120, 701, 841))
        brush = QtGui.QBrush(QtGui.QColor(210, 238, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdarea_make_data_set_1.setBackground(brush)
        self.mdarea_make_data_set_1.setObjectName("mdarea_make_data_set_1")
        self.mdarea_load_data_set = QtWidgets.QMdiArea(self.tab_data_set)
        self.mdarea_load_data_set.setGeometry(QtCore.QRect(720, 120, 701, 261))
        brush = QtGui.QBrush(QtGui.QColor(219, 239, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdarea_load_data_set.setBackground(brush)
        self.mdarea_load_data_set.setObjectName("mdarea_load_data_set")
        self.st11 = QtWidgets.QPlainTextEdit(self.tab_data_set)
        self.st11.setGeometry(QtCore.QRect(832, 420, 511, 391))
        self.st11.setPlaceholderText("{1: {         \"module_name\":             \"no_change_char\",         \"class_name\": \"\",         \"method_name\":             \"no_change_char\",         \"special_parameters\":             {\"\"}     }")
        self.st11.setObjectName("st11")
        self.mdarea_make_data_set_2 = QtWidgets.QMdiArea(self.tab_data_set)
        self.mdarea_make_data_set_2.setGeometry(QtCore.QRect(550, 380, 871, 581))
        brush = QtGui.QBrush(QtGui.QColor(210, 238, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdarea_make_data_set_2.setBackground(brush)
        self.mdarea_make_data_set_2.setObjectName("mdarea_make_data_set_2")
        self.group_saving_data_set = QtWidgets.QGroupBox(self.tab_data_set)
        self.group_saving_data_set.setGeometry(QtCore.QRect(353, 606, 180, 41))
        self.group_saving_data_set.setTitle("")
        self.group_saving_data_set.setObjectName("group_saving_data_set")
        self.rbtn_data_set_saving_format_txt = QtWidgets.QRadioButton(self.group_saving_data_set)
        self.rbtn_data_set_saving_format_txt.setGeometry(QtCore.QRect(16, 4, 81, 23))
        self.rbtn_data_set_saving_format_txt.setChecked(True)
        self.rbtn_data_set_saving_format_txt.setObjectName("rbtn_data_set_saving_format_txt")
        self.group_data_set = QtWidgets.QGroupBox(self.tab_data_set)
        self.group_data_set.setGeometry(QtCore.QRect(1120, 273, 180, 41))
        self.group_data_set.setTitle("")
        self.group_data_set.setObjectName("group_data_set")
        self.rbtn_data_set_loading_format_txt = QtWidgets.QRadioButton(self.group_data_set)
        self.rbtn_data_set_loading_format_txt.setGeometry(QtCore.QRect(16, 10, 119, 23))
        self.rbtn_data_set_loading_format_txt.setChecked(True)
        self.rbtn_data_set_loading_format_txt.setObjectName("rbtn_data_set_loading_format_txt")
        self.groupBox = QtWidgets.QGroupBox(self.tab_data_set)
        self.groupBox.setGeometry(QtCore.QRect(279, 130, 891, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.rbtn_load_new_data_set = QtWidgets.QRadioButton(self.groupBox)
        self.rbtn_load_new_data_set.setGeometry(QtCore.QRect(690, 10, 191, 21))
        self.rbtn_load_new_data_set.setObjectName("rbtn_load_new_data_set")
        self.rbtn_make_new_data_set = QtWidgets.QRadioButton(self.groupBox)
        self.rbtn_make_new_data_set.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.rbtn_make_new_data_set.setChecked(True)
        self.rbtn_make_new_data_set.setObjectName("rbtn_make_new_data_set")
        self.mdarea_make_data_set_2.raise_()
        self.mdarea_load_data_set.raise_()
        self.mdarea_make_data_set_1.raise_()
        self.mdiArea_3.raise_()
        self.st1.raise_()
        self.et_zero_conversion_threshold.raise_()
        self.et_No_sR.raise_()
        self.st2.raise_()
        self.et_No_chips_in_sR.raise_()
        self.et_No_Symbols_preamb.raise_()
        self.st4.raise_()
        self.st3.raise_()
        self.et_sampling_frequency.raise_()
        self.et_chip_length.raise_()
        self.st7.raise_()
        self.st6.raise_()
        self.st5.raise_()
        self.et_communication_frequency.raise_()
        self.st12.raise_()
        self.st8.raise_()
        self.rbgroup_data_set_save.raise_()
        self.st9.raise_()
        self.st10.raise_()
        self.et_data_set_extractor_methods.raise_()
        self.btn_dat_set_extractor_method_ex.raise_()
        self.data_set_address_groupBox.raise_()
        self.et_data_set_name.raise_()
        self.et_data_set_address.raise_()
        self.btn_brows_data_set.raise_()
        self.st11.raise_()
        self.group_saving_data_set.raise_()
        self.group_data_set.raise_()
        self.groupBox.raise_()
        self.Program_Tabs.addTab(self.tab_data_set, "")
        self.tab_preProcessing = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_preProcessing.sizePolicy().hasHeightForWidth())
        self.tab_preProcessing.setSizePolicy(sizePolicy)
        self.tab_preProcessing.setObjectName("tab_preProcessing")
        self.st13 = QtWidgets.QPlainTextEdit(self.tab_preProcessing)
        self.st13.setGeometry(QtCore.QRect(30, 100, 201, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st13.setFont(font)
        self.st13.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st13.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st13.setCenterOnScroll(True)
        self.st13.setObjectName("st13")
        self.st15 = QtWidgets.QPlainTextEdit(self.tab_preProcessing)
        self.st15.setGeometry(QtCore.QRect(90, 242, 351, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st15.setFont(font)
        self.st15.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st15.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st15.setCenterOnScroll(True)
        self.st15.setObjectName("st15")
        self.st14 = QtWidgets.QPlainTextEdit(self.tab_preProcessing)
        self.st14.setGeometry(QtCore.QRect(90, 180, 351, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st14.setFont(font)
        self.st14.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st14.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st14.setCenterOnScroll(True)
        self.st14.setObjectName("st14")
        self.st16 = QtWidgets.QPlainTextEdit(self.tab_preProcessing)
        self.st16.setGeometry(QtCore.QRect(90, 450, 321, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st16.setFont(font)
        self.st16.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st16.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st16.setCenterOnScroll(True)
        self.st16.setObjectName("st16")
        self.btn_preProcess_methods_ex = QtWidgets.QPushButton(self.tab_preProcessing)
        self.btn_preProcess_methods_ex.setGeometry(QtCore.QRect(220, 500, 75, 23))
        self.btn_preProcess_methods_ex.setObjectName("btn_preProcess_methods_ex")
        self.mdarea_preProcess = QtWidgets.QMdiArea(self.tab_preProcessing)
        self.mdarea_preProcess.setGeometry(QtCore.QRect(0, 0, 1421, 961))
        brush = QtGui.QBrush(QtGui.QColor(221, 238, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdarea_preProcess.setBackground(brush)
        self.mdarea_preProcess.setObjectName("mdarea_preProcess")
        self.et_preProcessed_methods = QtWidgets.QPlainTextEdit(self.tab_preProcessing)
        self.et_preProcessed_methods.setGeometry(QtCore.QRect(420, 290, 441, 481))
        self.et_preProcessed_methods.setPlaceholderText("")
        self.et_preProcessed_methods.setObjectName("et_preProcessed_methods")
        self.st17 = QtWidgets.QPlainTextEdit(self.tab_preProcessing)
        self.st17.setGeometry(QtCore.QRect(870, 10, 541, 761))
        self.st17.setPlaceholderText("{1: {         \"module_name\":             \"no_change_char\",         \"class_name\": \"\",         \"method_name\":             \"no_change_char\",         \"special_parameters\":             {\"\"}     }")
        self.st17.setObjectName("st17")
        self.group_saving_preProcessed_data_set = QtWidgets.QGroupBox(self.tab_preProcessing)
        self.group_saving_preProcessed_data_set.setGeometry(QtCore.QRect(490, 237, 180, 41))
        self.group_saving_preProcessed_data_set.setTitle("")
        self.group_saving_preProcessed_data_set.setObjectName("group_saving_preProcessed_data_set")
        self.rbtn_saving_preProcessed_data_set_txt = QtWidgets.QRadioButton(self.group_saving_preProcessed_data_set)
        self.rbtn_saving_preProcessed_data_set_txt.setGeometry(QtCore.QRect(10, 10, 62, 21))
        self.rbtn_saving_preProcessed_data_set_txt.setChecked(True)
        self.rbtn_saving_preProcessed_data_set_txt.setObjectName("rbtn_saving_preProcessed_data_set_txt")
        self.group_save_preProcess = QtWidgets.QGroupBox(self.tab_preProcessing)
        self.group_save_preProcess.setGeometry(QtCore.QRect(480, 177, 171, 41))
        self.group_save_preProcess.setTitle("")
        self.group_save_preProcess.setObjectName("group_save_preProcess")
        self.rbtn_save_preProcessed_data_set = QtWidgets.QRadioButton(self.group_save_preProcess)
        self.rbtn_save_preProcessed_data_set.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.rbtn_save_preProcessed_data_set.setChecked(True)
        self.rbtn_save_preProcessed_data_set.setObjectName("rbtn_save_preProcessed_data_set")
        self.rbtn_dont_save_preProcessed_data_set = QtWidgets.QRadioButton(self.group_save_preProcess)
        self.rbtn_dont_save_preProcessed_data_set.setGeometry(QtCore.QRect(90, 10, 61, 21))
        self.rbtn_dont_save_preProcessed_data_set.setObjectName("rbtn_dont_save_preProcessed_data_set")
        self.group_run_preProcess = QtWidgets.QGroupBox(self.tab_preProcessing)
        self.group_run_preProcess.setGeometry(QtCore.QRect(240, 96, 171, 41))
        self.group_run_preProcess.setTitle("")
        self.group_run_preProcess.setObjectName("group_run_preProcess")
        self.rbtn_run_preProcess = QtWidgets.QRadioButton(self.group_run_preProcess)
        self.rbtn_run_preProcess.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.rbtn_run_preProcess.setChecked(True)
        self.rbtn_run_preProcess.setObjectName("rbtn_run_preProcess")
        self.rbtn_dont_run_preProcess = QtWidgets.QRadioButton(self.group_run_preProcess)
        self.rbtn_dont_run_preProcess.setGeometry(QtCore.QRect(90, 10, 61, 21))
        self.rbtn_dont_run_preProcess.setObjectName("rbtn_dont_run_preProcess")
        self.mdarea_preProcess.raise_()
        self.st13.raise_()
        self.st15.raise_()
        self.st14.raise_()
        self.st16.raise_()
        self.btn_preProcess_methods_ex.raise_()
        self.et_preProcessed_methods.raise_()
        self.st17.raise_()
        self.group_saving_preProcessed_data_set.raise_()
        self.group_save_preProcess.raise_()
        self.group_run_preProcess.raise_()
        self.Program_Tabs.addTab(self.tab_preProcessing, "")
        self.tab_data_bank = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_data_bank.sizePolicy().hasHeightForWidth())
        self.tab_data_bank.setSizePolicy(sizePolicy)
        self.tab_data_bank.setObjectName("tab_data_bank")
        self.st20 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st20.setGeometry(QtCore.QRect(120, 228, 391, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st20.setFont(font)
        self.st20.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st20.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st20.setCenterOnScroll(True)
        self.st20.setObjectName("st20")
        self.st18 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st18.setGeometry(QtCore.QRect(30, 86, 251, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st18.setFont(font)
        self.st18.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st18.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st18.setCenterOnScroll(True)
        self.st18.setObjectName("st18")
        self.st19 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st19.setGeometry(QtCore.QRect(120, 166, 391, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st19.setFont(font)
        self.st19.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st19.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st19.setCenterOnScroll(True)
        self.st19.setObjectName("st19")
        self.group_save_data_bank = QtWidgets.QGroupBox(self.tab_data_bank)
        self.group_save_data_bank.setGeometry(QtCore.QRect(560, 160, 180, 41))
        self.group_save_data_bank.setTitle("")
        self.group_save_data_bank.setObjectName("group_save_data_bank")
        self.rbtn_save_data_bank = QtWidgets.QRadioButton(self.group_save_data_bank)
        self.rbtn_save_data_bank.setGeometry(QtCore.QRect(9, 10, 57, 21))
        self.rbtn_save_data_bank.setChecked(True)
        self.rbtn_save_data_bank.setObjectName("rbtn_save_data_bank")
        self.rbtn_dont_save_data_bank = QtWidgets.QRadioButton(self.group_save_data_bank)
        self.rbtn_dont_save_data_bank.setGeometry(QtCore.QRect(110, 10, 61, 21))
        self.rbtn_dont_save_data_bank.setObjectName("rbtn_dont_save_data_bank")
        self.btn_data_bank_methods_ex = QtWidgets.QPushButton(self.tab_data_bank)
        self.btn_data_bank_methods_ex.setGeometry(QtCore.QRect(270, 600, 75, 23))
        self.btn_data_bank_methods_ex.setObjectName("btn_data_bank_methods_ex")
        self.group_run_data_bank = QtWidgets.QGroupBox(self.tab_data_bank)
        self.group_run_data_bank.setGeometry(QtCore.QRect(300, 80, 171, 41))
        self.group_run_data_bank.setTitle("")
        self.group_run_data_bank.setObjectName("group_run_data_bank")
        self.rbtn_run_data_bank = QtWidgets.QRadioButton(self.group_run_data_bank)
        self.rbtn_run_data_bank.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.rbtn_run_data_bank.setChecked(True)
        self.rbtn_run_data_bank.setObjectName("rbtn_run_data_bank")
        self.rbtn_dont_run_data_bank = QtWidgets.QRadioButton(self.group_run_data_bank)
        self.rbtn_dont_run_data_bank.setGeometry(QtCore.QRect(90, 10, 61, 21))
        self.rbtn_dont_run_data_bank.setObjectName("rbtn_dont_run_data_bank")
        self.et_data_bank_methods = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.et_data_bank_methods.setGeometry(QtCore.QRect(540, 441, 321, 391))
        self.et_data_bank_methods.setPlaceholderText("")
        self.et_data_bank_methods.setObjectName("et_data_bank_methods")
        self.st23 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st23.setGeometry(QtCore.QRect(120, 550, 391, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st23.setFont(font)
        self.st23.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st23.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st23.setCenterOnScroll(True)
        self.st23.setObjectName("st23")
        self.st24 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st24.setGeometry(QtCore.QRect(870, 70, 511, 761))
        self.st24.setBackgroundVisible(False)
        self.st24.setPlaceholderText("{1: {         \"module_name\":             \"no_change_char\",         \"class_name\": \"\",         \"method_name\":             \"no_change_char\",         \"special_parameters\":             {\"\"}     }")
        self.st24.setObjectName("st24")
        self.group_saving_data_bank_format = QtWidgets.QGroupBox(self.tab_data_bank)
        self.group_saving_data_bank_format.setGeometry(QtCore.QRect(560, 222, 180, 41))
        self.group_saving_data_bank_format.setTitle("")
        self.group_saving_data_bank_format.setObjectName("group_saving_data_bank_format")
        self.rbtn_saving_data_bank_csv = QtWidgets.QRadioButton(self.group_saving_data_bank_format)
        self.rbtn_saving_data_bank_csv.setGeometry(QtCore.QRect(10, 10, 62, 21))
        self.rbtn_saving_data_bank_csv.setChecked(True)
        self.rbtn_saving_data_bank_csv.setObjectName("rbtn_saving_data_bank_csv")
        self.rbtn_saving_data_bank_mat = QtWidgets.QRadioButton(self.group_saving_data_bank_format)
        self.rbtn_saving_data_bank_mat.setGeometry(QtCore.QRect(110, 10, 71, 21))
        self.rbtn_saving_data_bank_mat.setObjectName("rbtn_saving_data_bank_mat")
        self.st21 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st21.setGeometry(QtCore.QRect(120, 296, 391, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st21.setFont(font)
        self.st21.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st21.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st21.setCenterOnScroll(True)
        self.st21.setObjectName("st21")
        self.group_data_bank_dimensions_in_rows_or_columns = QtWidgets.QGroupBox(self.tab_data_bank)
        self.group_data_bank_dimensions_in_rows_or_columns.setGeometry(QtCore.QRect(560, 290, 180, 41))
        self.group_data_bank_dimensions_in_rows_or_columns.setTitle("")
        self.group_data_bank_dimensions_in_rows_or_columns.setObjectName("group_data_bank_dimensions_in_rows_or_columns")
        self.rbtn_data_bank_dimensions_in_columns = QtWidgets.QRadioButton(self.group_data_bank_dimensions_in_rows_or_columns)
        self.rbtn_data_bank_dimensions_in_columns.setGeometry(QtCore.QRect(10, 10, 95, 21))
        self.rbtn_data_bank_dimensions_in_columns.setChecked(True)
        self.rbtn_data_bank_dimensions_in_columns.setObjectName("rbtn_data_bank_dimensions_in_columns")
        self.rbtn_data_bank_dimensions_in_rows = QtWidgets.QRadioButton(self.group_data_bank_dimensions_in_rows_or_columns)
        self.rbtn_data_bank_dimensions_in_rows.setGeometry(QtCore.QRect(110, 10, 71, 21))
        self.rbtn_data_bank_dimensions_in_rows.setObjectName("rbtn_data_bank_dimensions_in_rows")
        self.st22 = QtWidgets.QPlainTextEdit(self.tab_data_bank)
        self.st22.setGeometry(QtCore.QRect(120, 365, 391, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st22.setFont(font)
        self.st22.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st22.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st22.setCenterOnScroll(True)
        self.st22.setObjectName("st22")
        self.mdiArea_8 = QtWidgets.QMdiArea(self.tab_data_bank)
        self.mdiArea_8.setGeometry(QtCore.QRect(-30, 10, 1441, 941))
        brush = QtGui.QBrush(QtGui.QColor(238, 141, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea_8.setBackground(brush)
        self.mdiArea_8.setObjectName("mdiArea_8")
        self.group_add_dim_headers_to_data_bank = QtWidgets.QGroupBox(self.tab_data_bank)
        self.group_add_dim_headers_to_data_bank.setGeometry(QtCore.QRect(560, 360, 180, 41))
        self.group_add_dim_headers_to_data_bank.setTitle("")
        self.group_add_dim_headers_to_data_bank.setObjectName("group_add_dim_headers_to_data_bank")
        self.rbtn_add_dim_headers = QtWidgets.QRadioButton(self.group_add_dim_headers_to_data_bank)
        self.rbtn_add_dim_headers.setGeometry(QtCore.QRect(10, 10, 72, 20))
        self.rbtn_add_dim_headers.setChecked(True)
        self.rbtn_add_dim_headers.setObjectName("rbtn_add_dim_headers")
        self.rbtn_dont_add_dim_headers = QtWidgets.QRadioButton(self.group_add_dim_headers_to_data_bank)
        self.rbtn_dont_add_dim_headers.setGeometry(QtCore.QRect(110, 10, 71, 20))
        self.rbtn_dont_add_dim_headers.setObjectName("rbtn_dont_add_dim_headers")
        self.mdiArea_8.raise_()
        self.st20.raise_()
        self.st18.raise_()
        self.st19.raise_()
        self.group_save_data_bank.raise_()
        self.btn_data_bank_methods_ex.raise_()
        self.group_run_data_bank.raise_()
        self.et_data_bank_methods.raise_()
        self.st23.raise_()
        self.group_saving_data_bank_format.raise_()
        self.st21.raise_()
        self.group_data_bank_dimensions_in_rows_or_columns.raise_()
        self.st22.raise_()
        self.group_add_dim_headers_to_data_bank.raise_()
        self.st24.raise_()
        self.Program_Tabs.addTab(self.tab_data_bank, "")
        self.tab_postProcessing = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_postProcessing.sizePolicy().hasHeightForWidth())
        self.tab_postProcessing.setSizePolicy(sizePolicy)
        self.tab_postProcessing.setObjectName("tab_postProcessing")
        self.st26 = QtWidgets.QPlainTextEdit(self.tab_postProcessing)
        self.st26.setGeometry(QtCore.QRect(30, 84, 201, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st26.setFont(font)
        self.st26.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st26.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st26.setCenterOnScroll(True)
        self.st26.setObjectName("st26")
        self.btn_postProcess_methods_ex = QtWidgets.QPushButton(self.tab_postProcessing)
        self.btn_postProcess_methods_ex.setGeometry(QtCore.QRect(260, 288, 75, 23))
        self.btn_postProcess_methods_ex.setObjectName("btn_postProcess_methods_ex")
        self.st27 = QtWidgets.QPlainTextEdit(self.tab_postProcessing)
        self.st27.setGeometry(QtCore.QRect(150, 238, 311, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.st27.setFont(font)
        self.st27.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.st27.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.st27.setCenterOnScroll(True)
        self.st27.setObjectName("st27")
        self.group_runPostProcess = QtWidgets.QGroupBox(self.tab_postProcessing)
        self.group_runPostProcess.setGeometry(QtCore.QRect(280, 78, 161, 41))
        self.group_runPostProcess.setTitle("")
        self.group_runPostProcess.setObjectName("group_runPostProcess")
        self.rbtn_run_postProcess = QtWidgets.QRadioButton(self.group_runPostProcess)
        self.rbtn_run_postProcess.setGeometry(QtCore.QRect(15, 10, 61, 21))
        self.rbtn_run_postProcess.setChecked(False)
        self.rbtn_run_postProcess.setObjectName("rbtn_run_postProcess")
        self.rbtn_dont_run_postProcess = QtWidgets.QRadioButton(self.group_runPostProcess)
        self.rbtn_dont_run_postProcess.setGeometry(QtCore.QRect(85, 10, 61, 21))
        self.rbtn_dont_run_postProcess.setChecked(True)
        self.rbtn_dont_run_postProcess.setObjectName("rbtn_dont_run_postProcess")
        self.mdarea_postProcess = QtWidgets.QMdiArea(self.tab_postProcessing)
        self.mdarea_postProcess.setGeometry(QtCore.QRect(10, 20, 1431, 951))
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdarea_postProcess.setBackground(brush)
        self.mdarea_postProcess.setObjectName("mdarea_postProcess")
        self.et_postProcess_methods = QtWidgets.QPlainTextEdit(self.tab_postProcessing)
        self.et_postProcess_methods.setGeometry(QtCore.QRect(470, 29, 391, 761))
        self.et_postProcess_methods.setPlaceholderText("")
        self.et_postProcess_methods.setObjectName("et_postProcess_methods")
        self.st28 = QtWidgets.QPlainTextEdit(self.tab_postProcessing)
        self.st28.setGeometry(QtCore.QRect(870, 28, 511, 761))
        self.st28.setPlaceholderText("{1: {         \"module_name\":             \"no_change_char\",         \"class_name\": \"\",         \"method_name\":             \"no_change_char\",         \"special_parameters\":             {\"\"}     }")
        self.st28.setObjectName("st28")
        self.mdarea_postProcess.raise_()
        self.st26.raise_()
        self.btn_postProcess_methods_ex.raise_()
        self.st27.raise_()
        self.group_runPostProcess.raise_()
        self.et_postProcess_methods.raise_()
        self.st28.raise_()
        self.Program_Tabs.addTab(self.tab_postProcessing, "")
        self.tab_classification = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_classification.sizePolicy().hasHeightForWidth())
        self.tab_classification.setSizePolicy(sizePolicy)
        self.tab_classification.setObjectName("tab_classification")
        self.Program_Tabs.addTab(self.tab_classification, "")
        self.tab_evaluation = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_evaluation.sizePolicy().hasHeightForWidth())
        self.tab_evaluation.setSizePolicy(sizePolicy)
        self.tab_evaluation.setObjectName("tab_evaluation")
        self.Program_Tabs.addTab(self.tab_evaluation, "")
        self.TabsLayout.addWidget(self.Program_Tabs)
        self.verticalLayout.addLayout(self.TabsLayout)
        self.lout_Start_Close = QtWidgets.QHBoxLayout()
        self.lout_Start_Close.setObjectName("lout_Start_Close")
        self.btn_start = QtWidgets.QPushButton(GUIStart)
        self.btn_start.setEnabled(True)
        self.btn_start.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btn_start.setObjectName("btn_start")
        self.lout_Start_Close.addWidget(self.btn_start)
        self.btn_save_as_default = QtWidgets.QPushButton(GUIStart)
        self.btn_save_as_default.setEnabled(True)
        self.btn_save_as_default.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btn_save_as_default.setObjectName("btn_save_as_default")
        self.lout_Start_Close.addWidget(self.btn_save_as_default)
        self.btn_close = QtWidgets.QPushButton(GUIStart)
        self.btn_close.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btn_close.setObjectName("btn_close")
        self.lout_Start_Close.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.lout_Start_Close)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(GUIStart)
        self.Program_Tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GUIStart)

    def retranslateUi(self, GUIStart):
        _translate = QtCore.QCoreApplication.translate
        GUIStart.setWindowTitle(_translate("GUIStart", "GUIStarter"))
        self.et_project_name.setPlainText(_translate("GUIStart", "Proj_PyVersion"))
        self.st0.setPlainText(_translate("GUIStart", "Project Name:"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_general), _translate("GUIStart", "General"))
        self.data_set_address_groupBox.setTitle(_translate("GUIStart", "Dat Set Adress:"))
        self.rbtn_data_set_name.setText(_translate("GUIStart", "Data-Set Name:"))
        self.rbtn_data_set_address.setText(_translate("GUIStart", "Dat-Set Address:"))
        self.st1.setPlainText(_translate("GUIStart", "Zero Conversion Threshold:"))
        self.et_zero_conversion_threshold.setPlainText(_translate("GUIStart", "0.7"))
        self.et_No_sR.setPlainText(_translate("GUIStart", "32"))
        self.st2.setPlainText(_translate("GUIStart", "Number of sub-Regions:"))
        self.et_No_chips_in_sR.setPlainText(_translate("GUIStart", "4"))
        self.et_No_Symbols_preamb.setPlainText(_translate("GUIStart", "8"))
        self.st4.setPlainText(_translate("GUIStart", "Number of Chips/sub-Region:"))
        self.st3.setPlainText(_translate("GUIStart", "Number of Symbls/preamble:"))
        self.et_sampling_frequency.setPlainText(_translate("GUIStart", "20e6"))
        self.et_chip_length.setPlainText(_translate("GUIStart", "1e-6"))
        self.st7.setPlainText(_translate("GUIStart", "Communication Frequency (Hz):"))
        self.st6.setPlainText(_translate("GUIStart", "Sampling Frequency (Hz):"))
        self.st5.setPlainText(_translate("GUIStart", "Length of Chip (Sec.):"))
        self.et_communication_frequency.setPlainText(_translate("GUIStart", "2e6"))
        self.st12.setPlainText(_translate("GUIStart", "Characteristic Extractor Methods:"))
        self.st8.setPlainText(_translate("GUIStart", "Save the Data-Set:"))
        self.rbtn_save_data_set.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_save_data_set.setText(_translate("GUIStart", "No"))
        self.st9.setPlainText(_translate("GUIStart", "Data-Set Saving Format:"))
        self.st10.setPlainText(_translate("GUIStart", "Data-Set Loading Format:"))
        self.et_data_set_extractor_methods.setPlainText(_translate("GUIStart", "{    \n"
"    1: {\n"
"                     \"module_name\": \"amplitude_calculator\",\n"
"                     \"class_name\": \"\",\n"
"                     \"method_name\":\"amp\",\n"
"                     \"special_parameters\":{\"\"}\n"
"                     },\n"
"\n"
"                2: {\n"
"                      \"module_name\": \"phase_calculator\",\n"
"                      \"class_name\": \"\",\n"
"                       \"method_name\": \"phase\",\n"
"                       \"special_parameters\": {\"\"}\n"
"                     },\n"
"\n"
"                 3: {\n"
"                        \"module_name\": \"ifrequency_calculator\",\n"
"                        \"class_name\": \"\",\n"
"                        \"method_name\": \"ifreq\",\n"
"                        \"special_parameters\": {\"\"}\n"
"                     },\n"
"\n"
"} "))
        self.btn_dat_set_extractor_method_ex.setText(_translate("GUIStart", "Ex."))
        self.et_data_set_name.setHtml(_translate("GUIStart", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_brows_data_set.setText(_translate("GUIStart", "Browse"))
        self.st11.setPlainText(_translate("GUIStart", "{\n"
"     priority-index : {\n"
"                                     \"module_name\":\n"
"                                               \"name of module\",\n"
"\n"
"                                      \"class_name\": \n"
"                                                  \"name of class\",\n"
"\n"
"                                      \"method_name\": \n"
"                                                   \"name of method\",\n"
"\n"
"                                       \"special_parameters\":\n"
"                                                    {\"parameter-1\": parameter_1,\n"
"                                                      \"parameter-2\": parameter_2, \n"
"                                                    ...}\n"
"                                }, \n"
"\n"
" ...  }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"for ex.:\n"
"{    \n"
"    1: {\n"
"                     \"module_name\": \"amplitude_calculator\",\n"
"                     \"class_name\": \"\",\n"
"                     \"method_name\":\"amp\",\n"
"                     \"special_parameters\":{\"\"}\n"
"                     },\n"
"\n"
"                2: {\n"
"                      \"module_name\": \"phase_calculator\",\n"
"                      \"class_name\": \"\",\n"
"                       \"method_name\": \"phase\",\n"
"                       \"special_parameters\": {\"\"}\n"
"                     },\n"
"\n"
"                 3: {\n"
"                        \"module_name\": \"ifrequency_calculator\",\n"
"                        \"class_name\": \"\",\n"
"                        \"method_name\": \"ifreq\",\n"
"                        \"special_parameters\": {\"\"}\n"
"                     },\n"
"\n"
"    4:{}\n"
"\n"
"} "))
        self.rbtn_data_set_saving_format_txt.setText(_translate("GUIStart", ".TXT"))
        self.rbtn_data_set_loading_format_txt.setText(_translate("GUIStart", ".TXT"))
        self.rbtn_load_new_data_set.setText(_translate("GUIStart", "Load Current Data-Set"))
        self.rbtn_make_new_data_set.setText(_translate("GUIStart", "Make New Data-Set"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_data_set), _translate("GUIStart", "DataSet"))
        self.st13.setPlainText(_translate("GUIStart", "Run pre-Processing:"))
        self.st15.setPlainText(_translate("GUIStart", "pre-Processed Data-Set Saving Format:"))
        self.st14.setPlainText(_translate("GUIStart", "Save the pre-Processed Data-Set:"))
        self.st16.setPlainText(_translate("GUIStart", "selected pre-Processing Methods:"))
        self.btn_preProcess_methods_ex.setText(_translate("GUIStart", "Ex."))
        self.et_preProcessed_methods.setPlainText(_translate("GUIStart", "{\n"
"  1 : {\n"
"          \"module_name\": \"dwt_calculator\",\n"
"          \"class_name\": \"\",\n"
"          \"method_name\": \"dwt_calculator\",\n"
"          \"special_parameters\":{\"important_element\":\"details\"}\n"
"         }\n"
"}"))
        self.st17.setPlainText(_translate("GUIStart", "{\n"
"     priority-index : {\n"
"                                     \"module_name\":\n"
"                                               \"name of module\",\n"
"\n"
"                                      \"class_name\": \n"
"                                                  \"name of class\",\n"
"\n"
"                                      \"method_name\": \n"
"                                                   \"name of method\",\n"
"\n"
"                                       \"special_parameters\":\n"
"                                                    {\"parameter-1\": parameter_1,\n"
"                                                      \"parameter-2\": parameter_2, \n"
"                                                    ...}\n"
"                                }, \n"
"\n"
" ...  }# these functions are executed in order of priority-index\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"for ex.:\n"
"{\n"
"                        1 : {\n"
"                                     \"module_name\": \"wavelet_module_name\",\n"
"                                      \"class_name\": \"wavelet_class_name\",\n"
"                                      \"method_name\": \"wavelet_method_name\",\n"
"                                       \"special_parameters\":{\"important_element\":\"details\"} # or: \"approximations\"\n"
"                                },\n"
"\n"
"\n"
"                        2 : {\n"
"                                     \"module_name\":\"fourier_module_name\",\n"
"                                      \"class_name\":\"fourier_class_name\",\n"
"                                      \"method_name\":\"fourier_method_name\",\n"
"                                       \"special_parameters\":\n"
"                                                    {\"first_factor\": 2,\n"
"                                                      \"output_name\": \"ft}\n"
"                                }\n"
"\n"
"\n"
"   }"))
        self.rbtn_saving_preProcessed_data_set_txt.setText(_translate("GUIStart", ".TXT"))
        self.rbtn_save_preProcessed_data_set.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_save_preProcessed_data_set.setText(_translate("GUIStart", "No"))
        self.rbtn_run_preProcess.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_run_preProcess.setText(_translate("GUIStart", "No"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_preProcessing), _translate("GUIStart", "preProcessing"))
        self.st20.setPlainText(_translate("GUIStart", "Data-Bank Saving Format:"))
        self.st18.setPlainText(_translate("GUIStart", "Run Data-Bank Production:"))
        self.st19.setPlainText(_translate("GUIStart", "Save the Data-Bank:"))
        self.rbtn_save_data_bank.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_save_data_bank.setText(_translate("GUIStart", "No"))
        self.btn_data_bank_methods_ex.setText(_translate("GUIStart", "Ex."))
        self.rbtn_run_data_bank.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_run_data_bank.setText(_translate("GUIStart", "No"))
        self.et_data_bank_methods.setPlainText(_translate("GUIStart", "{\n"
"\n"
"  1:\n"
"          {\n"
"            \"module_name\": \"variance\",\n"
"            \"class_name\": \"\",\n"
"            \"method_name\": \"variance\",\n"
"            \"special_parameters\": {}\n"
"           },\n"
"  2:\n"
"          {\n"
"            \"module_name\": \"skewness\",\n"
"            \"class_name\": \"\",\n"
"            \"method_name\": \"skewness\",\n"
"            \"special_parameters\": {}\n"
"           },\n"
"  3:\n"
"           {\n"
"             \"module_name\": \"kurtosis\",\n"
"             \"class_name\": \"\",\n"
"             \"method_name\": \"kurt\",\n"
"             \"special_parameters\": {}\n"
"            }\n"
"\n"
"}  \n"
""))
        self.st23.setPlainText(_translate("GUIStart", "selected Data-Bsnk Poduction Methods:"))
        self.st24.setPlainText(_translate("GUIStart", "{\n"
"     priority-index : {\n"
"                                     \"module_name\":\n"
"                                               \"name of module\",\n"
"\n"
"                                      \"class_name\": \n"
"                                                  \"name of class\",\n"
"\n"
"                                      \"method_name\": \n"
"                                                   \"name of method\",\n"
"\n"
"                                       \"special_parameters\":\n"
"                                                    {\"parameter-1\": parameter_1,\n"
"                                                      \"parameter-2\": parameter_2, \n"
"                                                    ...}\n"
"                                }, \n"
"\n"
" ...  }# these functions are executed in order of priority-index\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"for ex.:\n"
"{\n"
"                       1:\n"
"                  {\n"
"                      \"module_name\": \"variance\",\n"
"                      \"class_name\": \"\",\n"
"                      \"method_name\": \"variance\",\n"
"                      \"special_parameters\": {}\n"
"                   },\n"
"             2:\n"
"                  {\n"
"                      \"module_name\": \"skewness\",\n"
"                      \"class_name\": \"\",\n"
"                      \"method_name\": \"skewness\",\n"
"                      \"special_parameters\": {}\n"
"                   },\n"
"                       3:\n"
"                   {\n"
"                       \"module_name\": \"kurtosis\",\n"
"                        \"class_name\": \"\",\n"
"                       \"method_name\": \"kurt\",\n"
"                         \"special_parameters\": {}\n"
"                                 }\n"
"\n"
"\n"
"   }\n"
"\n"
"\n"
"or:\n"
"\n"
"\n"
"{\n"
"                       1:\n"
"                  {\n"
"                      \"module_name\": \"no_change_FP\",\n"
"                                  \"class_name\": \"\", \"method_name\": \"no_change_FP\",\n"
"                                  \"special_parameters\": {}\n"
"                                 }\n"
"}  # these functions are executed in order of\n"
""))
        self.rbtn_saving_data_bank_csv.setText(_translate("GUIStart", ".CSV"))
        self.rbtn_saving_data_bank_mat.setText(_translate("GUIStart", ".MAT"))
        self.st21.setPlainText(_translate("GUIStart", "Data-Bank Dimensions in Columns or Rows:"))
        self.rbtn_data_bank_dimensions_in_columns.setText(_translate("GUIStart", "Columns"))
        self.rbtn_data_bank_dimensions_in_rows.setText(_translate("GUIStart", "Rows"))
        self.st22.setPlainText(_translate("GUIStart", "Add Dimension Headers to Saving Data-Bank:"))
        self.rbtn_add_dim_headers.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_add_dim_headers.setText(_translate("GUIStart", "No"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_data_bank), _translate("GUIStart", "DataBank"))
        self.st26.setPlainText(_translate("GUIStart", "Run post-Processing:"))
        self.btn_postProcess_methods_ex.setText(_translate("GUIStart", "Ex."))
        self.st27.setPlainText(_translate("GUIStart", "selected post-Processing Methods:"))
        self.rbtn_run_postProcess.setText(_translate("GUIStart", "Yes"))
        self.rbtn_dont_run_postProcess.setText(_translate("GUIStart", "No"))
        self.et_postProcess_methods.setPlainText(_translate("GUIStart", "{\n"
"\n"
"1:\n"
"        {\n"
"            \"module_name\": \"normalizer\",\n"
"            \"class_name\": \"\",\n"
"            \"method_name\": \"normalizer\",\n"
"            \"special_parameters\": {}\n"
"        },\n"
" 2:\n"
"        {\n"
"            \"module_name\": \"standardizer\",\n"
"            \"class_name\": \"\",\n"
"            \"method_name\": \"standardizer\",\n"
"            \"special_parameters\": {}\n"
"         },\n"
"\n"
"}  "))
        self.st28.setPlainText(_translate("GUIStart", "{\n"
"     priority-index : {\n"
"                                     \"module_name\":\n"
"                                               \"name of module\",\n"
"\n"
"                                      \"class_name\": \n"
"                                                  \"name of class\",\n"
"\n"
"                                      \"method_name\": \n"
"                                                   \"name of method\",\n"
"\n"
"                                       \"special_parameters\":\n"
"                                                    {\"parameter-1\": parameter_1,\n"
"                                                      \"parameter-2\": parameter_2, \n"
"                                                    ...}\n"
"                                }, \n"
"\n"
" ...  }# these functions are executed in order of priority-index\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"for ex.:\n"
"{\n"
"\n"
"                        1 : {\n"
"                                     \"module_name\":  \"normalizer\",\n"
"                                      \"class_name\": \"\",\n"
"                                      \"method_name\": \"normalizer\",\n"
"                                       \"special_parameters\":{}\n"
"                                },\n"
"\n"
"                        2 : {\n"
"                                     \"module_name\":  \"standardizer\",\n"
"                                      \"class_name\": \"\",\n"
"                                      \"method_name\": \"standardizer\",\n"
"                                       \"special_parameters\":{}\n"
"                                }\n"
"\n"
"\n"
"   }"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_postProcessing), _translate("GUIStart", "postProcessing"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_classification), _translate("GUIStart", "Classification"))
        self.Program_Tabs.setTabText(self.Program_Tabs.indexOf(self.tab_evaluation), _translate("GUIStart", "Evaluation"))
        self.btn_start.setText(_translate("GUIStart", "Start"))
        self.btn_save_as_default.setText(_translate("GUIStart", "Save as Default"))
        self.btn_close.setText(_translate("GUIStart", "Close"))


        self.et_data_set_address.setEnabled(False)

        # assigning Event Handlers
        # 1. General
        self.btn_start.clicked.connect(self.start_clicked)
        self.btn_close.clicked.connect(self.close_clicked)
        self.btn_save_as_default.clicked.connect(self.save_as_default)

        # 2. Data-Set
        self.rbtn_make_new_data_set.toggled.connect(self.making_data_set_selected)
        self.making_data_set_selected(True)
        self.btn_brows_data_set.clicked.connect(self.brows_data_set)
        self.rbtn_data_set_name.toggled.connect(self.data_set_name_selected)

        # 3. preProcessed Data-Set
        self.btn_preProcess_methods_ex.clicked.connect(self.preProcess_ex)

        # 4. Data-Bank
        self.btn_data_bank_methods_ex.clicked.connect(self.data_bank_ex)

        # 5. postProcessed Data-Set
        self.btn_postProcess_methods_ex.clicked.connect(self.postProcess_ex)

        # 6. Lading default
        self.load_default()

    def configuration_folder_address_extractor(self):
        root_folder_address = root_project_folder_address_extractor(
            target_folder_name=self.et_project_name.toPlainText())

        parent_folder_address = root_folder_address + "\\Start\\PythonGUI"
        parent_folder_address = parent_folder_address.replace("\\", "/")

        return parent_folder_address

    def load_default(self):
        parent_folder_address = self.configuration_folder_address_extractor()
        configuration_file_address = ("%s/configuration.txt" % parent_folder_address)

        if os.path.exists(configuration_file_address):
            loaded_configuration = ast.literal_eval(pickle_file_loader(configuration_file_address))

            # 1. General
            self.et_project_name.setPlainText(loaded_configuration["project_name"])

            # 2. Data-Set
            if loaded_configuration["rbtn_data_set_name"]:

                if not self.rbtn_data_set_name.isChecked():
                    self.rbtn_data_set_name.click()
                self.data_set_name_selected(True)
                self.et_data_set_name.setText(loaded_configuration["data_set_name"])
                self.et_data_set_address.setPlainText("")

            else:
                if not self.rbtn_data_set_address.isChecked():
                    self.rbtn_data_set_address.click()
                self.data_set_name_selected(False)
                self.et_data_set_address.setText(loaded_configuration["data_set_address"])
                self.et_data_set_name.setPlainText("")

            if loaded_configuration["make_new_data_set"]:
                if not self.rbtn_make_new_data_set.isChecked():
                    self.rbtn_make_new_data_set.click()
                self.making_data_set_selected(True)

            elif not loaded_configuration["make_new_data_set"]:
                if not self.rbtn_load_new_data_set.isChecked():
                    self.rbtn_load_new_data_set.click()
                self.making_data_set_selected(False)

            self.et_zero_conversion_threshold.setPlainText(loaded_configuration["zero_conversion_threshold"])
            self.et_No_sR.setPlainText(loaded_configuration["number_of_subRegions"])
            self.et_No_Symbols_preamb.setPlainText(loaded_configuration["number_of_symbols_per_subRegion"])
            self.et_No_chips_in_sR.setPlainText(loaded_configuration["number_of_chips_per_subRegion"])
            self.et_chip_length.setPlainText(loaded_configuration["time_length_of_chip"])
            self.et_sampling_frequency.setPlainText(loaded_configuration["sampling_frequency"])
            self.et_communication_frequency.setPlainText(loaded_configuration["communication_frequency"])

            if (loaded_configuration["save_data_set"]) and (not self.rbtn_save_data_set.isChecked()):
                self.rbtn_save_data_set.setChecked(True)

            elif (not loaded_configuration["save_data_set"]) and (not self.rbtn_dont_save_data_set.isChecked()):
                self.rbtn_dont_save_data_set.setChecked(True)

            if (loaded_configuration["data_set_saving_format"] == "txt") and (
            not self.rbtn_data_set_saving_format_txt.isChecked()):
                self.rbtn_data_set_saving_format_txt.setChecked(True)

            elif (loaded_configuration["data_set_saving_format"] != "txt") and (
            self.rbtn_data_set_saving_format_txt.isChecked()):
                self.rbtn_data_set_saving_format_txt.setChecked(False)

            self.et_data_set_extractor_methods.setPlainText(loaded_configuration["data_set_extractor_methods"])

            if loaded_configuration["data_set_loading_format"] == "txt" and (
            not self.rbtn_data_set_loading_format_txt.isChecked()):
                self.rbtn_data_set_loading_format_txt.click()

            elif (loaded_configuration["data_set_loading_format"] != "txt") and (
            self.rbtn_data_set_loading_format_txt.isChecked()):
                self.rbtn_data_set_loading_format_txt.click()

            # 3. preProcessed Data-Set
            if (loaded_configuration["run_preProcess"]) and (not self.rbtn_run_preProcess.isChecked()):
                self.rbtn_run_preProcess.click()

            elif (not loaded_configuration["run_preProcess"]) and (not self.rbtn_dont_run_preProcess.isChecked()):
                self.rbtn_dont_run_preProcess.click()

            if (loaded_configuration["save_preProcessed_data_set"]) and (
            not self.rbtn_save_preProcessed_data_set.isChecked()):
                self.rbtn_save_preProcessed_data_set.click()

            elif (not loaded_configuration["save_preProcessed_data_set"]) and (
            not self.rbtn_dont_save_preProcessed_data_set.isChecked()):
                self.rbtn_dont_save_preProcessed_data_set.click()

            if loaded_configuration["preProcessed_data_set_saving_format"] == "txt" and (
            not self.rbtn_saving_preProcessed_data_set_txt.isChecked()):
                self.rbtn_saving_preProcessed_data_set_txt.click()

            elif (loaded_configuration["preProcessed_data_set_saving_format"] != "txt") and (
            self.rbtn_saving_preProcessed_data_set_txt.isChecked()):
                self.rbtn_saving_preProcessed_data_set_txt.click()

            self.et_preProcessed_methods.setPlainText(loaded_configuration["preProcessing_methods"])

            # 4. Data-Bank
            if (loaded_configuration["run_data_bank"]) and (not self.rbtn_run_data_bank.isChecked()):
                self.rbtn_run_data_bank.click()

            elif (not loaded_configuration["run_data_bank"]) and (not self.rbtn_dont_run_data_bank.isChecked()):
                self.rbtn_dont_run_data_bank.click()

            if (loaded_configuration["save_data_bank"]) and (not self.rbtn_save_data_bank.isChecked()):
                self.rbtn_save_data_bank.click()

            elif (not loaded_configuration["save_data_bank"]) and (not self.rbtn_dont_save_data_bank.isChecked()):
                self.rbtn_dont_save_data_bank.click()

            if (loaded_configuration["data_bank_saving_format"] == "csv") and (
            not self.rbtn_saving_data_bank_csv.isChecked()):
                self.rbtn_saving_data_bank_csv.click()

            elif (loaded_configuration["data_bank_saving_format"] == "mat") and (
            not self.rbtn_saving_data_bank_mat.isChecked()):
                self.rbtn_saving_data_bank_mat.click()

            if loaded_configuration["data_bank_dimensions_in_columns"] == "columns" and (
            not self.rbtn_data_bank_dimensions_in_columns.isChecked()):
                self.rbtn_data_bank_dimensions_in_columns.click()

            elif loaded_configuration["data_bank_dimensions_in_columns"] == "rows" and (
            not self.rbtn_data_bank_dimensions_in_rows.isChecked()):
                self.rbtn_data_bank_dimensions_in_rows.click()

            if loaded_configuration["add_dim_headers"] and (not self.rbtn_add_dim_headers.isChecked()):
                self.rbtn_add_dim_headers.click()

            elif (not loaded_configuration["add_dim_headers"]) and (not self.rbtn_dont_add_dim_headers.isChecked()):
                self.rbtn_dont_add_dim_headers.click()

            self.et_data_bank_methods.setPlainText(loaded_configuration["data_bank_methods"])

            # 5. postProcessed Data-Set
            if (loaded_configuration["run_postProcess"]) and (not self.rbtn_run_postProcess.isChecked()):
                self.rbtn_run_postProcess.click()

            elif (not loaded_configuration["run_postProcess"]) and (not self.rbtn_dont_run_postProcess.isChecked()):
                self.rbtn_dont_run_postProcess.click()

            self.et_postProcess_methods.setPlainText(loaded_configuration["postProcessing_methods"])

    def save_as_default(self):
        saved_parameters = str(self.parameter_collector("save_as_default"))

        parent_folder_address = self.configuration_folder_address_extractor()

        pickle_file_saver(saved_parameters, parent_folder_address, "configuration", [])

    def making_data_set_selected(self, enabled):
        if not enabled:
            self.et_zero_conversion_threshold.setDisabled(True)
            self.et_No_sR.setDisabled(True)
            self.et_No_Symbols_preamb.setDisabled(True)
            self.et_No_chips_in_sR.setDisabled(True)
            self.et_chip_length.setDisabled(True)
            self.et_sampling_frequency.setDisabled(True)
            self.et_communication_frequency.setDisabled(True)

            self.rbtn_save_data_set.setEnabled(False)
            self.rbtn_dont_save_data_set.setEnabled(False)

            self.rbtn_data_set_saving_format_txt.setEnabled(False)

            self.et_data_set_extractor_methods.setDisabled(True)

            self.rbtn_data_set_loading_format_txt.setEnabled(True)

        else:
            self.et_zero_conversion_threshold.setDisabled(False)
            self.et_No_sR.setDisabled(False)
            self.et_No_Symbols_preamb.setDisabled(False)
            self.et_No_chips_in_sR.setDisabled(False)
            self.et_chip_length.setDisabled(False)
            self.et_sampling_frequency.setDisabled(False)
            self.et_communication_frequency.setDisabled(False)

            self.rbtn_save_data_set.setEnabled(True)
            self.rbtn_dont_save_data_set.setEnabled(True)

            self.rbtn_data_set_saving_format_txt.setEnabled(True)

            self.et_data_set_extractor_methods.setDisabled(False)

            self.rbtn_data_set_loading_format_txt.setEnabled(False)

    def data_set_name_selected(self, enabled):
        if not enabled:
            self.et_data_set_name.setDisabled(True)
            self.et_data_set_address.setDisabled(False)

            if self.et_data_set_name.toPlainText() == "A Data-Set Name Should be Assigned!":
                self.et_data_set_name.setText("")

        else:
            self.et_data_set_address.setDisabled(True)
            self.et_data_set_name.setDisabled(False)

            if (self.et_data_set_address.toPlainText() == "A Data-Set Address Should be Assigned!") or \
                    ("There is no Folder Named RawData in:" in self.et_data_set_address.toPlainText()):
                self.et_data_set_address.setText("")

    def start_clicked(self):
        # Collecting Variables
        self.parameter_collection = self.parameter_collector("start_clicked")

        if self.start_allowed():
            start = timeit.default_timer()
            outpurt = main_GUI(self.parameter_collection)
            stop = timeit.default_timer()

            print (stop - start)
            # print(outpurt.keys())

    def close_clicked(self):
        sys.exit(0)

    def brows_data_set(self):
        if self.rbtn_data_set_address.isChecked():

            root_folder_address = root_project_folder_address_extractor(
                target_folder_name=self.et_project_name.toPlainText())
            root = Tk()
            root.withdraw()  # use to hide tkinter window
            parent_folder_address = filedialog.askdirectory(parent=root, initialdir=root_folder_address,
                                                            title='Please select a Recorded Data Collection')

            data_set_address = parent_folder_address + "\\RawData"
            data_set_address = data_set_address.replace("\\", "/")
            self.et_data_set_address.setText(data_set_address)
            self.et_data_set_address.setStyleSheet("QTextEdit {color:black}")
            if not os.path.exists(data_set_address):
                error_text = ('There is no Folder Named RawData in: %s' % parent_folder_address)
                self.et_data_set_address.setText(error_text)
                self.et_data_set_address.setStyleSheet("QTextEdit {color:red}")
                # raise ValueError(error_text)

    def preProcess_ex(self):
        # TODO: Complete this function
        pass

    def data_bank_ex(self):
        # TODO: Complete this function
        pass

    def postProcess_ex(self):
        # TODO: Complete this function
        pass

    def parameter_collector(self, caller_function):
        self.parameter_collection = {}

        # 1. General
        self.parameter_collection["project_name"] = self.et_project_name.toPlainText()

        # 2. Data-Set
        self.parameter_collection["data_set_name"] = self.et_data_set_name.toPlainText()
        self.parameter_collection["data_set_address"] = self.et_data_set_address.toPlainText()

        self.parameter_collection["rbtn_data_set_name"] = self.rbtn_data_set_name.isChecked()  # Just for SaveAsDefault

        self.parameter_collection["zero_conversion_threshold"] = self.et_zero_conversion_threshold.toPlainText()
        self.parameter_collection["number_of_subRegions"] = self.et_No_sR.toPlainText()
        self.parameter_collection["number_of_symbols_per_subRegion"] = self.et_No_Symbols_preamb.toPlainText()
        self.parameter_collection["number_of_chips_per_subRegion"] = self.et_No_chips_in_sR.toPlainText()
        self.parameter_collection["time_length_of_chip"] = self.et_chip_length.toPlainText()
        self.parameter_collection["sampling_frequency"] = self.et_sampling_frequency.toPlainText()
        self.parameter_collection["communication_frequency"] = self.et_communication_frequency.toPlainText()

        if self.rbtn_data_set_saving_format_txt.isChecked():
            self.parameter_collection["data_set_saving_format"] = "txt"

        else:
            self.parameter_collection["data_set_saving_format"] = ""

        if self.rbtn_data_set_loading_format_txt.isChecked():
            self.parameter_collection["data_set_loading_format"] = "txt"

        else:
            self.parameter_collection["data_set_loading_format"] = ""

        self.parameter_collection["data_set_extractor_methods"] = self.et_data_set_extractor_methods.toPlainText()

        self.parameter_collection["save_data_set"] = self.rbtn_save_data_set.isChecked()
        self.parameter_collection["make_new_data_set"] = self.rbtn_make_new_data_set.isChecked()

        if self.rbtn_data_set_address.isChecked():
            self.parameter_collection["data_set_address"] = self.et_data_set_address.toPlainText()

        else:

            if caller_function == "start_clicked":
                if self.et_data_set_name.toPlainText():
                    root_folder_address = root_project_folder_address_extractor(
                        target_folder_name=self.parameter_collection["project_name"])
                    parent_folder_address = root_folder_address + "\\Resources\\" + self.et_data_set_name.toPlainText()
                    data_set_address = parent_folder_address + "\\RawData"
                    data_set_address = data_set_address.replace("\\", "/")
                    self.parameter_collection["data_set_address"] = data_set_address

                else:
                    self.et_data_set_name.setText("A Data-Set Name Should be Assigned!")
                    self.parameter_collection["data_set_address"] = ""

            elif caller_function == "save_as_default":
                self.parameter_collection["data_set_address"] = self.et_data_set_name.toPlainText()

        # 3. preProcessed Data-Set
        self.parameter_collection["run_preProcess"] = self.rbtn_run_preProcess.isChecked()
        self.parameter_collection["save_preProcessed_data_set"] = self.rbtn_save_preProcessed_data_set.isChecked()

        if self.rbtn_saving_preProcessed_data_set_txt.isChecked():
            self.parameter_collection["preProcessed_data_set_saving_format"] = "txt"
        else:
            self.parameter_collection["preProcessed_data_set_saving_format"] = ""

        self.parameter_collection["preProcessing_methods"] = self.et_preProcessed_methods.toPlainText()

        # 4. Data-Bank
        self.parameter_collection["run_data_bank"] = self.rbtn_run_data_bank.isChecked()
        self.parameter_collection["save_data_bank"] = self.rbtn_save_data_bank.isChecked()

        if self.rbtn_saving_data_bank_csv.isChecked():
            self.parameter_collection["data_bank_saving_format"] = "csv"

        elif self.rbtn_saving_data_bank_mat.isChecked():
            self.parameter_collection["data_bank_saving_format"] = "mat"

        if self.rbtn_data_bank_dimensions_in_columns.isChecked():
            self.parameter_collection["data_bank_dimensions_in_columns"] = "columns"

        else:
            self.parameter_collection["data_bank_dimensions_in_columns"] = "rows"

        self.parameter_collection["add_dim_headers"] = self.rbtn_add_dim_headers.isChecked()
        self.parameter_collection["data_bank_methods"] = self.et_data_bank_methods.toPlainText()

        # 5. postProcessed Data-Set
        self.parameter_collection["run_postProcess"] = self.rbtn_run_postProcess.isChecked()
        self.parameter_collection["postProcessing_methods"] = self.et_postProcess_methods.toPlainText()

        return self.parameter_collection

    def start_allowed(self):
        start_is_allowed = True
        if (not self.parameter_collection["data_set_address"]) or \
                (self.parameter_collection["data_set_address"] == "A Data-Set Address Should be Assigned!") or \
                (self.et_data_set_name.toPlainText() == "A Data-Set Name Should be Assigned!") or \
                ("There is no Folder Named RawData in:" in self.et_data_set_address.toPlainText()):

            if self.rbtn_data_set_name.isChecked():
                self.et_data_set_name.setText("A Data-Set Name Should be Assigned!")
                self.et_data_set_name.setStyleSheet("QTextEdit {color:red}")

            else:
                self.et_data_set_address.setText("A Data-Set Address Should be Assigned!")
                self.et_data_set_address.setStyleSheet("QTextEdit {color:red}")

            start_is_allowed = False

        elif self.et_data_set_address.toPlainText() == "A Data-Set Address Should be Assigned!":
            self.et_data_set_address.setText("")

        return start_is_allowed

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUIStart = QtWidgets.QWidget()
    ui = Ui_GUIStart()
    ui.setupUi(GUIStart)

    GUIStart.showMaximized()
    sys.exit(app.exec_())

