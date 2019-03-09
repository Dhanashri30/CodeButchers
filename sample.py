import os
import re
import sys
import app
import PyPDF2
import docx2txt

htmlBody = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.1//EN\" \"http://www" \
           + ".w3.org/TR/xhtml11/DTD/xhtml11.dtd\">\n" \
           + "<html xmlns=\"http://www.w3.org/1999/xhtml\">\n" \
           + "<head>\n" \
           + "<title>Resume Screening Report</title>\n" \
           + "<style type=\"text/css\">\n" \
           + "table {margin-bottom:10px;border-collapse:collapse;empty-cells:show}\n" \
           + "td,th {border:1px solid #009;padding:.25em .5em}\n" \
           + ".result th {vertical-align:bottom}\n" \
           + ".param th {padding-left:1em;padding-right:1em}\n" \
           + ".param td {padding-left:.5em;padding-right:2em}\n" \
           + ".stripe td,.stripe th {background-color: #E6EBF9}\n" \
           + ".numi,.numi_attn {text-align:right}\n" \
           + ".total td {font-weight:bold}\n" \
           + ".passedodd td {background-color: #00e600}\n" \
           + ".passedeven td {background-color: #80ff80}\n" \
           + ".skippedodd td {background-color: #CCC}\n" \
           + ".skippedodd td {background-color: #DDD}\n" \
           + ".failedodd td,.numi_attn {background-color:  #ffb3b3}\n" \
           + ".failedeven td,.stripe .numi_attn {background-color: #ff8080}\n" \
           + ".stacktrace {white-space:pre;font-family:monospace}\n" \
           + ".totop {font-size:85%;text-align:center;border-bottom:2px solid #000}\n" \
           + "body {background-color: #cccccc99;}\n" \
           + "rect {fill-opacity: 0.0;}\n" \
           + "</style>\n" \
           + "</head>\n" \
           + "<body>\n" \
           + "<center>\n" \
           + "<h1>Scan Report</h1>\n" \
           + "</center>\n" \
           + "<center><table cellspacing=\"0\" cellpadding=\"0\" class=\"testOverview\" " \
           + "style=\"margin-bottom: 10px;border-collapse: collapse;empty-cells: show;\">\n" \
           + "<tr>\n" \
           + "<th style=\"border: 1px solid #009;padding: .25em .5em;\">Filename</th>\n" \
           + "<th style=\"border: 1px solid #009;padding: .25em .5em;\">Skill Score</th>\n" \
           + "<th style=\"border: 1px solid #009;padding: .25em .5em;\">Total Score</th>\n" \
           + "</tr>\n" \
           + "{html_report}" \
           + "</table>\n" \
           + "</center>\n" \
           + "</body>\n" \
           + "</html>"

htmlPart = "<tr>\n" \
           + "<td style=\"text-align: left;padding-right: 2em;border: 1px solid #009;padding: .25em " \
           + ".5em;\"><b>{file_Name}</b></td>\n" \
           + "<td class=\"numi\" style=\"border: 1px solid #009;padding: .25em .5em;text-align: right;" \
           + "\">{skill_Score}</td>\n" \
           + "<td class=\"numi\" style=\"border: 1px solid #009;padding: .25em .5em;text-align: right;" \
           + "\">{total_score}</td>\n" \
           + "</tr>"

total_file_count = 0
filename_list = []
score_list = []

# fileName = [ "1", "2", "3", "rcvhbj", "cvhm", "xcvbj" ]
# educationCriteria = [ "pass", "fail", "pass", "pass", "fail", "pass" ]
# collegeTierScore = [ 10, 5, 10, 10, 5, 10 ]
# skillScore = [ 8, 4, 6, 10, 5, 10 ]
# totalScore = [ 9, 4.5, 8, 10, 5, 10 ]
path = "/Users/manidharmulagapaka/PycharmProjects/untitled3/Resume"
def filelistreader():
    # dir = os.listdir(os.path.join(path,dir))
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            print("PDF file found : ", file)
            pdf2txtconv(os.path.join(path, file))
        elif file.endswith(".docx"):
            print("DOCX file found : ", file)
            docx2txtconv(os.path.join(path, file))
        else:
            print("WRONG file found : ", file)


def pdf2txtconv(location):
    global total_file_count
    global filename_list

    head, tail = os.path.split(location)
    # creating a pdf file object
    # pdfFileObj = open('Jeena_Curriculum_Vitae.pdf', 'rb')
    pdfFileObj = open(location, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)

    # extracting text from page
    # print(pageObj.extractText())

    str_to_execute = 'touch ' + os.path.splitext(tail)[0]
    new_filename = os.path.splitext(tail)[0] + '.txt'
    filename_list.append(new_filename)
    total_file_count += 1
    os.system(str_to_execute)

    with open(new_filename, 'w') as fp1:
        for line in pageObj.extractText():
            fp1.write(line)

    # closing the pdf file object
    pdfFileObj.close()


def docx2txtconv(location):
    global total_file_count
    global filename_list

    head, tail = os.path.split(location)
    my_text = docx2txt.process(tail)
    str_to_execute = 'touch ' + os.path.splitext(tail)[0]
    new_filename = os.path.splitext(tail)[0] + '.txt'
    filename_list.append(new_filename)
    total_file_count += 1
    os.system(str_to_execute)

    with open(new_filename, 'w') as fp2:
        for line in my_text:
            fp2.write(line)

    # print(my_text)


'''
def raw_string(s):
    if isinstance(s, str):
        s = s.encode('string-escape')
    elif isinstance(s, unicode):
        s = s.encode('unicode-escape')
    return s
'''


def keyword_matcher():
    global total_file_count
    global filename_list
    global score_list

    temp_score = 0

    # take input of keywords
    primary_skill_keyword_list = "java"
    secondary_skill_keyword_list = "c"
    # experience_keyword_list = input ("Enter the experience separated by commas : ")

    primary_skill_keyword_list = primary_skill_keyword_list.split(",")
    secondary_skill_keyword_list = secondary_skill_keyword_list.split(",")

    primary_keyword_dict = {}.fromkeys(primary_skill_keyword_list, 0)
    secondary_keyword_dict = {}.fromkeys(secondary_skill_keyword_list, 0)

    print ("Initial Primary keyword has table is :", primary_keyword_dict)
    print ("Initial Secondary keyword has table is :", secondary_keyword_dict)

    # scanning starts
    for fileindex in range(0, total_file_count):
        print("Starting for filename: ", filename_list[fileindex])
        with open(filename_list[fileindex], 'r') as fp:
            for line in fp:
                # primary key search
                for key in primary_keyword_dict:
                    p_searchObj = re.search(key, line, re.M | re.I)
                    if p_searchObj:
                        # print ("search --> searchObj.group() : ", searchObj.group())
                        primary_keyword_dict[key] += 1

                # secondary key search
                for key in secondary_keyword_dict:
                    s_searchObj = re.search(key, line, re.M | re.I)
                    if s_searchObj:
                        # print ("search --> searchObj.group() : ", searchObj.group())
                        secondary_keyword_dict[key] += 1

        for key in primary_keyword_dict:
            temp_score += int(primary_keyword_dict[key]) * 10

        for key in secondary_keyword_dict:
            temp_score += int(secondary_keyword_dict[key]) * 5

        score_list.append(temp_score)
        temp_score = 0

        print ("********** After", fileindex + 1, " no. search on ", filename_list[fileindex], " keyword table is :",
               primary_keyword_dict, "*********", secondary_keyword_dict, " & Score is :", score_list[fileindex])

        # for initialization to be used for next loop
        for key in primary_keyword_dict:
            primary_keyword_dict[key] = 0

        for key in secondary_keyword_dict:
            secondary_keyword_dict[key] = 0


#   return score


# def filterResults():
#     for i in range(0, total_file_count):
#         if educationCriteria[i] == "fail":
#             del fileName[i]
#             del collegeTierScore[i]
#             del skillScore[i]
#             del totalScore[i]


def writeHTMLFile(data):
    f = open("resume_report.html", "w")
    f.write(htmlBody)


def report_generate():
    global htmlBody
    # function to generate report
    html = ""
    # csvData = [['Filename' , 'Skill Score' , 'Total Score']]
    # filterResults()
    for i in range(0, total_file_count):
        test = htmlPart.replace('{file_Name}', filename_list[i])
        test = test.replace('{skill_Score}', str(score_list[i]))
        test = test.replace('{total_score}', str(score_list[i]))
        html = html + test
        list1 = []
        list1.append(filename_list[i])
        list1.append(str(score_list[i]))
        list1.append(str(score_list[i]))

    # print (htmlBody)
    # csvData.append(list1)
    # print csvData

    htmlBody = htmlBody.replace("{html_report}", html);

    writeHTMLFile(htmlBody)


# writeCSVFile(csvData)


# if __name__ == "__main__":
    # the main thread is here
    # /Users/niladrisekharpandit/PycharmProjects/pdfreader/venv
if __name__ == "__main__":
    print("The path to look for Resumes is: ")
    filelistreader()
    keyword_matcher()
    report_generate()

    # run the generated report file
    os.system("open -a \"Google Chrome\" resume_report.html ")



