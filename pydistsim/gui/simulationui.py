# Form implementation generated from reading ui file 'simulation.ui'
#
# Created: Wed Feb 06 01:24:05 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_SimulationWindow:
    def setupUi(self, SimulationWindow):
        SimulationWindow.setObjectName("SimulationWindow")
        SimulationWindow.resize(1106, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(SimulationWindow.sizePolicy().hasHeightForWidth())
        SimulationWindow.setSizePolicy(sizePolicy)
        SimulationWindow.setMinimumSize(QSize(1096, 800))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/pydistsim.png"), QIcon.Normal, QIcon.Off)
        SimulationWindow.setWindowIcon(icon)
        SimulationWindow.setDockOptions(
            QMainWindow.AllowTabbedDocks
            | QMainWindow.AnimatedDocks
            | QMainWindow.VerticalTabs
        )
        self.centralwidget = QWidget(SimulationWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftWidget = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout_3 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.controlGroupBox = QGroupBox(self.leftWidget)
        self.controlGroupBox.setMinimumSize(QSize(0, 0))
        self.controlGroupBox.setObjectName("controlGroupBox")
        self.verticalLayout_5 = QVBoxLayout(self.controlGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QWidget(self.controlGroupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.stepSize = QSpinBox(self.widget)
        self.stepSize.setAccelerated(True)
        self.stepSize.setMaximum(999)
        self.stepSize.setProperty("value", 1)
        self.stepSize.setObjectName("stepSize")
        self.horizontalLayout_2.addWidget(self.stepSize)
        self.verticalLayout_5.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.controlGroupBox)
        self.viewGroupBox = QGroupBox(self.leftWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewGroupBox.sizePolicy().hasHeightForWidth())
        self.viewGroupBox.setSizePolicy(sizePolicy)
        self.viewGroupBox.setObjectName("viewGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.viewGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.networkViewGroup = QGroupBox(self.viewGroupBox)
        self.networkViewGroup.setObjectName("networkViewGroup")
        self.verticalLayout_6 = QVBoxLayout(self.networkViewGroup)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.showNodes = QCheckBox(self.networkViewGroup)
        self.showNodes.setChecked(True)
        self.showNodes.setObjectName("showNodes")
        self.verticalLayout_6.addWidget(self.showNodes)
        self.showEdges = QCheckBox(self.networkViewGroup)
        self.showEdges.setChecked(True)
        self.showEdges.setObjectName("showEdges")
        self.verticalLayout_6.addWidget(self.showEdges)
        self.showMessages = QCheckBox(self.networkViewGroup)
        self.showMessages.setChecked(True)
        self.showMessages.setObjectName("showMessages")
        self.verticalLayout_6.addWidget(self.showMessages)
        self.showLabels = QCheckBox(self.networkViewGroup)
        self.showLabels.setChecked(True)
        self.showLabels.setObjectName("showLabels")
        self.verticalLayout_6.addWidget(self.showLabels)
        self.redrawNetworkButton = QPushButton(self.networkViewGroup)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.redrawNetworkButton.sizePolicy().hasHeightForWidth()
        )
        self.redrawNetworkButton.setSizePolicy(sizePolicy)
        self.redrawNetworkButton.setObjectName("redrawNetworkButton")
        self.verticalLayout_6.addWidget(self.redrawNetworkButton)
        self.verticalLayout_2.addWidget(self.networkViewGroup)
        self.treeGroupBox = QGroupBox(self.viewGroupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeGroupBox.sizePolicy().hasHeightForWidth())
        self.treeGroupBox.setSizePolicy(sizePolicy)
        self.treeGroupBox.setMinimumSize(QSize(132, 60))
        self.treeGroupBox.setFlat(False)
        self.treeGroupBox.setCheckable(True)
        self.treeGroupBox.setChecked(True)
        self.treeGroupBox.setObjectName("treeGroupBox")
        self.treeKey = QLineEdit(self.treeGroupBox)
        self.treeKey.setGeometry(QRect(42, 20, 71, 20))
        self.treeKey.setFrame(True)
        self.treeKey.setObjectName("treeKey")
        self.label = QLabel(self.treeGroupBox)
        self.label.setGeometry(QRect(10, 22, 31, 16))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.treeGroupBox)
        self.propagationError = QGroupBox(self.viewGroupBox)
        self.propagationError.setMinimumSize(QSize(132, 70))
        self.propagationError.setCheckable(True)
        self.propagationError.setChecked(False)
        self.propagationError.setObjectName("propagationError")
        self.locKey = QLineEdit(self.propagationError)
        self.locKey.setGeometry(QRect(10, 40, 111, 20))
        self.locKey.setObjectName("locKey")
        self.label2 = QLabel(self.propagationError)
        self.label2.setGeometry(QRect(10, 20, 46, 13))
        self.label2.setObjectName("label2")
        self.verticalLayout_2.addWidget(self.propagationError)
        self.verticalLayout_3.addWidget(self.viewGroupBox)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.leftWidget)
        spacerItem1 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.networkDisplayWidget = QWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.networkDisplayWidget.sizePolicy().hasHeightForWidth()
        )
        self.networkDisplayWidget.setSizePolicy(sizePolicy)
        self.networkDisplayWidget.setMinimumSize(QSize(650, 0))
        self.networkDisplayWidget.setObjectName("networkDisplayWidget")
        self.horizontalLayout.addWidget(self.networkDisplayWidget)
        spacerItem2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        SimulationWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(SimulationWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setObjectName("toolBar")
        SimulationWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.menubar = QMenuBar(SimulationWindow)
        self.menubar.setGeometry(QRect(0, 0, 1106, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimulation = QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        SimulationWindow.setMenuBar(self.menubar)
        self.dockWidget = QDockWidget(SimulationWindow)
        self.dockWidget.setMinimumSize(QSize(87, 109))
        self.dockWidget.setFeatures(
            QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable
        )
        self.dockWidget.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dockWidgetContents.sizePolicy().hasHeightForWidth()
        )
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout_3 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.networkInspector = QTreeView(self.dockWidgetContents)
        self.networkInspector.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.networkInspector.setFrameShape(QFrame.NoFrame)
        self.networkInspector.setProperty("showDropIndicator", False)
        self.networkInspector.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.networkInspector.setAnimated(True)
        self.networkInspector.setWordWrap(True)
        self.networkInspector.setHeaderHidden(True)
        self.networkInspector.setObjectName("networkInspector")
        self.horizontalLayout_3.addWidget(self.networkInspector)
        self.dockWidget.setWidget(self.dockWidgetContents)
        SimulationWindow.addDockWidget(Qt.DockWidgetArea(2), self.dockWidget)
        self.dockWidget_2 = QDockWidget(SimulationWindow)
        self.dockWidget_2.setMinimumSize(QSize(105, 377))
        self.dockWidget_2.setFeatures(
            QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable
        )
        self.dockWidget_2.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dockWidgetContents_2.sizePolicy().hasHeightForWidth()
        )
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_4 = QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nodeInspector = QTreeView(self.dockWidgetContents_2)
        sizePolicy = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nodeInspector.sizePolicy().hasHeightForWidth()
        )
        self.nodeInspector.setSizePolicy(sizePolicy)
        self.nodeInspector.setMinimumSize(QSize(87, 337))
        self.nodeInspector.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.nodeInspector.setFrameShape(QFrame.NoFrame)
        self.nodeInspector.setProperty("showDropIndicator", False)
        self.nodeInspector.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.nodeInspector.setAnimated(True)
        self.nodeInspector.setWordWrap(True)
        self.nodeInspector.setHeaderHidden(True)
        self.nodeInspector.setObjectName("nodeInspector")
        self.horizontalLayout_4.addWidget(self.nodeInspector)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        SimulationWindow.addDockWidget(Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_3 = QDockWidget(SimulationWindow)
        self.dockWidget_3.setMinimumSize(QSize(87, 109))
        self.dockWidget_3.setFeatures(
            QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable
        )
        self.dockWidget_3.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dockWidgetContents_3.sizePolicy().hasHeightForWidth()
        )
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_5 = QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logListWidget = QListWidget(self.dockWidgetContents_3)
        self.logListWidget.setFrameShape(QFrame.NoFrame)
        self.logListWidget.setFrameShadow(QFrame.Sunken)
        self.logListWidget.setLineWidth(0)
        self.logListWidget.setObjectName("logListWidget")
        self.horizontalLayout_5.addWidget(self.logListWidget)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        SimulationWindow.addDockWidget(Qt.DockWidgetArea(2), self.dockWidget_3)
        self.actionRun = QAction(SimulationWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/player_play.png"), QIcon.Normal, QIcon.Off)
        self.actionRun.setIcon(icon1)
        self.actionRun.setObjectName("actionRun")
        self.actionStep = QAction(SimulationWindow)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/icons/player_fwd.png"), QIcon.Normal, QIcon.Off)
        self.actionStep.setIcon(icon2)
        self.actionStep.setObjectName("actionStep")
        self.actionReset = QAction(SimulationWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/player_start.png"), QIcon.Normal, QIcon.Off)
        self.actionReset.setIcon(icon3)
        self.actionReset.setObjectName("actionReset")
        self.actionCopyInspectorData = QAction(SimulationWindow)
        self.actionCopyInspectorData.setShortcutContext(Qt.WidgetShortcut)
        self.actionCopyInspectorData.setObjectName("actionCopyInspectorData")
        self.actionSaveNetwork = QAction(SimulationWindow)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/filesaveas.png"), QIcon.Normal, QIcon.Off)
        self.actionSaveNetwork.setIcon(icon4)
        self.actionSaveNetwork.setObjectName("actionSaveNetwork")
        self.actionOpenNetwork = QAction(SimulationWindow)
        self.actionOpenNetwork.setCheckable(False)
        self.actionOpenNetwork.setChecked(False)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/icons/fileopen.png"), QIcon.Normal, QIcon.Off)
        self.actionOpenNetwork.setIcon(icon5)
        self.actionOpenNetwork.setObjectName("actionOpenNetwork")
        self.actionShowLocalizedSubclusters = QAction(SimulationWindow)
        self.actionShowLocalizedSubclusters.setObjectName(
            "actionShowLocalizedSubclusters"
        )
        self.toolBar.addAction(self.actionOpenNetwork)
        self.toolBar.addAction(self.actionSaveNetwork)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionStep)
        self.toolBar.addAction(self.actionReset)
        self.menuFile.addAction(self.actionOpenNetwork)
        self.menuFile.addAction(self.actionSaveNetwork)
        self.menuSimulation.addAction(self.actionRun)
        self.menuSimulation.addAction(self.actionStep)
        self.menuSimulation.addAction(self.actionReset)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())

        self.retranslateUi(SimulationWindow)
        QMetaObject.connectSlotsByName(SimulationWindow)
        SimulationWindow.setTabOrder(self.stepSize, self.treeKey)

    def retranslateUi(self, SimulationWindow):
        SimulationWindow.setWindowTitle(
            QApplication.translate("SimulationWindow", "PyDistSim Simulation", None)
        )
        self.controlGroupBox.setTitle(
            QApplication.translate("SimulationWindow", "Control", None)
        )
        self.label_2.setText(
            QApplication.translate("SimulationWindow", "Step size:", None)
        )
        self.stepSize.setSpecialValueText(
            QApplication.translate("SimulationWindow", "All", None)
        )
        self.viewGroupBox.setTitle(
            QApplication.translate("SimulationWindow", "View", None)
        )
        self.networkViewGroup.setTitle(
            QApplication.translate("SimulationWindow", "Network", None)
        )
        self.showNodes.setText(
            QApplication.translate("SimulationWindow", "Nodes", None)
        )
        self.showEdges.setText(
            QApplication.translate("SimulationWindow", "Edges", None)
        )
        self.showMessages.setText(
            QApplication.translate("SimulationWindow", "Messages", None)
        )
        self.showLabels.setText(
            QApplication.translate("SimulationWindow", "Labels", None)
        )
        self.redrawNetworkButton.setText(
            QApplication.translate("SimulationWindow", "Redraw", None)
        )
        self.treeGroupBox.setToolTip(
            QApplication.translate(
                "SimulationWindow",
                "Enter memory key that has parent and child items.",
                None,
            )
        )
        self.treeGroupBox.setTitle(
            QApplication.translate("SimulationWindow", "Tree", None)
        )
        self.treeKey.setText(
            QApplication.translate("SimulationWindow", "treeNeighbors", None)
        )
        self.label.setText(QApplication.translate("SimulationWindow", "Key:", None))
        self.propagationError.setToolTip(
            QApplication.translate(
                "SimulationWindow",
                "Enter memory key that has stitch location data.",
                None,
            )
        )
        self.propagationError.setTitle(
            QApplication.translate("SimulationWindow", "Propagation error", None)
        )
        self.locKey.setText(
            QApplication.translate("SimulationWindow", "convergecastLoc", None)
        )
        self.label2.setText(QApplication.translate("SimulationWindow", "LocKey:", None))
        self.toolBar.setWindowTitle(
            QApplication.translate("SimulationWindow", "toolBar", None)
        )
        self.menuFile.setTitle(QApplication.translate("SimulationWindow", "File", None))
        self.menuSimulation.setTitle(
            QApplication.translate("SimulationWindow", "Simulation", None)
        )
        self.dockWidget.setWindowTitle(
            QApplication.translate("SimulationWindow", "Network inspector", None)
        )
        self.dockWidget_2.setWindowTitle(
            QApplication.translate("SimulationWindow", "Node inspector", None)
        )
        self.dockWidget_3.setWindowTitle(
            QApplication.translate("SimulationWindow", "Log", None)
        )
        self.actionRun.setText(QApplication.translate("SimulationWindow", "Run", None))
        self.actionRun.setToolTip(
            QApplication.translate(
                "SimulationWindow", "Run simulation from beginning", None
            )
        )
        self.actionRun.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+R", None)
        )
        self.actionStep.setText(
            QApplication.translate("SimulationWindow", "Step", None)
        )
        self.actionStep.setToolTip(
            QApplication.translate("SimulationWindow", "Run next step", None)
        )
        self.actionStep.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+Space", None)
        )
        self.actionReset.setText(
            QApplication.translate("SimulationWindow", "Reset", None)
        )
        self.actionReset.setToolTip(
            QApplication.translate("SimulationWindow", "Reset simulation", None)
        )
        self.actionReset.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+W", None)
        )
        self.actionCopyInspectorData.setText(
            QApplication.translate("SimulationWindow", "Copy", None)
        )
        self.actionCopyInspectorData.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+C", None)
        )
        self.actionSaveNetwork.setText(
            QApplication.translate("SimulationWindow", "Save", None)
        )
        self.actionSaveNetwork.setToolTip(
            QApplication.translate(
                "SimulationWindow", "Save network in npickle format", None
            )
        )
        self.actionSaveNetwork.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+S", None)
        )
        self.actionOpenNetwork.setText(
            QApplication.translate("SimulationWindow", "Open", None)
        )
        self.actionOpenNetwork.setToolTip(
            QApplication.translate(
                "SimulationWindow", "Open network from npickle", None
            )
        )
        self.actionOpenNetwork.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+O", None)
        )
        self.actionShowLocalizedSubclusters.setText(
            QApplication.translate(
                "SimulationWindow", "Show localized subclusters", None
            )
        )
        self.actionShowLocalizedSubclusters.setToolTip(
            QApplication.translate(
                "SimulationWindow",
                "Show localized subclusters based on memory field that has positions and subclusters items.",
                None,
            )
        )
        self.actionShowLocalizedSubclusters.setShortcut(
            QApplication.translate("SimulationWindow", "Ctrl+L", None)
        )


try:
    from . import icons_rc
except ImportError:
    import icons_rc