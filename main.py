import sys
import csv
from PyQt6 import QtCore, QtWidgets, QtGui
arr_elements = []
with open("periodictable.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        arr_elements.append(line)

def printElementInfo(item):
    element_function_info = []
    for y in range(len(arr_elements)):
        if arr_elements[y][2] == item.text():
            element_function_info = arr_elements[y]
            break
    if element_function_info[11] == "":
        element_function_info[11] = "no"
    if element_function_info[12] == "":
        element_function_info[12] = "no"
    if element_function_info[13] == "":
        element_function_info[13] = "no"
    if element_function_info[14] == "":
        element_function_info[14] = "no"
    if element_function_info[8] == "":
        if element_function_info[7] == "6":
            element_function_info[8] = "Lanthanide"
        else:
            element_function_info[8] = "Actinoid"
    if element_function_info:
        info_label.setText("<table width=\"40%\"><tr><td><span style=\"font-size: 15px;\"><b>Atomic number</b>: "+element_function_info[0]+"<br>"
                           "<b>Element</b>: "+element_function_info[1]+"<br>"
                           "<b>Symbol</b>: "+element_function_info[2]+"<br>"
                           "<b>Atomic mass</b>: "+element_function_info[3]+"<br>"
                           "<b>Number of neutrons</b>: "+element_function_info[4]+"<br>"
                           "<b>Number of protons</b>: "+element_function_info[5]+"<br>"
                           "<b>Number of electrons</b>: "+element_function_info[6]+"<br>"
                           "<b>Period</b>: "+element_function_info[7]+"<br>"
                           "<b>Group</b>: "+element_function_info[8]+"<br>"
                           "<b>Phase</b>: "+element_function_info[9]+"<br>"
                           "<b>Radioactive</b>: "+element_function_info[10]+"<br>"
                           "<b>Natural</b>: "+element_function_info[11]+"<br>"
                           "<b>Metal</b>: "+element_function_info[12]+"<br>"
                           "<b>Nonmetal</b>: "+element_function_info[13]+"<br></span></td>"
                           "<td><span style=\"font-size: 15px;\"><b>Metalloid</b>: "+element_function_info[14]+"<br>"
                           "<b>Type</b>: "+element_function_info[15]+"<br>"
                           "<b>Atomic radius</b>: "+element_function_info[16]+"<br>"
                           "<b>Electronegativity</b>: "+element_function_info[17]+"<br>"
                           "<b>First ionization</b>: "+element_function_info[18]+"<br>"
                           "<b>Density</b>: "+element_function_info[19]+"<br>"
                           "<b>Melting point</b>: "+element_function_info[20]+"<br>"
                           "<b>Boiling point</b>: "+element_function_info[21]+"<br>"
                           "<b>Number of isotopes</b>: "+element_function_info[22]+"<br>"
                           "<b>Discoverer</b>: "+element_function_info[23]+"<br>"
                           "<b>Year</b>: "+element_function_info[24]+"<br>"
                           "<b>Specific heat</b>: "+element_function_info[25]+"<br>"
                           "<b>Number of shells</b>: "+element_function_info[26]+"<br>"
                           "<b>Number of valence</b>: "+element_function_info[27]+"</span></td></tr></table>")
        info_label.show()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Таблица Менделеева")
window.setWindowIcon(QtGui.QIcon('icon_app.png'))
window.resize(1850, 660)
table = QtWidgets.QTableWidget()
info_label = QtWidgets.QLabel("")
vbox = QtWidgets.QVBoxLayout()

table.setRowCount(10)
table.setColumnCount(18)

column_i1 = 0
column_i2 = 0
for y in range(len(arr_elements)):
    element_info = []
    for x in range(len(arr_elements[y])):
        element_info.append(arr_elements[y][x])

    if element_info[8] != "":
        numrow = int(element_info[7]) - 1
        numcolumn = int(element_info[8]) - 1
    else:
        numrow1 = int(element_info[7])
        if numrow1 == 6:
            numcolumn = column_i1
            column_i1 += 1
            numrow = 8
        elif numrow1 == 7:
            numcolumn = column_i2
            column_i2 += 1
            numrow = 9
    itemm = QtWidgets.QTableWidgetItem(element_info[2])
    itemm.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
    table.setItem(numrow, numcolumn, itemm)
table.itemClicked.connect(printElementInfo)

vbox.addWidget(table)
vbox.addWidget(info_label)
info_label.hide()
window.setLayout(vbox)
window.show()
sys.exit(app.exec())