import os
import webbrowser
import re
import time

def find_files(file_name, search_path):
    d=[]
    #a="chcp 65001 & "
    b=search_path
    c=" & dir /b/s "
    d=file_name
    g=chr(62)
    e=" "+g+" E:"+chr(92)+"helper"+chr(92)+"abc.txt"
    f=b+c+d+e
    #find= disk+" &"+" dir /b/s " + file_name
    #os.system(f
    print(f)
    find_file_txt=open('ABS.txt','r',encoding='cp866')
    full_find_file_list=get_full_comand_list(find_file_txt)
    print(full_find_file_list)
    find_file_txt.close()
    #os.system("chcp 855 & D: & dir /b/s 1.1.mp4 >> C:\User\Cergol\Desktop\helper\abc.txt")
    #f = open("abc.txt", "r", encoding="utf-8")
    #print(f.read())
    #print(str(os.system(find)))
    
def get_full_comand_list(file):
    com_list=""
    for line in file:
        com_list+=line # adr_list - list with adress of programm
        print(line)
    com_list=com_list.split('\n')
    return com_list

b="D:"
c=" & dir /b/s "
d="шапка.png"
g=chr(62)+chr(62)
e=" "+g+" C:"+chr(92)+"Users"+chr(92)+"Cergol"+chr(92)+"Desktop"+chr(92)+"abc.txt"
f=b+c+d+e
os.system(f)
"""
disk="D"
disk=disk+":"

find_file="шапка.png"
count_find_files=len(find_file)
text_to_say="я нашла "+str(count_find_files)+" файлов\n"
print(text_to_say)
#find_files(find_file,disk)
g=chr(62)
e=" "+g+" E:"+chr(92)+"helper"+chr(92)+"disks.txt"
f="fsutil fsinfo drives"+e
print(f)
print(os.system(f))
find_file_txt=open('disks.txt','r',encoding='cp866')
full_find_file_list=get_full_comand_list(find_file_txt)
#print(full_find_file_list)
lists=full_find_file_list[1].split(':')
l=len(lists)
k=2
while k<l-2:
    print(lists[k][2])
    k=k+1
"""

