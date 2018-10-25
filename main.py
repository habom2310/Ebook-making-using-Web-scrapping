#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QMainWindow, QMessageBox, QAction, QLineEdit, QPushButton, QFileDialog, QPlainTextEdit
import threading
import time
import glob
import os
import zipfile
import shutil


from scrapper import Scrapper


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.chap = 0
        self.progress = 0
        
    def initUI(self):               
        
        #label
        self.label_tentruyen = QLabel("link", self)
        self.label_tentruyen.move(40,40)
        
        self.label_savefolder= QLabel("save folder", self)
        self.label_savefolder.move(40,70)
        
        #textbox
        self.textbox_tentruyen = QLineEdit(self)
        self.textbox_tentruyen.move(100, 45)
        self.textbox_tentruyen.resize(280,20)
        
        self.textbox_saveFolder = QLineEdit(self)
        self.textbox_saveFolder.move(100, 75)
        self.textbox_saveFolder.resize(280,20)
        
        #button
        self.button_selectSaveFolder = QPushButton("...",self)
        self.button_selectSaveFolder.setGeometry(400,75,40,20)
        self.button_selectSaveFolder.clicked.connect(self.openFolderDialog)
        
        
        self.button_start = QPushButton("Start", self)
        self.button_start.setGeometry(100, 120, 40, 40)
        self.button_start.clicked.connect(self.thread)
        
        # self.plainTextBox = QPlainTextEdit(self)
        # self.plainTextBox.move(100, 180)
        # self.plainTextBox.resize(360,200)
        # self.plainTextBox.setDisabled(True)
        
        self.label_status = QLabel("Progress: ", self)
        self.label_status.move(40,250)
        
        self.statusBar()

        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)
        
        self.setGeometry(300, 200, 500, 350)
        self.setWindowTitle('Ebook maker')
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure wish to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
            self.t._stop()
            self.t2.cancel()
        else:
            event.ignore()   
            
    def openFolderDialog(self):
        self.folder = QFileDialog.getExistingDirectory(None, 'Choose directory to save', './', QFileDialog.ShowDirsOnly)
        self.textbox_saveFolder.setText(self.folder)
    
    def thread(self):
        self.t = threading.Thread(target=self.run)
        self.t.start()
        
    def run(self):
        
        if(self.textbox_tentruyen.text() != ''):
            link = self.textbox_tentruyen.text()
        else:
            return
        if(self.textbox_saveFolder.text() != ''):
            saveFolder  = self.textbox_saveFolder.text()
        else:
            saveFolder = os.getcwd()
        print(saveFolder)
        self.scr = Scrapper(link, saveFolder)
        
        
        self.getProgress()
        print("start")
        self.scr.run()
        print("end")
        self.t2.cancel()
        
        self.label_status.setText("DONE!")
        
        self.novel_name =  self.scr.novelname 
        self.zip_File(saveFolder,self.novel_name)
        self.changeExtension2Epub(saveFolder, self.novel_name)
        
        shutil.rmtree(saveFolder + '/' + self.novel_name)
    

    def getProgress(self):
        self.t2 = threading.Timer(1.0, self.getProgress)
        self.t2.start()
        self.chap = self.scr.chap_num
   
        self.progress = self.scr.chap_progress
        print(str(self.progress) + '/' + str(self.chap))
        self.label_status.setText("Progress: " + str(self.progress) + '/' + str(self.chap))
        
        
    def zip_File(self, saveFolder, novel_name):
        folder = glob.glob(saveFolder + '/' + novel_name + '/')
        print(len(folder))
        zipf = zipfile.ZipFile(saveFolder +'/' + novel_name + '.zip', 'w', zipfile.ZIP_DEFLATED)
            
        b = glob.glob(folder[0] + "*") # file
        c = glob.glob(folder[0] + "*/") #subfolder
            
        for file in b:
            zipf.write(file)
           
        for folder in c:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    zipf.write(os.path.join(root, file))
        zipf.close()
        print(folder + "zip done!")
            
    def changeExtension2Epub(self, saveFolder, novel_name):
        zfile = glob.glob(saveFolder + '/' + novel_name + '.zip')

        print(zfile)

        for file in zfile:
            
            base = os.path.splitext(file)[0]
            
            if not os.path.isfile(base + ".epub"):
                os.rename(file, base + ".epub")   
                
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())