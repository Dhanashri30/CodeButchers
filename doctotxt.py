import docx2txt
from globalVariables import BDegree
from globalVariables import MDegree
import re
import os
from qwerty import samelinechecker

text = docx2txt.process("/Users/hiteshjain/Downloads/untitled4/Android_Developer.docx")


def isContainsIT(collegename):
 x = re.search("^.+IT$", collegename)
 if (x):
   return True
 else:
   return False

def isContainsTU(collegename):
 x = re.search("^.+TU$", collegename)
 if (x):
   return True
 else:
   return False


def processing(path,fileName):
    text = docx2txt.process(os.path.join(path, fileName))
    content = []
    result = []
    for line in text.splitlines():
        # This will ignore empty/blank lines.
        if line != '':
            # Append to list
            content.append(line)

    length = len(content)
    result = []
    text = 0
    bachelors = ""
    master = ""
    check = False

    while text < length:
        if ("engineering" in content[text].lower() and "college" in content[text].lower()) or \
                ("engg" in content[text].lower() and "college" in content[text].lower()) or \
                ("institute" in content[text].lower() and "technology" in content[text].lower()) or \
                (("board / university" not in content[text].lower()) and ("university" in content[text].lower())) or \
                (isContainsIT(content[text])) or \
                ("university" in content[text].lower() and "board" not in content[text].lower()) or \
                (isContainsTU(content[text])) or \
                ("college of" in content[text].lower()):

            temp1 = text
            count = 0
            while (count < 5):
                content[temp1] = content[temp1].replace("CS","")
                content[temp1] = content[temp1].replace("IT","")
                content[temp1] = content[temp1].replace("computer science","")
                content[temp1] = content[temp1].replace("information technology","")
                content[temp1] = content[temp1].replace("Computer science engineering","")
                temp2 = ''.join(e for e in content[temp1] if e.isalnum())
                if temp2.lower() in MDegree:
                    check = True
                    master = master + content[temp1] + " "
                    master = master + content[text]
                if temp2.lower() in BDegree:
                    check = True
                    bachelors = bachelors + content[temp1] + " "
                    bachelors = bachelors + content[text]
                temp1 = temp1 - 1
                count = count + 1
            temp1 = text
            count = 0
            while (count < 5):
                temp2 = ''.join(e for e in content[temp1] if e.isalnum())
                if temp2.lower() in MDegree and check == False:
                    master = master + content[temp1] + " "
                    master = master + content[text]
                if temp2.lower() in BDegree and check == False:
                    bachelors = bachelors + content[temp1] + " "
                    bachelors = bachelors + content[text]
                temp1 = temp1 + 1
                count = count + 1
            if len(master) == 0 and len(bachelors) == 0 :
                # check in same line
                # print(content[text])
                degree , collegename = samelinechecker(content[text])
                master = master + degree + " " + collegename + " "


        text = text + 1

    # print(master + "\n" + bachelors)
    result.append(fileName)
    result.append(master)
    result.append(bachelors)

    return result


    # print(globalVariables.BDegree)