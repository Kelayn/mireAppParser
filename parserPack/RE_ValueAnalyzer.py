# парсер значения
import re


def valueParser(cellValue, typeO, teacher, room, pairNum):
    xcptNums = []
    fromNum = None
    weeksNums = []
    lessonList = []
    list1 = []
    lesson = {
        "except": None,
        "startsFrom": None,
        "periodical": None,
        "lesson": None,
        "type": None,
        "teacher": None,
        "room": None,
        "pairNum": pairNum
    }
    astLesson = lesson.copy()
    longRow = False
    numTmplt = re.compile('\d+\d*')

    # поиск "кр", выделение и вырезание подстроки "кр", список недель "кр"
    xcptTmplt = re.compile(r'\bкр+(?:оме)*[.]*\s*\d+\d*(?:\s*,\s*\d\d*\s*)*\s*[н]*[.]*\s*', re.I)  # Шаблон
    if cellValue: list1 = (xcptTmplt.findall(cellValue))  # Список из подстроки
    for ind in range(2):
        if list1:
            if len(list1) == 1:
                if ind == 0:
                    xcptLen = (len(list1[0]))  # Длина подстроки
                    cutPos = cellValue.find('кр')  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + xcptLen:]  # вырезание подстроки
                    xcptNums = numTmplt.findall(list1[0])  # список "кр" недель
                    if xcptNums: lesson["except"] = xcptNums
            elif len(list1) == 2:
                longRow = True
                if ind == 0:
                    xcptLen = (len(list1[0]))  # Длина подстроки
                    cutPos = cellValue.find('кр')  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + xcptLen:]  # вырезание подстроки
                    xcptNums = numTmplt.findall(list1[0])  # список "кр" недель
                    if xcptNums: lesson["except"] = xcptNums
                if ind == 1:
                    xcptLen = (len(list1[1]))  # Длина подстроки
                    cutPos = cellValue.find('кр')  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + xcptLen:]  # вырезание подстроки
                    xcptNums = numTmplt.findall(list1[1])  # список "кр" недель
                    if xcptNums: astLesson["except"] = xcptNums

    # поиск "с", выделение и вырезание подстроки "с", список недель "с"
    fromTmplt = re.compile(r'\bс+\s*\d+\d*\s*[н]+\s*[н]*[.]*\s*', re.I)  # Шаблон
    if cellValue: list1 = (fromTmplt.findall(cellValue))  # Список из подстроки
    for ind in range(2):
        if list1:
            if len(list1) == 1:
                if ind == 0:
                    fromLen = (len(list1[0]))  # Длина подстроки
                    cutPos = cellValue.find('с')  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + fromLen:]  # вырезание подстроки
                    fromNum = numTmplt.findall(list1[0])[0]  # "с" неделя
                    if fromNum: lesson["startsFrom"] = fromNum
            if len(list1) == 2:
                longRow = True
                if ind == 0:
                    fromLen = (len(list1[0]))  # Длина подстроки
                    cutPos = cellValue.find('с')  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + fromLen:]  # вырезание подстроки
                    fromNum = numTmplt.findall(list1[0])[0]  # "с" неделя
                    if fromNum: lesson["startsFrom"] = fromNum
                if ind == 1:
                    fromLen = (len(list1[1]))  # Длина подстроки
                    cutPos = cellValue.find('с')  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + fromLen:]  # вырезание подстроки
                    fromNum2 = numTmplt.findall(list1[1][0])  # "с" неделя
                    if fromNum: astLesson["startsFrom"] = fromNum

    # поиск недель, выделение и вырезание, список недель
    cellValue1 = cellValue
    weeksTmplt = re.compile(r'\d+(?:\s*,\s*\d\d*)*\s*[н]*[.]*\s*', re.I)
    if cellValue: list1 = (weeksTmplt.findall(cellValue))  # Список из подстроки
    for ind in range(2):
        if list1 and (cellValue.find("3-D") == -1):
            if len(list1) == 1:
                if ind == 0 and list1[0] != "1 " and list1[0] != "2 ":
                    weeksLen = (len(list1[0]))  # Длина подстроки
                    cutPos = cellValue.find(list1[0][0])  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + weeksLen:]  # вырезание подстроки
                    weeksNums = numTmplt.findall(list1[0])  # Список недель
                    if weeksNums:   lesson["periodical"] = weeksNums
            if len(list1) == 2:
                if ind == 0 and list1[0] != "1 " and list1[0] != "2 ":
                    weeksLen = (len(list1[0]))  # Длина подстроки
                    cutPos = cellValue.find(list1[0])  # Позиция начала подстроки
                    endLen = cellValue.find(list1[1])
                    cellValue1 = cellValue[:cutPos] + cellValue[cutPos + weeksLen:endLen]
                    cellValue = cellValue[cellValue.find(list1[1]):]  # вырезанная первая подстрока
                    weeksNums = numTmplt.findall(list1[0])  # Список недель
                    if weeksNums: lesson["periodical"] = weeksNums
                if ind == 1 and list1[1] != "1 " and list1[1] != "2 ":
                    longRow = True
                    weeksLen = (len(list1[1]))  # Длина подстроки
                    cutPos = cellValue.find(list1[1][0])  # Позиция начала подстроки
                    cellValue = cellValue[:cutPos] + cellValue[cutPos + weeksLen:]  # вырезание подстроки (ТУТ БЫЛО +1)
                    weeksNums = numTmplt.findall(list1[1])  # Список недель
                    if weeksNums: astLesson["periodical"] = weeksNums

    if cellValue and not longRow:
        lesson["lesson"] = cellValue
    elif cellValue1 and longRow:
        lesson["lesson"] = cellValue1
        astLesson["lesson"] = cellValue

    for ind in range(2):
        if typeO:
            if (not astLesson["lesson"]) and ind == 0:
                lesson["type"] = typeO  # вместится любой вид предмета, если он один
            elif astLesson["lesson"]:
                if ind == 0:
                    if typeO.find(' ') != -1:
                        lesson["type"] = typeO[:typeO.find(' ')]
                    else:
                        lesson["type"] = "Вероятно " + typeO
                if ind == 1:
                    if typeO.rfind(' ') != -1:
                        astLesson["type"] = typeO[typeO.rfind(' '):]  # обработка на пр    лек (в случае,если нет табуляции)
                    else:
                        astLesson["type"] = "Вероятно " + typeO
        if teacher:
            if teacher != "митхт" and teacher != "мгупи":
                if not astLesson["lesson"]:
                    if ind == 0:
                        lesson["teacher"] = teacher
                elif astLesson["lesson"]:
                    if ind == 0: lesson["teacher"] = "Вероятно " + teacher
                    if ind == 1: astLesson["teacher"] = "Вероятно " + teacher  # если 2 предмета в строчку,\
                    #  а препод на 2й предмет
        if room:
            room = str(room)
            if not astLesson["lesson"]:
                if ind == 0:
                    lesson["room"] = room
            elif astLesson["lesson"]:
                if ind == 0:
                    lesson["room"] = room[:room.find('\n')+1] + ' ' + room[room.find("\n")+1:room.find(' ')]
                    # Ищет первый знак таубляции, чтобы добавить адрес кампуса (вопрос, а что если такого не будет?)
                    # Судя по поведению в консоли - "+1" не изменит вывод, при этом компенсирует случай,
                    # если такого не будет
                elif ind == 1:
                    astLesson["room"] = room[:room.find('\n')+1] + ' ' + room[room.rfind(' ')+1:len(room)]
    if astLesson["lesson"]:
        lessonList.append(astLesson)
    lessonList.append(lesson)
    return lessonList



