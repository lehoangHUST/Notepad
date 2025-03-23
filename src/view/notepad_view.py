from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from .notepad_ui import Ui_MainWindow

class NotepadView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def get_text(self):
        return self.ui.textEdit.toPlainText()

    def set_text(self, text):
        self.ui.textEdit.setText(text)

    def show_error(self, message):
        QMessageBox.critical(self, "Lỗi", message)

    def get_save_path(self):
        return QFileDialog.getSaveFileName(self, "Lưu file", "", "Text Files (*.txt);;All Files (*)")[0]

    def get_open_path(self):
        return QFileDialog.getOpenFileName(self, "Mở file", "", "Text Files (*.txt);;All Files (*)")[0]
    
    def add_shortcuts(self):
        self.ui.actionNew.setShortcut("Ctrl+N")       # Open new file
        self.ui.actionOpen_File.setShortcut("Ctrl+O") # Open file
        self.ui.actionSave.setShortcut("Ctrl+S")      # Save file
        self.ui.actionSave_As.setShortcut("Ctrl+Shift+S")  # Save file with new file
        self.ui.actionExit.setShortcut("Ctrl+Q")      # Exit

    def connect_actions(self, controller):
        
        self.add_shortcuts()
        
        self.ui.actionNew.triggered.connect(controller.new_file)
        self.ui.actionOpen_File.triggered.connect(controller.open_file)
        self.ui.actionSave.triggered.connect(controller.save_file)
        self.ui.actionSave_As.triggered.connect(controller.save_file_as)
        self.ui.actionExit.triggered.connect(self.close)

        # Kết nối thao tác chỉnh sửa
        self.ui.actionCut.triggered.connect(self.ui.textEdit.cut)
        self.ui.actionCopy.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit.paste)
        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)