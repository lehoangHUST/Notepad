from model.notepad_model import NotepadModel

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