# -*- coding: utf-8 -*-

# Snow cover area assessment tool using Python 
#
# Created: Fri Apr 25  2014
# Authors: Antara / Prasun (@pkg_sd)
# 
# Published under GPLv3

from PySide import QtCore, QtGui
import gdal
import numpy
import pylab as plt
import glob


class Ui_Dialog(object):
    folder = ''
    files = []
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 371)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 381, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        ###keedda####
        self.pushButton1 = QtGui.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(220, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")

        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(540, 40, 241, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("""background color=rgb(255, 255, 255)""")
        self.label_2.setObjectName("label_2")
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(510, 90, 20, 201))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 70, 731, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(9, 19, 771, 331))
        self.frame.setStyleSheet("bgcolor=rgb(255, 255, 255)")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.browse)
        QtCore.QObject.connect(self.pushButton1,QtCore.SIGNAL("clicked()"),self.run)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton1.setText(QtGui.QApplication.translate("Dialog", "RUN", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "    Snow Cover Assesment Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Calculates the snow cover area\n"
            "using MODIS Terra datasets\n"
            "and plots a graph of the change.\n"
            "Requires an input folder of all\n"
            "the MODIS .HDF files to be\n"
            "analysed, arranged sequentially.", None, QtGui.QApplication.UnicodeUTF8))

    @QtCore.Slot()
    def browse(self):
        print 'selecting folder containing modis data'
        self.folder=str(QtGui.QFileDialog.getExistingDirectory())
        self.folder.replace('\\','/')
        self.lineEdit.setText(self.folder)
        
    @QtCore.Slot()
    def run(self):
        print 'running the code'
        self.files=glob.glob(self.folder+'/*.tif')
        print 'Number of files found in %s = %d' %(self.folder, len(self.files))
        areas=[]
        years=[]
        for eachfile in self.files:
            print eachfile,' - ',
            f=gdal.Open(eachfile)
            data=f.ReadAsArray()
            threshold_data=numpy.where(data==200)
            areas.append(len(threshold_data[0])*(0.25))
            years.append(eachfile[-36:-32])
        plt.plot(years, areas)
        plt.ylabel('Snow Cover Area in sq. km')
        plt.xlabel('Years')   
        plt.show()                        

if __name__ == "__main__":
    import sys
    try:
          app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        app = QtCore.QCoreApplication.instance()
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

