import myjson
import json
import os


def uploadJson():
    dict = {}
    listOfFiles = os.listdir("C:\Test\json")
    print(listOfFiles)
    jsonTmp = "C:\Test\json\\"
    coef = 100/len(listOfFiles)
    summ = 0
    for file in listOfFiles:
        summ += coef
        print(file + ' ' + str(summ) + '%')
        with open(jsonTmp+file, "r") as rf:
            js = json.load(rf)
            url = myjson.store(json.dumps(js))
            dict[file[:10]] = url
    with open("C:\Test\json\JSONDICT.json", "w") as jD:
        json.dump(dict, jD, ensure_ascii=False)
