import sys
from PyQt5 import QtWidgets
import windo
import os
import ParsHtmFileRQ

class ExampleApp(QtWidgets.QMainWindow, windo.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OneBtm.clicked.connect(self.browse_folder)
        self.setWindowOpacity(0.6)
        self.keys = list

    def FormInf(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.keys = ParsHtmFileRQ.one(directory + '/' + os.listdir(directory)[-1])
        return(self.keys)
    
    def browse_folder(self):
        kay = self.FormInf()
        for vid in range(len(kay)):
            self.listWidget.addItem(str(kay[vid]))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()