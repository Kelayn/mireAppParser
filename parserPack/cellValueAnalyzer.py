from parserPack.RE_ValueAnalyzer import valueParser


# Обработчик значения
def valueHandler(sheet, locCell, pairNum):
    if sheet.cell(column=locCell.col_idx, row=locCell.row-1).value == "Военная\nподготовка":
        locCell = sheet.cell(column=locCell.col_idx, row=locCell.row-1)
    if locCell.value:

        lessons = []
        typeO_List = []
        teacher_List = []
        room_List = []

        cellValue = sheet[locCell.column + str(locCell.row)].value
        if cellValue != "*Занятия по адресу:" and cellValue != "ул. М.Пироговская, д.1" \
                and cellValue != "Пр-т Вернадского, 86" and cellValue != "Занятия по адресу:"\
                and cellValue != "…………………." and cellValue != "…………………" and cellValue != "……………………"\
                and cellValue != "………………………." and cellValue != "………………….." and cellValue != "……………………."\
                and cellValue != "……………………."  and cellValue != "………………………." and cellValue != "……………………….."\
                and cellValue != "…………………" and cellValue != "………………….." and cellValue != "…………………"\
                and cellValue != "………………" and cellValue != "……………….." and cellValue != "……………." \
                and cellValue != "…………….." \
                and cellValue != "В-86 - занятия в кампусе по адресу Проспекте Вернадского, д.86":
            if not cellValue and sheet[locCell.column + str(locCell.row-1)].value == "Военная\nподготовка":
                cellValue = "Военная\nподготовка"
            cellValue_List = cellValue.split('\n')
            if sheet.cell(column=locCell.col_idx + 1, row=locCell.row).value:
                typeO_List = sheet.cell(column=locCell.col_idx + 1, row=locCell.row).value.split('\n')
            if sheet.cell(column=locCell.col_idx + 2, row=locCell.row).value:
                teacher_List = sheet.cell(column=locCell.col_idx + 2, row=locCell.row).value.split('\n')
            if sheet.cell(column=locCell.col_idx + 3, row=locCell.row).value:
                room_List = str(sheet.cell(column=locCell.col_idx + 3, row=locCell.row).value).split('\n')

            valueParseArgs = [None, None, None, None]

            for i in range(len(cellValue_List)):
                valueParseArgs[0] = cellValue_List[i]

                if typeO_List:
                    if i < len(typeO_List):
                        valueParseArgs[1] = typeO_List[i]
                    elif i - 1 < len(typeO_List):
                        valueParseArgs[1] = "Вероятно " + typeO_List[i - 1]
                    else:
                        valueParseArgs[1] = "Вероятно " + typeO_List[len(typeO_List) - 1]

                if teacher_List:
                    if i < len(teacher_List):
                        valueParseArgs[2] = teacher_List[i]
                    elif i - 1 < len(teacher_List) and i > 0:
                        valueParseArgs[2] = "Вероятно " + teacher_List[i - 1]
                    else:
                        valueParseArgs[2] = "Вероятно " + teacher_List[len(teacher_List) - 1]

                if room_List:
                    if i < len(room_List):
                        valueParseArgs[3] = room_List[i]
                    elif i - 1 < len(room_List) and i > 0:
                        valueParseArgs[3] = "Вероятно " + room_List[i - 1]
                    else:
                        valueParseArgs[3] = "Вероятно " + room_List[len(room_List) - 1]
                if len(cellValue_List) == 1:
                    valueParseArgs[1] = ''.join(typeO_List)
                    valueParseArgs[2] = ''.join(teacher_List)
                    valueParseArgs[3] = ''.join(room_List)
                lessons.extend(valueParser(valueParseArgs[0],
                                           valueParseArgs[1],
                                           valueParseArgs[2],
                                           valueParseArgs[3],
                                           pairNum))
        return lessons
