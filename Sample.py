# from googlesearch import search
#
#
# urls=[]
# for url in search("nitk",stop=10):
#     if "ac.in" or "edu.in" in str(url):
#         print(url)
#
import os
from doctotxt import processing
results = []


def filelistreader(path):
    # dir = os.listdir(os.path.join(path,dir))
    for file in os.listdir(path):
        # print (file)
        if file.endswith(".docx"):
            # print("DOCX file found : ", file)
            # docx2txtconv(os.path.join(path, file))
            results.append(processing(path,file))
        else:
            pass
            # print("WRONG file found : ", file)


src_path = input("Enter the source path : ")
filelistreader(src_path)

# print(results)
for ele in results:
    print(ele)
