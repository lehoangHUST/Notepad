import pytest
import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from view.notepad_view import NotepadView
from controller.notepad_controller import NotepadController

# Tạo một QApplication duy nhất cho tất cả các test
@pytest.fixture(scope="session")
def qapp():
    app = QApplication([])
    yield app
    app.quit()

@pytest.fixture
def app(qapp, qtbot):
    view = NotepadView()
    controller = NotepadController(view)
    qtbot.addWidget(view)
    return view, controller

def test_window_title(qtbot):
    view = NotepadView()
    controller = NotepadController(view)
    qtbot.addWidget(view)
    view.setWindowTitle("My Notepad - Ứng dụng ghi chú")
    assert view.windowTitle() == "My Notepad - Ứng dụng ghi chú"

def test_initial_text_empty(qtbot):
    view = NotepadView()
    controller = NotepadController(view)
    qtbot.addWidget(view)
    assert view.get_text() == ""