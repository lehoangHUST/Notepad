from model.notepad_model import NotepadModel
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QTextCursor, QTextDocument
import webbrowser

class NotepadController:
    def __init__(self, view):
        self.view = view
        self.model = NotepadModel()
        self.view.connect_actions(self)

    def new_file(self):
        self.view.set_text("")
        self.model.current_file = ""

    def open_file(self):
        file_path = self.view.get_open_path()
        if file_path:
            try:
                content = self.model.open_file(file_path)
                self.view.set_text(content)
            except Exception as e:
                self.view.show_error(str(e))

    def save_file(self):
        current_file = self.model.get_current_file()
        if current_file:
            self._save_to_path(current_file)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = self.view.get_save_path()
        if file_path:
            self._save_to_path(file_path)

    def _save_to_path(self, file_path):
        try:
            content = self.view.get_text()
            self.model.save_file(file_path, content)
        except Exception as e:
            self.view.show_error(str(e))
            
    def find_text(self):
        cursor = self.view.get_cursor()
        if cursor.hasSelection():
            text = cursor.selectedText()
            cursor = self.view.find_cursor(text, cursor)
            if not cursor.isNull():
                self.view.set_cursor(cursor)
            else:
                QMessageBox.information(self.view, "Find Next", "No more occurrences found.")
                
    def search_with_bing(self):
        cursor = self.view.get_cursor()
        selected_text = cursor.selectedText()
        if selected_text:
            url = f"https://www.bing.com/search?q={selected_text}"
            webbrowser.open(url)
        else:
            QMessageBox.information(self.view, "Search with Bing", "Please select text to search.")

    def find_next_text(self):
        cursor = self.view.get_cursor()
        if cursor.hasSelection():
            text = cursor.selectedText()
            cursor = self.view.find_cursor(text, cursor)
            if not cursor.isNull():
                self.view.set_cursor(cursor)
            else:
                QMessageBox.information(self.view, "Find Next", "No more occurrences found.")

    def find_previous_text(self):
        cursor = self.view.get_cursor()
        if cursor.hasSelection():
            text = cursor.selectedText()
            cursor = self.view.find_cursor(text, cursor)
            if not cursor.isNull():
                self.view.set_cursor(cursor)
            else:
                QMessageBox.information(self.view, "Find Previous", "No previous occurrences found.")

    def replace_text(self):
        find_text, ok = QInputDialog.getText(self.view, 'Replace', 'Find:')
        if ok and find_text:
            replace_text, ok = QInputDialog.getText(self.view, 'Replace', 'Replace with:')
            if ok:
                content = self.view.get_text()
                new_content = content.replace(find_text, replace_text)
                self.view.set_text(new_content)

    def go_to_line(self):
        line_number, ok = QInputDialog.getInt(self.view, 'Go to Line', 'Enter line number:')
        if ok:
            cursor = self.view.get_cursor()
            cursor.movePosition(QTextCursor.Start)
            cursor.movePosition(QTextCursor.Down, QTextCursor.MoveAnchor, line_number - 1)
            self.view.set_cursor(cursor)

    def insert_time_date(self):
        current_time = QDateTime.currentDateTime().toString("hh:mm dd/MM/yyyy")
        self.view.insert_text(current_time)