import os


def find_all_disk():
    curent_path="C:"+chr(92)+"Program Files"+chr(92)
    comand="fsutil fsinfo drives "+chr(62)+" "+curent_path+"disks.txt"
    print(comand)
    os.system(comand)
    path=curent_path+"disks.txt"
    print(path)
    find_file_txt=open(path,'r',encoding='cp866')
    full_find_file_list=get_full_list(find_file_txt)
    lists=full_find_file_list[1].split(':')
    k=1 # диски C ...
    count_disk=len(lists)
    disk=""
    
    while k<count_disk-2:
        #print(lists[k][len(lists[k])-1])
        disk=disk+lists[k][len(lists[k])-1]+":"
        k=k+1
    #print(disk)
    find_file_txt.close()
    return(disk)


def get_full_list(file):
    com_list=""
    for line in file:
        com_list+=line # adr_list - list with adress of programm
    com_list=com_list.split('\n')
    return com_list


print(find_all_disk())
