import sys
import os
from InstallWindow import InstallWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer
#Creating MainScreen class for SplashScreen
class MainScreen():
    def showSplashScreen(self):
        self.pix=QPixmap("python_vehicle.jpg")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()


def showSetupWindow():#Function to show installWindow
    mainScreen.splassh.close()
    installWindow.show()



def showLoginWindow(): #function to show login window
    mainScreen.splassh.close()
    login.showLoginScreen()



app=QApplication(sys.argv)
login=LoginScreen()
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"): #if .json file exist show Login Window
    QTimer.singleShot(3000,showLoginWindow) #Used to call Setup and LoginWindow After 3 second of delay
else:#else show setup window
    QTimer.singleShot(3000,showSetupWindow)


sys.exit(app.exec_()) #Program Termination on app close