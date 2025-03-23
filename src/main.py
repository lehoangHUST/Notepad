import sys
from PyQt5.QtWidgets import QApplication
from view.notepad_view import NotepadView
from controller.notepad_controller import NotepadController

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Khởi tạo View và Controller
    view = NotepadView()
    controller = NotepadController(view)

    # Hiển thị ứng dụng
    view.show()
    sys.exit(app.exec_())