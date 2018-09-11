from parserPack.RE_ValueAnalyzer import valueParser


# Обработчик значения
def valueHandler(sheet, cell):
    cellRowCorrection = 0
    if cell.row % 2 != 0:
        cellRowCorrection -= 1

    if cell.value:
        cellValue = sheet[cell.column + str(cell.row)].value
        typeValue = sheet.cell(column=cell.col_idx + 1, row=cell.row).value
        teacherValue = sheet.cell(column=cell.col_idx + 2, row=cell.row).value
        roomValue = sheet.cell(column=cell.col_idx + 3, row=cell.row).value

        newLine = -1
        newTpLine = -1
        newTcLine = -1
        newRmLine = -1

        if cellValue: newLine = str(cellValue).find('\n')
        if typeValue: newTpLine = str(typeValue).find('\n')
        if teacherValue: newTcLine = str(teacherValue).find('\n')
        if roomValue: newRmLine = str(roomValue).find('\n')

        lessons = []
        valueParseArgs1 = [None, None, None, None]
        valueParseArgs2 = [None, None, None, None]

        if newLine != -1 and cellValue:
            valueParseArgs1[0] = cellValue[:newLine]
            valueParseArgs2[0] = cellValue[newLine + 1:]
        else:
            valueParseArgs1[0] = cellValue
        if newTpLine != -1:
            valueParseArgs1[1] = typeValue[:newTpLine]
            valueParseArgs2[1] = typeValue[newTpLine + 1:]
        else:
            valueParseArgs1[1] = typeValue
        if newTcLine != -1:
            valueParseArgs1[2] = teacherValue[:newTcLine]
            valueParseArgs2[2] = teacherValue[newTcLine + 1:]
        else:
            valueParseArgs1[2] = teacherValue
        if newRmLine != -1:
            if newLine == -1:
                valueParseArgs1[3] = roomValue[:newRmLine] + roomValue[newRmLine + 1:]
            else:
                valueParseArgs1[3] = roomValue[:newRmLine]
                valueParseArgs2[3] = roomValue[newRmLine + 1:]
        else:
            valueParseArgs1[3] = roomValue
        if valueParseArgs1[0] or valueParseArgs1[1] or valueParseArgs1[2] or valueParseArgs1[3]:
            lessons.append(valueParser(valueParseArgs1[0],
                                                        valueParseArgs1[1],
                                                        valueParseArgs1[2],
                                                        valueParseArgs1[3],
                                                        sheet.cell(column=cell.col_idx - 4,
                                                                   row=cell.row + cellRowCorrection).value))
        if valueParseArgs2[0] or valueParseArgs2[1] or valueParseArgs2[2] or valueParseArgs2[3]:
            lessons.append(valueParser(valueParseArgs2[0],
                                                        valueParseArgs2[1],
                                                        valueParseArgs2[2],
                                                        valueParseArgs2[3],
                                                        sheet.cell(column=cell.col_idx - 4,
                                                                   row=cell.row + cellRowCorrection).value))

        return lessons
