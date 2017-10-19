#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyossia-pyqt module add Graphical User Interface for libossia devices
TODO : create a generic panel with an address attribute
it will automagically display the coreespondant UI for the address
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QGroupBox, QLabel, QHBoxLayout, QSlider, QDial, QLineEdit
from PyQt5.QtGui import QFont


class AbstractValue(QGroupBox):
    """
    This must be sublassed with a value attribute set to a UI widget / object
    PyQt Widget that display label with parameter of the parameter
    """
    def __init__(self, parameter):
        super(AbstractValue, self).__init__()
        self.parameter = parameter
        # Create label with parameter
        self.label = QLabel(str(self.parameter.node))
        self.label.setFixedSize(100, 20)
        self.label.setFont(QFont('Helvetica', 12, QFont.Light))
        # Create parameter layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        #self.setFixedSize(300, 45)
        self.setFixedWidth(300)

    def new_value(self, value):
        """
        check if a new value is there
        """
        if value != self.getUI():
            # this is a new value, please set the UI
            # block signal from new value
            self.value.blockSignals(True)
            self.value.setUpdatesEnabled(False)
            self.setUI(value)
            self.value.blockSignals(False)
            self.value.setUpdatesEnabled(True)


class IntUI(AbstractValue):
    """
    docstring for FloatUI
    """
    def __init__(self, parameter):
        super(IntUI, self).__init__(parameter)
        self.value = QSlider(Qt.Horizontal, None)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            if self.parameter.domain.min:
                range_min = self.parameter.domain.min*32768
            else:
                range_min = 0
            if self.parameter.domain.max:
                range_max = self.parameter.domain.max*32768
            else:
                range_max = 100
        else:
            self.value.setRange(0, 100)
        self.value.valueChanged.connect(self.parameter.push_value)

    def setUI(self, value):
        self.value.setSliderPosition(value)

    def getUI(self):
        return self.value.sliderPosition()


class FloatUI(AbstractValue):
    """
    docstring for FloatUI
    """
    def __init__(self, parameter):
        super(FloatUI, self).__init__(parameter)
        self.value = QSlider(Qt.Horizontal, None)
        self.layout.addWidget(self.value)
        print('-----', self.parameter.have_domain())
        if self.parameter.have_domain():
            if self.parameter.min:
                range_min = self.parameter.min*32768
            else:
                range_min = 0
            if self.parameter.max:
                range_max = self.parameter.max*32768
            else:
                range_max = 32768
            self.value.setRange(range_min, range_max)
        else:
            self.value.setRange(0, 32768)
        def parameter_push(value):
            value = float(value/32768)
            self.parameter.push_value(value)
        self.value.valueChanged.connect(parameter_push)

    def setUI(self, value):
        self.value.setSliderPosition(value*32768)

    def getUI(self):
        return self.value.sliderPosition()/32768

class BoolUI(AbstractValue):
    """
    docstring for BoolUI
    """
    def __init__(self, parameter):
        super(BoolUI, self).__init__(parameter)
        self.value = QPushButton(str(self.parameter.value))
        self.value.setCheckable(True)
        self.value.toggled.connect(lambda value: self.value.setText(str(value)))
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        self.value.toggled.connect(self.parameter.push_value)

    def setUI(self, value):
        self.value.setChecked(value)
        self.value.setText(str(value))

    def getUI(self):
        return self.value.isChecked()


class TextUI(AbstractValue):
    """
    This must be subclassed
    """
    def __init__(self, parameter):
        super(TextUI, self).__init__(parameter)

    def setUI(self, value):
        self.value.setText(str(value))

    def getUI(self):
        return self.value.text()


class CharUI(TextUI):
    """
    docstring for StringUI
    """
    def __init__(self, parameter):
        super(CharUI, self).__init__(parameter)
        self.value = QLineEdit()
        self.value.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        self.value.textEdited.connect(self.parameter.push_value)


class ListUI(TextUI):
    """
    docstring for StringUI
    """
    def __init__(self, parameter):
        super(ListUI, self).__init__(parameter)
        self.value = QLineEdit()
        self.value.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        def parameter_push(value):
            value = value.split(' ')
            self.parameter.value = value
        self.value.textEdited.connect(parameter_push)


    def setUI(self, value):
        self.value.setText(", ".join(value))


class StringUI(TextUI):
    """
    docstring for StringUI
    """
    def __init__(self, parameter):
        super(StringUI, self).__init__(parameter)
        self.value = QLineEdit()
        self.value.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        self.value.textEdited.connect(self.parameter.push_value)



class Vec2fUI(AbstractValue):
    """
    docstring for Vec3f
    """
    def __init__(self, parameter):
        super(Vec2fUI, self).__init__(parameter)
        self.value1 = QDial()
        self.value2 = QDial()
        self.value1.setValue(1)
        self.value2.setValue(1)
        self.value1.setFixedSize(35, 35)
        self.value2.setFixedSize(35, 35)
        self.value1.setRange(0, 32768)
        self.value2.setRange(0, 32768)
        def parameter_push():
            value_1 = self.value1.value()/32768
            value_2 = self.value2.value()/32768
            self.parameter.value = [value_1, value_2]
        self.value1.valueChanged.connect(parameter_push)
        self.value2.valueChanged.connect(parameter_push)
        self.layout.addWidget(self.value1)
        self.layout.addWidget(self.value2)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        self.parameter.add_callback(self.new_value)

    def parameter_update(self, value):
        value1 = value[0]
        value2 = value[1]
        self.new_value([value1, value2])

    def setValue(self, value):
        """
        Set the value of the GUI
        """
        self.value1.setValue(value[0])
        self.value2.setValue(value[1])

    def new_value(self, new_value):
        """
        check if a new value is different than current UI value
        if yes, it will update it
        """
        new_value1 = new_value[0]
        new_value2 = new_value[1]
        if new_value1 != self.value1.value():
            self.value1.setValue(int(new_value1*32768))
        if new_value2 != self.value2.value():
            self.value2.setValue(int(new_value2*32768))


class Vec3fUI(AbstractValue):
    """
    docstring for Vec3f
    """
    def __init__(self, parameter):
        super(Vec3fUI, self).__init__(parameter)
        self.value1 = QDial()
        self.value2 = QDial()
        self.value3 = QDial()
        self.value1.setValue(1)
        self.value2.setValue(1)
        self.value3.setValue(1)
        self.value1.setFixedSize(35, 35)
        self.value2.setFixedSize(35, 35)
        self.value3.setFixedSize(35, 35)
        self.value1.setRange(0, 32768)
        self.value2.setRange(0, 32768)
        self.value3.setRange(0, 32768)
        def parameter_push():
            value_1 = self.value1.value()/32768
            value_2 = self.value2.value()/32768
            value_3 = self.value3.value()/32768
            self.parameter.value = [value_1, value_2, value_3]
        self.value1.valueChanged.connect(parameter_push)
        self.value2.valueChanged.connect(parameter_push)
        self.value3.valueChanged.connect(parameter_push)
        self.layout.addWidget(self.value1)
        self.layout.addWidget(self.value2)
        self.layout.addWidget(self.value3)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        self.parameter.add_callback(self.new_value)

    def parameter_update(self, value):
        value1 = int(value[0]*32768)
        value2 = int(value[1]*32768)
        value3 = int(value[2]*32768)
        self.setValue([value1, value2, value3])

    def setValue(self, value):
        """
        Set the value of the GUI
        """
        self.value1.setValue(int(value[0]*32768))
        self.value2.setValue(int(value[1]*32768))
        self.value3.setValue(int(value[2]*32768))

    def new_value(self, new_value):
        """
        check if a new value is there
        """
        new_value1 = int(new_value[0]*32768)
        new_value2 = int(new_value[1]*32768)
        new_value3 = int(new_value[2]*32768)
        if new_value1 != self.value1.value():
            self.value1.setValue(new_value2)
        if new_value2 != self.value2.value():
            self.value2.setValue(new_value2)
        if new_value3 != self.value3.value():
            self.value3.setValue(new_value3)


class Vec4fUI(AbstractValue):
    """
    docstring for Vec3f
    """
    def __init__(self, parameter):
        super(Vec4fUI, self).__init__(parameter)
        self.value1 = QDial()
        self.value2 = QDial()
        self.value3 = QDial()
        self.value4 = QDial()
        self.value1.setValue(1)
        self.value2.setValue(1)
        self.value3.setValue(1)
        self.value4.setValue(1)
        self.value1.setFixedSize(35, 35)
        self.value2.setFixedSize(35, 35)
        self.value3.setFixedSize(35, 35)
        self.value4.setFixedSize(35, 35)
        self.value1.setRange(0, 32768)
        self.value2.setRange(0, 32768)
        self.value3.setRange(0, 32768)
        self.value4.setRange(0, 32768)
        def parameter_push():
            value_1 = self.value1.value()/32768
            value_2 = self.value2.value()/32768
            value_3 = self.value3.value()/32768
            value_4 = self.value4.value()/32768
            self.parameter.value = [value_1, value_2, value_3, value_4]
        # TODO : separate in 4 parameter1_push etc…
        self.value1.valueChanged.connect(parameter_push)
        self.value2.valueChanged.connect(parameter_push)
        self.value3.valueChanged.connect(parameter_push)
        self.value4.valueChanged.connect(parameter_push)
        self.layout.addWidget(self.value1)
        self.layout.addWidget(self.value2)
        self.layout.addWidget(self.value3)
        self.layout.addWidget(self.value4)
        if self.parameter.have_domain():
            ### SOMETHING TO DO
            print('do something please with domain of ' + str(self.parameter))
        self.parameter.add_callback(self.new_value)

    def setValue(self, value):
        """
        Set the value of the GUI
        """
        self.value1.setValue(int(value[0]*32768))
        self.value2.setValue(int(value[1]*32768))
        self.value3.setValue(int(value[2]*32768))
        self.value4.setValue(int(value[3]*32768))

    def new_value(self, new_value):
        """
        check if a new value is there
        """
        new_value1 = int(new_value[0]*32768)
        new_value2 = int(new_value[1]*32768)
        new_value3 = int(new_value[2]*32768)
        new_value4 = int(new_value[3]*32768)
        if new_value1 != self.value1.value():
            self.value1.setValue(new_value1)
        if new_value2 != self.value2.value():
            self.value2.setValue(new_value2)
        if new_value3 != self.value3.value():
            self.value3.setValue(new_value3)
        if new_value4 != self.value4.value():
            self.value4.setValue(new_value4)


