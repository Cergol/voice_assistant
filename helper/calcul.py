from PIL import Image
 
im1 = Image.open('451116c6-17a8-452a-b7b8-ebff1b6a2bed.jfif')
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
