# Обработчик пар
def pairHandler(cell):
    day = []
    if valueHandler(sheet[cell.column + str(cell.row)], 1):
        day.extend(valueHandler(sheet[cell.column + str(cell.row)], 1))
    if valueHandler(sheet[cell.column + str(cell.row + 2)], 2):
        day.extend(valueHandler(sheet[cell.column + str(cell.row + 2)], 2))
    if valueHandler(sheet[cell.column + str(cell.row + 4)], 3):
        day.extend(valueHandler(sheet[cell.column + str(cell.row + 4)], 3))
    if valueHandler(sheet[cell.column + str(cell.row + 6)], 4):
        day.extend(valueHandler(sheet[cell.column + str(cell.row + 6)], 4))
    if valueHandler(sheet[cell.column + str(cell.row + 8)], 5):
        day.extend(valueHandler(sheet[cell.column + str(cell.row + 8)], 5))
    if valueHandler(sheet[cell.column + str(cell.row + 10)], 6):
        day.extend(valueHandler(sheet[cell.column + str(cell.row + 10)], 6))
    return day


# Обработчик всей недели по четным и нечетным парам отдельно
def weekHandler(cell, num):
    cell.row += num  # Условие четности или нечестности пары
    days = {
        "Monday": pairHandler(sheet[cell.column + str(cell.row)]),
        "Tuesday": pairHandler(sheet[cell.column + str(cell.row + 12)]),
        "Wednesday": pairHandler(sheet[cell.column + str(cell.row + 24)]),
        "Thursday": pairHandler(sheet[cell.column + str(cell.row + 36)]),
        "Friday": pairHandler(sheet[cell.column + str(cell.row + 48)]),
        "Saturday": pairHandler(sheet[cell.column + str(cell.row + 60)])
    }
    return days
