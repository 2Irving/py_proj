import msvcrt
import json
TXTPath = './KSLSH1.txt'
NotePath ='./BookNote.json'
#打开txt文件
ftext = open(TXTPath, encoding='utf8')

#打开并且读取json数据
def read_json(path):
    with open(path,'r') as fnote:
        params = json.load(fnote)
    return params

#打开并且保存json参数
def write_json(path,params):
    with open(path, 'w') as f:
        json.dump(params,f,indent=2)


params = read_json(NotePath)
#for i,line in enumerate(ftext):
lines = ftext.readlines()
#读取书签行 
i=params["Note_Line"]
print(lines[i])
while(1):
    if msvcrt.kbhit():
        if msvcrt.getch() != b'\x1b':
            if(lines[i]!='\n'):
                print(lines[i])
                params["Note_Line"] = i
            i = i+1
        else:
            write_json(NotePath,params)
            print("note OK")
            break;
#json文件保存数据    
    
