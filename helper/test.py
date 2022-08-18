import os
import sys
import webbrowser
from gtts import gTTS
import random
import time
import playsound
import glob
import winsound
import speech_recognition as sr

#may delete endings

"""__________________________________________________________"""

def close_target(target_flag,adres_list,flag_list):
    k=0
    while target_flag!=flag_list[k]:
        k+=1
    close_comand="TASKKILL /F /IM " + adres_list[k]
    os.system(close_comand)

"""__________________________________________________________"""


def comand_list(mute,ps): #com_flag - flag from function comand_type
    
    say_text("неверная команда. вам показать список команд?",mute)
    yn = listen_command() #yn - yes or no char type
    if (yn[0] == "y") or (yn[0] == "д"):
        os.startfile(r'comand_list.txt')  #open_target("n") #need to add target_list.txt
    else: say_text("как хотите, но команда все равно не верная",mute)

"""__________________________________________________________"""
def comand_target(string,flag,tag):

    tof=0
    i=0
    rez=""
    while i < len(tag):
        c=0
        while c < len(tag[i]):
            if str(tag[i][c]) in string:
                tof=1
                break
            else: c+=1
        if tof == 1:break
        else : i+=1
    if tof==0:rez= "no"
    else: rez=flag[i]
    return rez


"""__________________________________________________________"""
def comand_type(string, flag,tag):

    tof=0     # tof=true or false
    i=0
    while i < len(tag):
        c=0
        while c < len(tag[i]):
            if str(tag[i][c]) in string:
                tof=1
                break
            else: c+=1
        if tof == 1: break
        else :i+=1
    if tof == 0: rezult= "no"
    else: rezult=flag[i]

    return rezult

"""__________________________________________________________"""


##сюда очистку файлов, которая снизу
def delete_find_file():
    #path=" E:"+chr(92)+"helper"+chr(92)+""
    comand="del abc.txt" #очистка ее в отдельную функицю
    os.system(comand)

"""__________________________________________________________"""

def find_files(file_name, search_path,mute):
    delete_find_file()
    global curent_path
    #curent_path=curent_path[0:2]
    #print(curent_path)
    disks=find_all_disk()
    disks=disks.split(':')
    count_disk=len(disks)
    if search_path == "all":
        
        k=0
        while k<count_disk-1:
            #print(lists[k][len(lists[k])-1])
            #disk=lists[k][len(lists[k])-1]+":"
            #k=k+1
            consloe_comand=" & dir /b/s "
            disk=disks[k]+":"
            k=k+1
            f=disk+consloe_comand+file_name+" "+chr(62)+chr(62)+" "+curent_path+"abc.txt"
            os.system(f)
        return(1)

    else:
        k=0
        count=0
        while k<count_disk-1:
            if disks[k] in search_path:
                count=1
            k=k+1
        if count==1:
            consloe_comand=" & dir /b/s "
            f=search_path+consloe_comand+file_name+" "+chr(62)+" "+curent_path+"abc.txt"
            os.system(f)
            return(1)
        else:
            say_text("введеный вами диск отсутствует или поиск на нем не возможен",mute)
            return(0)
   

"""__________________________________________________________"""

def find_all_disk():
    comand="fsutil fsinfo drives "+chr(62)+" "+curent_path+"disks.txt"
    os.system(comand)
    find_file_txt=open('disks.txt','r',encoding='cp866')
    full_find_file_list=get_full_comand_list(find_file_txt)
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
    
"""__________________________________________________________"""

def get_adres_flag_list(adr_list):
    flag_list=[]
    k=0
    while adr_list[k]!= "end":
        [a,b,c]=adr_list[k].split('|')
        flag_list.append(a)
        k+=1
    return flag_list

"""__________________________________________________________"""
def get_adres_list(adr_list):
    
    adres_list=[]
    k=0
    while adr_list[k]!= "end":  #adres_list - list of adress and flag_list= list of flags
        [a,b,c]=adr_list[k].split('|')
        adres_list.append(b)
        k+=1
       
    return adres_list

"""__________________________________________________________"""
def get_adres_tag_list(adr_list):
    tag_list=[]
    k=0
    while adr_list[k]!= "end":
        [a,b,c]=adr_list[k].split('|')
        tag_list.append(c.split())
        k+=1
    return tag_list    

"""__________________________________________________________"""
def get_comand_flag_list(com_list):
    flag_list=[]
    k=0
    while com_list[k]!="end":
        [a,b]=com_list[k].split('|')
        flag_list.append(a)
        k+=1
    return flag_list

"""__________________________________________________________"""

def get_comand_tag_list(com_list):
    tag_list=[]
    k=0
    while com_list[k]!="end":
        [a,b]=com_list[k].split('|')
        #print(a)
        tag_list.append(b.split())
        k+=1
    return tag_list

"""__________________________________________________________"""

def get_equation(string):
    num_space=string.index(" ")
    equation=string[num_space:len(string)]
    rez=0
            
    if ("+" in equation):
        
        [a,b]=equation.split("+")
        rez=int(a)+int(b)
        
    elif ("-" in equation):
        
        [a,b]=equation.split("-")
        rez=int(a)-int(b)
        
    elif ("x" in equation):
        
        [a,b]=equation.split("x")
        rez=int(a)*int(b)
        
    elif ("/" in equation):
        
        [a,b]=equation.split("/")
        rez=int(a)/int(b)
        
    elif ("возвести в" in equation):
        
        [a,b]=equation.split("возвести в")
        rez=int(a)**int(b)
        
    else:
        
        say_text("неверное выражение", mute)
   
    return rez      

"""__________________________________________________________"""
def get_full_adres_list(file):
    adr_list=""
    for line in file:
        adr_list+=line # adr_list - list with adress of programm
    adr_list=adr_list.split('\n')
    return adr_list

"""__________________________________________________________"""

def get_full_comand_list(file):
    com_list=""
    for line in file:
        com_list+=line # adr_list - list with adress of programm
    com_list=com_list.split('\n')
    return com_list

"""__________________________________________________________"""

def listen_command():
    # obtain audio from the microphone
    
    global print_speach 
    if print_speach =="speach":
        r = sr.Recognizer()
        our_speech=""
        with sr.Microphone() as source:
         
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            our_speech = r.recognize_google(audio, language="ru")
            our_speech=our_speech.lower()
            print("Вы сказали: "+our_speech)
            return our_speech
        except sr.UnknownValueError:
            #say_text("Ошибка")
            return "ошибка"
        except sr.RequestError:
            #say_text("Ошибка")
            return "ошибка"
    else: return(input())
    #return input("Скажите вашу команду: ")

"""__________________________________________________________"""

def make_true_file_name(file_name):
    if ("звёздочка" in file_name) or ("*" in file_name):
        file_name="*"
    elif " " in file_name:
        while " " in file_name:
            num=file_name.index(' ')
            file_name=file_name[0:num]+file_name[num+1:len(file_name)]
    #print(file_name)
    return(file_name)
        

"""__________________________________________________________"""
def open_find_files(file_path,numb_file):
    open_file=file_path[numb_file-1]
    #print(file_path[numb_file-1])
    os.startfile(open_file)

"""__________________________________________________________"""
def open_target(target_flag,adres_list,flag_list):
    k=0
    while target_flag!=flag_list[k]:
        k+=1
    os.startfile(adres_list[k])

"""__________________________________________________________"""
def say_text(text,mute):
    if mute == 0:
        voice = gTTS(text, lang="ru")
        file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
        voice.save(file_voice_name)
        playsound.playsound(file_voice_name)
    print("Голосовой ассистент: "+text)

"""__________________________________________________________"""
def search_in_internet(search_str):
        domen = ["com","ru","net","info","io"]
        const_str="https://yandex.ru/search/?lr=2&text="
        last_dot=search_str.rfind('.')
        last_dot+=1
        help_str=search_str.replace(' ','%20')
        i=0
        rez=0
        final_search_str=const_str+help_str
        if last_dot != -1:
            while i!= len(domen):
                if search_str[last_dot:len(search_str)]==domen[i]:
                    rez=1
                i+=1
            if rez==1:   
                final_search_str=search_str
           
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab(final_search_str)


"""__________________________________________________________"""
def select_type_of_file(string,tag,flag):
    k=0
    while string!=tag[k]:
        k+=1
    return flag[k]

"""__________________________________________________________"""

def time_for_timer(string, mute):
    inf=32000
    digit_list=""
    digit=[]
    k=0
    co=0
    while k <len(string):
        while string[k].isdigit():
            digit_list=digit_list+string[k]
            k=k+1
            if k == (len(string)-1):
                string=string+"." 
        if len(digit_list)!=0:
            if (digit_list[len(digit_list)-1]!=";"):
                digit_list=digit_list+";"
        k=k+1

    sum_h=0
    sum_m=0
    sum_c=0

    num_h=c_string.find('час')
    num_m=c_string.find('мин')  
    num_c=c_string.find('сек')
    digit=digit_list.split(";")
    digit.pop()
    mas=[[num_h,num_m,num_c],[3600,60,1]]

    j=0
    while j<len(mas[0]):
        if mas[0][j] == (-1):
            mas[0][j]=inf
        j=j+1

    j=0
    while j<len(mas[0]):
        k=1
        while k <len(mas[0]):
            if mas[0][k-1] > mas[0][k]:
                d=mas[0][k-1]
                mas[0][k-1]=mas[0][k]
                mas[0][k]=d
                w=mas[1][k-1]
                mas[1][k-1]=mas[1][k]
                mas[1][k]=w
            k=k+1
        j=j+1
    summ=0
    k=0
    str_to_say="ваш таймер на "
    while k <len(digit):
        if mas[0][k]!= inf:
            str_to_say=str_to_say+digit[k]
            if mas[1][k] == 3600:
                str_to_say=str_to_say+" часов "
            elif mas[1][k] == 60:
                str_to_say=str_to_say+" минут "
            else:
                str_to_say=str_to_say+" секунд "
            summ=summ+int(digit[k])*mas[1][k]
        k=k+1
    str_to_say=str_to_say+"заведен"
    say_text(str_to_say,mute)
    return(summ)
"""__________________________________________________________"""

def timer_file(time_start_list, timer_time_list):
    t_file=open('timer_list.txt','a')
    last=len(time_start_list)-1
    #print(time_start_list[last])
    #print(timer_time_list[last])
    s=str(time_start_list[last])+"|"+str(timer_time_list[last])+'\n'
    t_file.write(s)
    t_file.close()

"""__________________________________________________________"""

def target_list(string, com_flag,mute): #com_flag - flag from function comand_type
    yn="n"
    say_text("неверная цель. показать вам список целей?",mute) #ОЗВУЧИТЬ!!
    yn = listen_command() #yn - yes or no char type
    #if (com_flag == "o"): # may be need some else flag (to close ...)
        #yn - yes or no char type
    if (com_flag == "ca") or (com_flag == "ca_r"):
        say_text("u must enter number + (-*/^) number",mute)
    if (yn[0] == "y") or (yn[0] == "д"):
        os.startfile(r'adres_list.txt')  #open_target("n") #need to add target_list.txt
    else: say_text("как хотите, но цель все равно не верная",mute)



"""__________________________________________________________"""

def write_note(ps):
    mess = "\n"
    
    while not("конец заметки" in mess):
        mess=mess+""+listen_command()
    note_file=open('note.txt','a')
    mess=mess[0:len(mess)-len("конец заметки")-1]
    note_file.write(mess)
    note_file.close()
    
    
"""__________________________________________________________"""

def init_files():

    path_to_disk="C:"+chr(92)+"Users"+chr(92)+"Cergol"+chr(92)+"Desktop"+chr(92)+"disks.txt"
    disk_list="fsutil fsinfo drives "+chr(62)+" "+path_to_disk # 62 = '>'  92 = '\'
    os.system(disk_list)
    disk_file_txt=open(path_to_disk,'r',encoding='cp866')
    full_disk_file_list=get_full_comand_list(disk_file_txt)
    disk_file_txt.close()
    lists=full_disk_file_list[1].split(':')
    disk_count=len(lists)
    k=1
    file_name=[]
    while k<disk_count-2:
        disk=lists[k][2]+":"
        k=k+1
        comand=" & dir /b/s "
        path=" "+chr(62)+chr(62)+" C:"+chr(92)+"Users"+chr(92)+"Cergol"+chr(92)+"Desktop"+chr(92)+"needs_file.txt"
        full_comand=disk+comand+file_name+path
        os.system(full_comand)
    
    

"""__________________________________________________________"""
def split_path(ful_path):
    path=ful_path.split(' ')
    k=0
    true_path=''
    #print(path)
    while k <len(path):
        if path[k] != '':
            true_path=true_path+path[k]+chr(92)
        k=k+1
    return(true_path)


"""__________________________________________________________"""

def make_true_disk(disk):
    disk=disk.lower()
    if (disk[0] == "д") or (disk[0] == "d"):
        disk="D:"
                
    elif (disk[0] == "e") or (disk[0] == "ф")or (disk[0] == "е"): #first e - eng, second e - ru
        disk="E:"

    elif (disk[0] == "ц") or (disk[0] == "c")or (disk[0] == "с"):#first c - eng, second c - ru
        disk="C:"

    elif (disk[0] == "г") or (disk[0] == "g"):
        disk="G:"
           
    elif ("все" in disk):
        disk="all"
                
    else:
        say_text("таких дисков я не знаю", mute)
        disk="fail"
    return(disk)
                        
"""__________________________________________________________"""
 
# main parth
adres_file=open('adres_list.txt','r')
comand_file=open('comand_list.txt','r')
close_file=open('close_adres.txt','r')
types_file=open('file_types.txt','r',encoding='cp65001')
start_param_file=open('start_param.txt','r',encoding='cp65001')
#start_param_file=open('probe.txt','r',encoding='cp65001')



answer_options=['слушаю вас','дада я','уже тут','не томите','чё нада','ну я тут','сегодня пятница улица развратница пацы крутяться тёлочки мутяться','чего тебе','ну сколько можно']

len_a_o=len(answer_options)
full_comand_list=get_full_comand_list(comand_file)
comand_flag_list=get_comand_flag_list(full_comand_list)
comand_tag_list=get_comand_tag_list(full_comand_list)

full_adres_list=get_full_adres_list(adres_file)
adres_list=get_adres_list(full_adres_list)
adres_tag_list=get_adres_tag_list(full_adres_list)
adres_flag_list=get_adres_flag_list(full_adres_list)

full_close_adres_list=get_full_adres_list(close_file)
close_adres=get_adres_list(full_close_adres_list)
close_adres_tag_list=get_adres_tag_list(full_close_adres_list)
close_adres_flag_list=get_adres_flag_list(full_close_adres_list)

full_types_list=get_full_adres_list(types_file)
types_tag_list=get_comand_tag_list(full_types_list)
types_flag_list=get_comand_flag_list(full_types_list)

full_start_param_file=get_full_comand_list(start_param_file)
start_param_file.close()

curent_path_for_file=full_start_param_file[0]
curent_path=split_path(full_start_param_file[0])
yes_no=int(full_start_param_file[1])
mute=int(full_start_param_file[2])
print_speach =full_start_param_file[3]

sound_files_path=curent_path+"*.mp3"
sound_files = glob.glob(sound_files_path)
c_string = "ф"
c_type = "no"
equation=0

timer_list=[]
timer_start_list=[]
cur_time=time.time()
#timer_list.append(cur_time)
#print(len(timer_start_list))

#find_files("шапка.png","all")
#find_all_disk()
#start param

while c_type != "e":
    
    winsound.Beep(2500,200)
    
    while not("пятница" in c_string):
        k=0
        while k < len(timer_start_list):
            
            if time.time()-int(timer_start_list[k])>int(timer_list[k]): 
                d=0
                for d in range(4):  
                    winsound.Beep(8000,1000)
                time_out="ваш таймер на "
                hours=int(timer_list[k])//3600
                minut=(int(timer_list[k])%3600)//60
                sec=int(timer_list[k])%60
                if hours != 0:
                    time_out=time_out+str(hours)+ " часов "
                if minut != 0:
                    time_out=time_out+str(minut)+ " минут "
                time_out=time_out+str(sec)+ " секунд "
                time_out=time_out+" окончен"
                say_text(time_out,mute)
                timer_start_list.pop(k)
                timer_list.pop(k)
               
            k=k+1
        c_string = listen_command()
    say_text(answer_options[random.randint(0,len_a_o-1)],mute)
    c_string = listen_command()
    
    if yes_no == 1:
        say_text("вы уверены, что хотите выполнить следующую команду?",mute)
        say_text(c_string,mute)
        agree=listen_command()
        
        if agree[0] == "д":
            say_text("ок, выполняю",mute)
        else: continue
        
    c_string=c_string.strip(' ')
    c_type =comand_type(c_string,comand_flag_list,comand_tag_list)
    #print(c_string[2])
    if c_type == "no":
        comand_list(mute,print_speach)
        continue

    elif c_type == "e":
        say_text("Ушла спать",mute)
        adres_file.close()
        comand_file.close()
        close_file.close()
        types_file.close()
        for f in sound_files:
            try:
                os.remove(f)
            except OSError as e:
                print("Ошибка: %s : %s" % (f, e.strerror))
                sys.exit()
        
    elif c_type == "f":

        space_count=c_string.count(' ')
        
        if space_count !=0:
            first_space=c_string.find(' ')
            search_str=c_string[first_space:len(c_string)]
            if yes_no:
                ful_search_str = "вы хотите найти это? " + search_str
                say_text(ful_search_str,mute)
                yn=listen_command()
                #print(yn[0])
                if (yn[0] != "y") and (yn[0] != "д"):
                    say_text("введите запрос",mute)
                    search_str=listen_command()
        else:
            say_text('введите ваш запрос',mute) #query - like search
            search_str=listen_command()
        search_in_internet(search_str)

    elif c_type == "l":

        if ("вкл" in c_string):
            os.startfile(r'lamp_on.bat')
            say_text("лампа включена", mute)
        elif ("выкл" in c_string):
            os.startfile(r'lamp_off.bat')
            say_text("лампа выключена", mute)
        else: say_text("ничего не удалось", mute)
        
    elif c_type == "w":
        
        say_text("не забудьте в конец добавить слова 'конЕц заметки'",mute)
        write_note(print_speach)
        say_text("готово")
        
    elif c_type == "ca":
            
        equation_rez=get_equation(c_string)
        say_text(str(equation_rez),mute)

    elif c_type == "t":
        timer_start_list.append(time.time())
        timer_list.append(time_for_timer(c_string,mute))
        timer_file(timer_start_list,timer_list)
        
    elif c_type == "h":
        
        os.startfile(r'comand_list.txt')

    elif c_type == "fi":

        say_text("какое название у файла",mute)
        file_looking_for = listen_command() #то что ищем

        file_looking_for = make_true_file_name(file_looking_for)
        
        say_text("какое расширение",mute)
        type_of_file = listen_command()

        type_file=comand_type(type_of_file,types_flag_list, types_tag_list)
        
        if type_file =="no":
            say_text("такого типа я не знаю",mute)
            
        else:
            say_text("на каком диске ищем",mute)
            disk = listen_command()
            disk=disk.strip()
            if type_file != "dir":
                file_looking_for=file_looking_for+"."+str(type_file)
            
            print(file_looking_for)

            disk=make_true_disk(disk)
            if disk == "fail":
                continue
        
            say_text("уже приступаю, но это может занять некоторое время", mute)
    
            succes=find_files(file_looking_for,disk,mute)
            if succes == 1:
                find_file_txt=open('abc.txt','r',encoding='cp866')
                full_find_file_list=get_full_comand_list(find_file_txt)
            ######################
                count_find_files=len(full_find_file_list)-1
                if count_find_files == 0:
                    say_text("Ничего не найдено",mute)
                else:
                    
                    if count_find_files==1:
                        text_to_say=" файл"
                    elif (count_find_files>1) and (count_find_files<5):
                        text_to_say=" файла"
                    else:
                        text_to_say=" файлов"
                    text_to_say="я нашла "+str(count_find_files)+text_to_say
                    k=0
                    say_text(text_to_say,mute)
                    while k<count_find_files:
                        print(str(k+1)+" "+full_find_file_list[k])
                        k=k+1
                    
                    say_text("хотите открыть файл?", mute)
                    yn=listen_command()
                    if (yn[0]=="д") or (yn[0]=="х"):
                        number_file=1
                        if count_find_files > 1:
                            say_text("под каким номером нужный файл?",mute)
                            number_file=listen_command()
                            while (int(number_file)<1) or (int(number_file)>count_find_files):
                                say_text("неверный номер,попробуйте еще раз или скажите 'выйти'",mute)
                                number_file=listen_command()
                                if "выйти" in number_file:
                                    continue
                        open_find_files(full_find_file_list,int(number_file))
                    else:say_text("ну ок",mute)
                find_file_txt.close()
                

    elif c_type =="m":
            start_param_file=open('start_param.txt','w')
            first_space=c_string.find(' ')
            type_mod=c_string[first_space:len(c_string)]
            type_mod=type_mod.lower()
            type_mod=type_mod.strip()
            
            if type_mod == "звук":
                if mute == 0:
                    mute = 1
                    say_text("молчу", 0)
                    
                else:
                    mute = 0
                    say_text("я снова тут", mute)
                
            elif (type_mod == "подтверждения") or (type_mod == "подтверждение"):
                if yes_no == 0:
                    yes_no = 1
                    say_text("режим подтверждения включен", mute)
                    
                else:
                    yes_no = 0
                    say_text("режим подтверждения выключен", mute)
            elif ("голос" in type_mod):
                print_speach = "speach"
                say_text("Я вас снова слышу, можете говорить",mute)
            elif ("текст" in type_mod):
                print_speach = "print"
                say_text("Теперь я вас не слышу, пишите всё ручками",mute)
            else: say_text("Ничего не произошло, неверный режим работы", mute)
            start_param_file.write(curent_path_for_file+'\n')
            start_param_file.write(str(yes_no)+'\n')
            start_param_file.write(str(mute)+'\n')
            start_param_file.write(print_speach)    
            start_param_file.close()        
                    
        
    else:
        c_target =comand_target(c_string,adres_flag_list,adres_tag_list)
        
        while c_target == "no":
            
            target_list(c_string,c_type,mute)
            say_text("Хотите ввести цель?",mute)
            only_target_yn = listen_command()
            
            if (only_target_yn[0] == "y") or (only_target_yn[0] == "д"):
                say_text("Введите вашу цель")
                c_target = listen_command()
                c_target =comand_target(c_target,adres_flag_list,adres_tag_list)
            else:
                say_text("Как хотите",mute)
                c_type = "no"
                c_target = comand_flag_list[0]
                continue
            
        c_last=c_type
        if c_type == "o":
            
            #c_target = comand_target(c_target,adres_flag_list,adres_tag_list)
            open_target(c_target,adres_list,adres_flag_list)
            say_text("Сделано",mute)
            
        elif c_type =="c":

            close_target(c_target,close_adres,close_adres_flag_list)
            say_text("Сделано",mute)


             
        
         
        
   
    
    
