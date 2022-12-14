from ui_junkntrade import *
from Custom_Widgets.Widgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        loadJsonStyle(self, self.ui)
        self.show()

        # setting up current page
        self.ui.stackedWidget.setCurrentWidget(self.ui.profile)

        # buttons clicked
        self.ui.profileBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile))
        self.ui.redeemBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.redeem))
        self.ui.junkBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.shops))
        self.ui.rewardBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.rsystem))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
