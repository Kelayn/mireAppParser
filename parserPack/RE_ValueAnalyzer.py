# парсер значения
import re




def valueParser(cellValue, typeO, teacher, room, pairNum):

    numTmplt = re.compile('\d+\d*')
    # поиск "кр", выделение и вырезание подстроки "кр", список недель "кр"
    xcptTmplt = re.compile(r'\bкр[.]*\s*\d+\d*(?:\s*,\s*\d\d*\s*)*\s*[н]*[.]*\s*', re.I)  # Шаблон
    list1 = []
    if cellValue: list1 = (xcptTmplt.findall(cellValue))  # Список из подстроки
    xcptNums = []
    fromNum = None
    weeksNums = []
    if list1:
        xcptLen = (len(list1[0]))  # Длина подстроки
        cutPos = cellValue.find('кр')  # Позиция начала подстроки
        cellValue = cellValue[:cutPos] + cellValue[cutPos + xcptLen:]  # вырезание подстроки
        xcptNums = numTmplt.findall(list1[0])  # список "кр" недель

    # поиск "с", выделение и вырезание подстроки "с", список недель "с"
    fromTmplt = re.compile(r'\bс\s*\d+\d*\s*[н]+\s*[н]*[.]*\s*', re.I)  # Шаблон
    if cellValue: list1 = (fromTmplt.findall(cellValue))  # Список из подстроки
    if list1:
        fromLen = (len(list1[0]))  # Длина подстроки
        cutPos = cellValue.find('с')  # Позиция начала подстроки
        cellValue = cellValue[:cutPos] + cellValue[cutPos + fromLen:]  # вырезание подстроки
        fromNum = numTmplt.findall(list1[0][0])  # "с" неделя

    # поиск недель, выделение и вырезание, список недель
    weeksTmplt = re.compile(r'\d+\d*(?:\s*,\s*\d\d*)*\s*[н]*[.]*\s*', re.I)  # ТУТ НЕ БЫЛО [.]*
    if cellValue:
        list1 = (weeksTmplt.findall(cellValue))  # Список из подстроки
    if list1:
        weeksLen = (len(list1[0]))  # Длина подстроки
        cutPos = cellValue.find(list1[0][0])  # Позиция начала подстроки
        cellValue = cellValue[:cutPos] + cellValue[cutPos + weeksLen:]  # вырезание подстроки (ТУТ БЫЛО +1)
        weeksNums = numTmplt.findall(list1[0])  # Список недель

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
    lessonList = []

    if cellValue:
        lesson["lesson"] = cellValue
    if lesson["lesson"]:
        if xcptNums: lesson["except"] = xcptNums
        if fromNum: lesson["startsFrom"] = fromNum
        if weeksNums: lesson["periodical"] = weeksNums
    if typeO: lesson["type"] = typeO
    if teacher and teacher != "митхт" and teacher != "мгупи": lesson["teacher"] = teacher
    if room: lesson["room"] = room
    return lesson