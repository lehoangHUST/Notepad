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
        
    def insert_text(self, text):
        self.ui.textEdit.insertPlainText(text)

    def show_error(self, message):
        QMessageBox.critical(self, "Lỗi", message)

    def get_save_path(self):
        return QFileDialog.getSaveFileName(self, "Lưu file", "", "Text Files (*.txt);;All Files (*)")[0]

    def get_open_path(self):
        return QFileDialog.getOpenFileName(self, "Mở file", "", "Text Files (*.txt);;All Files (*)")[0]

    def get_cursor(self):
        return self.ui.textEdit.textCursor()
        
    def set_cursor(self, cursor):
        self.ui.textEdit.setTextCursor(cursor)  # Set cursor to the end of the textEdit``
        
    def find_cursor(self, text, cursor):
        return self.ui.textEdit.document().find(text, cursor)
    
    def add_shortcuts(self):
        self.ui.actionNew.setShortcut("Ctrl+N")       # Open new file
        self.ui.actionOpen_File.setShortcut("Ctrl+O") # Open file
        self.ui.actionSave.setShortcut("Ctrl+S")      # Save file
        self.ui.actionSave_As.setShortcut("Ctrl+Shift+S")  # Save file with new file
        self.ui.actionExit.setShortcut("Ctrl+Q")      # Exit
        self.ui.actionCopy.setShortcut("Ctrl+C")      # Copy
        self.ui.actionCut.setShortcut("Ctrl+X")       # Cut
        self.ui.actionPaste.setShortcut("Ctrl+V")     # Paste
        self.ui.actionUndo.setShortcut("Ctrl+Z")      # Undo
        self.ui.actionSearch_with_Bing.setShortcut("Ctrl+E")      # Search
        self.ui.actionFind.setShortcut("Ctrl+F")      # Find


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
        
        # Kết nối các theo tác tìm kiếm
        self.ui.actionSearch_with_Bing.triggered.connect(controller.search_with_bing)
        self.ui.actionFind.triggered.connect(controller.find_text)
        self.ui.actionFind_Next.triggered.connect(controller.find_next_text)
        self.ui.actionFind_Previous.triggered.connect(controller.find_previous_text)
        self.ui.actionReplace.triggered.connect(controller.replace_text)
        self.ui.actionGo_to.triggered.connect(controller.go_to_line)
        self.ui.actionTime_Date.triggered.connect(controller.insert_time_date)