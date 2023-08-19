import msvcrt
import json
TXTPath = './KSLSH1.txt'
NotePath ='./BookNote.json'
#打开并且读取json数据
def read_json(path):
    with open(path,'r') as fnote:
        params = json.load(fnote)
    return params

#打开并且保存json参数
def write_json(path,params):
    with open(path, 'w') as f:
        json.dump(params,f,indent=2)

#打开txt文件
ftext = open(TXTPath, encoding='utf8')
lines = ftext.readlines()
#读取json书签
params = read_json(NotePath)
#判断是否同一本书，同一本下才能读取书签
bookname = params["Book_Name"]
if(bookname == TXTPath[2:]):
    i=params["Note_Line"]
else:
    params["Book_Name"] = TXTPath[2:]
    write_json(NotePath,params)
    i=1

print(lines[i])
while(1):
    if msvcrt.kbhit():
        #判断ESC
        if msvcrt.getch() != b'\x1b':
            #skip all empty line
            while(i<len(lines)-1):
                if(lines[i]!='\n'):
                    break
                else:
                    i += 1 

            if(lines[i]!='\n'):
                print(lines[i])
                params["Note_Line"] = i
                i += 1
            else:
                print("END PAGE")
                params["Note_Line"] = 1
                write_json(NotePath,params)
                print("note start line OK")
                break   
        else:
            #note line to json 
            write_json(NotePath,params)
            print("note line "+str(i-1)+" OK ")
            break;
#json文件保存数据    
    