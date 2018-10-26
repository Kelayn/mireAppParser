from openpyxl import load_workbook

wb = load_workbook("C:/Users/Kelayn/PycharmProjects/mireAppParser/Test/_schedule/main/FTI_Stromynka-4-kurs-1-sem.xlsx")
sheet = wb.worksheets[0];
testStr = sheet['BH29'].value
cellValue_List = testStr.split('\n')
testStr = sheet["BI29"].value
typeO_List = testStr.split('\n')
testStr = sheet['BJ29'].value
teacher_List = testStr.split('\n')
testStr = str(sheet['BK29'].value)
room_List = testStr.split('\n')

valueParseArgs = [None, None, None, None]

# for item in list1:
for i in range(len(cellValue_List)):
    valueParseArgs[0] = cellValue_List[1]
    if i < len(typeO_List):
        valueParseArgs[1] = typeO_List[i]
    elif i-1 < len(typeO_List):
        valueParseArgs[1] = "Вероятно " + typeO_List[i - 1]
    else:
        valueParseArgs[1] = "Вероятно " + typeO_List[len(typeO_List)-1]

    if i < len(teacher_List):
        valueParseArgs[2] = teacher_List[i]
    elif i - 1 < len(teacher_List):
        valueParseArgs[2] = "Вероятно " + teacher_List[i - 1]
    else:
        valueParseArgs[2] = "Вероятно " + teacher_List[len(teacher_List)-1]

    if i < len(room_List):
        valueParseArgs[3] = room_List[i]
    elif i - 1 < len(room_List):
        valueParseArgs[3] = "Вероятно " + room_List[i - 1]
    else:
        valueParseArgs[3] = "Вероятно " + room_List[len(room_List)-1]

    print(valueParseArgs)

#print(cv_List)

            i