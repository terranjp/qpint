from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QFont, QFontDatabase
from PyQt5.QtWidgets import *
import utils.unitUtilities as utils
from utils import Q_

myUnits = utils.myUnits


class UnitConverterWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())

        # Create widget instances
        self.dimensionCombo = self.createUnitComboBox()
        self.dimensionCombo.addItems(sorted(myUnits.keys()))
        self.leftUnitCombo = self.createUnitComboBox()
        self.rightUnitCombo = self.createUnitComboBox()
        self.equalLbl = QLabel('=')
        self.equalLbl.setFont(QFont('deja vu sans mono', 11, QFont.DemiBold))
        self.leftTxt = self.createValueTxtWidget()
        self.rightTxt = self.createValueTxtWidget()

        # Create containers and add widgets
        inputWidget = QWidget()
        inputWidget.setLayout(QHBoxLayout())
        inputWidget.layout().addWidget(self.leftTxt)
        inputWidget.layout().addWidget(self.equalLbl)
        inputWidget.layout().addWidget(self.rightTxt)

        unitSelectWidget = QWidget()
        unitSelectWidget.setLayout(QHBoxLayout())
        unitSelectWidget.layout().addWidget(self.leftUnitCombo)
        unitSelectWidget.layout().addWidget(self.rightUnitCombo)

        # Add containers to main layout
        self.layout().addWidget(self.dimensionCombo)
        self.layout().addWidget(inputWidget)
        self.layout().addWidget(unitSelectWidget)

        # Connect signals
        self.rightTxt.textChanged.connect(self.handleRightTxtChange)
        self.leftTxt.textChanged.connect(self.handleLeftTxtChange)
        self.leftUnitCombo.currentIndexChanged.connect(self.handleLeftComboChange)
        self.rightUnitCombo.currentIndexChanged.connect(self.handleRightComboChange)
        self.dimensionCombo.currentIndexChanged.connect(self.handleDimensionCombo)

        self.dimensionCombo.setCurrentIndex(1)

    @staticmethod
    def createUnitComboBox() -> QComboBox:

        print(QFontDatabase().families())

        unitCombo = QComboBox()

        font = QFont('Calibri', 12)
        unitCombo.setFont(font)

        return unitCombo


    @staticmethod
    def convertUnit(value: float, oldUnit: str, newUnit: str) -> Q_:

        quantity = Q_(value, oldUnit).to(newUnit)

        return str(quantity.magnitude)

    @staticmethod
    def addItemsToCombo(items: dict, combo: QComboBox):
        combo.clear()

        for unit in items:
            combo.addItem(unit.display, unit)

    @staticmethod
    def createValueTxtWidget() -> QLineEdit:
        valueTxt = QLineEdit()

        font = QFont('Calibri', 12)
        valueTxt.setFont(font)

        validator = QDoubleValidator()
        validator.setBottom(0)

        valueTxt.setValidator(validator)
        valueTxt.setAlignment(Qt.AlignLeft)
        valueTxt.setText(str(1))

        return valueTxt

    def handleDimensionCombo(self):
        dimension = self.dimensionCombo.currentText()

        self.leftUnitCombo.currentIndexChanged.disconnect()
        self.rightUnitCombo.currentIndexChanged.disconnect()

        self.addItemsToCombo(items=myUnits[dimension], combo=self.leftUnitCombo)
        self.addItemsToCombo(items=myUnits[dimension], combo=self.rightUnitCombo)

        self.leftUnitCombo.currentIndexChanged.connect(self.handleLeftComboChange)
        self.rightUnitCombo.currentIndexChanged.connect(self.handleRightComboChange)

    def updateRightTxt(self):
        """
        Update the right text based on the lefts value and current units

        :return:

        """

        leftUnit = self.leftUnitCombo.currentData()
        rightUnit = self.rightUnitCombo.currentData()

        # oldValue =

        newValue = utils.convertUnit(value=float(self.leftTxt.text()),
                                     oldUnit=str(leftUnit),
                                     newUnit=str(rightUnit))

        # newValueString = '{:.{prec}}'.format(newValue, prec=12)

        self.rightTxt.setText(str(newValue))

    def updateLeftTxt(self):
        """
        Update the right text based on the lefts value and current units

        :return:
        """

        leftUnit = self.leftUnitCombo.currentData()
        rightUnit = self.rightUnitCombo.currentData()

        newValue = utils.convertUnit(value=float(self.rightTxt.text()),
                                     oldUnit=str(rightUnit),
                                     newUnit=str(leftUnit))

        newValueString = '{:.{prec}}'.format(newValue, prec=12)

        self.leftTxt.setText(str(newValue))

    def handleLeftComboChange(self):
        self.updateLeftTxt()

    def handleRightComboChange(self):
        self.updateRightTxt()

    def handleRightTxtChange(self):
        if self.rightTxt.hasFocus():
            self.updateLeftTxt()

    def handleLeftTxtChange(self):
        if self.leftTxt.hasFocus():
            self.updateRightTxt()
