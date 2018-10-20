from parserPack.cellValueAnalyzer import valueHandler

# Обработчик пар
def usualPairHandler(sheet, cell):
    day = []
    for i in range(0, 12, 2):
        lesson = valueHandler(sheet, sheet[cell.column + str(cell.row+i)], (i+2)/2)
        if lesson:
            day.extend(lesson)
    return day


# Обработчик всей недели по четным и нечетным парам отдельно
def usualWeekHandler(sheet, cell, num):
    cell.row += num  # Условие четности или нечестности пары
    days = {
        "Monday": usualPairHandler(sheet, sheet[cell.column + str(cell.row)]),
        "Tuesday": usualPairHandler(sheet, sheet[cell.column + str(cell.row + 12)]),
        "Wednesday": usualPairHandler(sheet, sheet[cell.column + str(cell.row + 24)]),
        "Thursday": usualPairHandler(sheet, sheet[cell.column + str(cell.row + 36)]),
        "Friday": usualPairHandler(sheet, sheet[cell.column + str(cell.row + 48)]),
        "Saturday": usualPairHandler(sheet, sheet[cell.column + str(cell.row + 60)])
    }
    return days

# добавить алгоритмы прохода по вечеркам и маге
# ...
