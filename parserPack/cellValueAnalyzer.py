from parserPack.RE_ValueAnalyzer import valueParser


# Обработчик значения
def valueHandler(sheet, locCell, pairNum):
    if sheet.cell(column=locCell.col_idx, row=locCell.row-1).value == "Военная\nподготовка":
        locCell = sheet.cell(column=locCell.col_idx, row=locCell.row-1)
    if locCell.value:
        lessons = []
        cellValue = sheet[locCell.column + str(locCell.row)].value
        if cellValue != "*Занятия по адресу:" and cellValue != "ул. М.Пироговская, д.1" \
                and cellValue != "Пр-т Вернадского, 86" and cellValue != "Занятия по адресу:"\
                and cellValue != "…………………." and cellValue != "…………………" and cellValue != "……………………"\
                and cellValue != "В-86 - занятия в кампусе по адресу Проспекте Вернадского, д.86":
            typeValue = sheet.cell(column=locCell.col_idx + 1, row=locCell.row).value
            teacherValue = sheet.cell(column=locCell.col_idx + 2, row=locCell.row).value
            roomValue = sheet.cell(column=locCell.col_idx + 3, row=locCell.row).value

            newLine = -1
            newTpLine = -1
            newTcLine = -1
            newRmLine = -1

            if cellValue:
                newLine = str(cellValue).find('\n')
            if typeValue:
                newTpLine = str(typeValue).find('\n')
            if teacherValue:
                newTcLine = str(teacherValue).find('\n')
            if roomValue:
                newRmLine = str(roomValue).find('\n')

            valueParseArgs1 = [None, None, None, None]
            valueParseArgs2 = [None, None, None, None]

            if newLine != -1 and cellValue:
                valueParseArgs1[0] = cellValue[:newLine]
                valueParseArgs2[0] = cellValue[newLine + 1:]
            else:
                valueParseArgs1[0] = cellValue
            if newTpLine != -1 and valueParseArgs2[0]:
                valueParseArgs1[1] = typeValue[:newTpLine]
                valueParseArgs2[1] = typeValue[newTpLine + 1:]
            else:
                valueParseArgs1[1] = typeValue
            if newTcLine != -1 and valueParseArgs2[0]:
                valueParseArgs1[2] = teacherValue[:newTcLine]
                valueParseArgs2[2] = teacherValue[newTcLine + 1:]
            else:
                valueParseArgs1[2] = teacherValue
            if newRmLine != -1:
                if newLine == -1:
                    valueParseArgs1[3] = roomValue  # [:newRmLine] + roomValue[newRmLine + 1:]
                    #  тут подразумевалось вырезание \n
                else:
                    valueParseArgs1[3] = roomValue[:newRmLine]
                    valueParseArgs2[3] = roomValue[newRmLine + 1:]
            else:
                valueParseArgs1[3] = roomValue
            if valueParseArgs2[0] and (valueParseArgs1[0][-10:] == valueParseArgs2[0][-10:]):
                                                                    # проверка на ячейку 2,4 предмет\n кр 2,4 предмет
                                                                    # Сравнивает значения с конца, что чисто в  теории
                                                                    # позволяет понять совпадают или нет значения в яч.
                                                                    # а так же в случае если одинаковы предмет и тип
                                                                    # и, соответственно, препод, а отл аудитория
                if not valueParseArgs2[1]:
                    valueParseArgs2[1] = valueParseArgs1[1]  # они же не могут сделать два одинаковых предмета
                                                                        # и не написать к ним разные типы, если
                                                                        # типы разные?????
                if (not valueParseArgs2[2]) and (valueParseArgs2[1] == valueParseArgs1[1]):
                    valueParseArgs2[2] = valueParseArgs1[2]
            if valueParseArgs2[0] and (not valueParseArgs2[3]) and valueParseArgs1[3]:
                valueParseArgs2[3] = valueParseArgs1[3]  # случай, когда есть два значения и одна общая комната
            if valueParseArgs1[0]:
                # extend or append?
                lessons.extend(valueParser(valueParseArgs1[0],
                                                            valueParseArgs1[1],
                                                            valueParseArgs1[2],
                                                            valueParseArgs1[3],
                                                            pairNum))
            if valueParseArgs2[0]:
                # extend or append?
                lessons.extend(valueParser(valueParseArgs2[0],
                                                            valueParseArgs2[1],
                                                            valueParseArgs2[2],
                                                            valueParseArgs2[3],
                                                            pairNum))

        return lessons
