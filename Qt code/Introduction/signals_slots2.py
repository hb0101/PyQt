# Filename: signals_slots2.py

"""Signals and slots example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from functools import partial



def greeting(who):
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f'Hello {who}')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(partial(greeting, 'Hosein!'))  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())