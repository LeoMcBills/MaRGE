"""
@author:    José Miguel Algarín
@email:     josalggui@i3m.upv.es
@affiliation:MRILab, i3M, CSIC, Valencia, Spain
"""
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QWidget, QHBoxLayout, QVBoxLayout, QTableWidget
from PyQt5.QtCore import QSize, QThreadPool
import qdarkstyle

from controller.controller_console import ConsoleController
from controller.controller_figures import FiguresLayoutController
from controller.controller_history_list import HistoryListController
from controller.controller_toolbar_marcos import MarcosController
from controller.controller_toolbar_sequences import SequenceController
from controller.controller_sequence_list import SequenceListController
from controller.controller_sequence_inputs import SequenceInputsController


class MainWindow(QMainWindow):
    def __init__(self, session, demo = False, parent=None):
        super(MainWindow, self).__init__(parent)
        self.app_open = True
        self.toolbar_sequences = None
        self.toolbar_marcos = None
        self.session = session
        self.demo = demo
        self.setWindowTitle(session['directory'])
        self.resize(QSize(800, 600))

        # Threadpool for parallel running
        self.threadpool = QThreadPool()

        # Set stylesheet
        self.styleSheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(self.styleSheet)

        # Add marcos toolbar
        self.toolbar_marcos = MarcosController(self.demo, "MaRCoS toolbar")
        self.addToolBar(self.toolbar_marcos)

        # Add sequence toolbar
        self.toolbar_sequences = SequenceController(self, "Sequence toolbar")
        self.addToolBar(self.toolbar_sequences)

        # Status bar
        self.setStatusBar(QStatusBar(self))

        # Create central widget that will contain the layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Add layout to input parameters
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Layout for inputs
        self.input_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_layout)

        # Layout for outputs
        self.output_layout = QVBoxLayout()
        self.main_layout.addLayout(self.output_layout)

        # Add sequence list
        self.sequence_list = SequenceListController(parent=self)
        self.input_layout.addWidget(self.sequence_list)

        # Add sequence inputs
        self.sequence_inputs = SequenceInputsController(parent=self)
        self.input_layout.addWidget(self.sequence_inputs)

        # Add console
        self.console = ConsoleController()
        self.input_layout.addWidget(self.console)

        # Add layout to show the figures
        self.figures_layout = FiguresLayoutController()
        self.output_layout.addWidget(self.figures_layout)

        # Layout for output history
        self.output_layout_h = QHBoxLayout()
        self.output_layout.addLayout(self.output_layout_h)

        # Add list to show the history
        self.history_list = HistoryListController(parent=self)
        self.output_layout_h.addWidget(self.history_list)
        self.history_list.setMaximumHeight(200)
        self.history_list.setMinimumHeight(200)

        # Table with input parameters from historic images
        self.input_table = QTableWidget()
        self.input_table.setMaximumHeight(200)
        self.input_table.setMinimumHeight(200)
        self.output_layout_h.addWidget(self.input_table)



