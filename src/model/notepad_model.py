class NotepadModel:
    def __init__(self):
        self.current_file = ""

    def open_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.current_file = file_path
            return content
        except Exception as e:
            raise Exception(f"Lỗi mở file: {e}")

    def save_file(self, file_path, content):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.current_file = file_path
        except Exception as e:
            raise Exception(f"Lỗi lưu file: {e}")

    def get_current_file(self):
        return self.current_file