import os
import io
os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe "yandex.ru/search/?text=сколько%20весит кит"')

file=open('adres_list_2.txt' , 'rt')
file2=open('flag_tags.txt','r')
line=""
lis=""
lis2=""
count=0

for line in file:
    lis2+=line
#print(lis)
full_list=lis.split('\n')
full_list2=lis2.split('\n')
k=0
flag_list=[]
adres_list=[]
tag_list=[]
list_of_lists=[]
"""while full_list[k]!= "end":
    list_of_lists=full_list[k].split('|')
    print(list_of_lists[3]) 
    flag_list.append(list_of_lists[3])
    k+=1"""
k=0
#print(full_list2)
while full_list2[k] !="end":
    [a,b,c]=full_list2[k].split('|')
    flag_list.append(a)
    adres_list.append(b)
    tag_list.append(c)
    k+=1
j=0
tags_list=[]
while j < k:
    tags_list.append(tag_list[j].split())
    j+=1
    #print(tags_list[j-1][0], "\n")
#comand=input("enter com ")
j=0
d=0
print(tags_list)
while j<k:
    c=0
    while c < len(tags_list[j]):
        #print(tag_list[j])
        if 'овер' == str(tags_list[j][c]):
            d=1
            break
        else: c+=1
    if d==1:break
    j+=1
    print(j,c,k)

print(flag_list[j])
print(adres_list[j])
print(tag_list[j])


