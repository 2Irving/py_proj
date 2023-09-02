import json
import time
import keyboard
import chardet

TXTPath = './Books/RLJS.txt'
#TXTPath = './Books/KSLSH1.txt'
NotePath ='./BookNote.json'
#自定错误
class UsualError(BaseException):
    pass
class EncodingDetectError(BaseException):
    pass

#对txt的编码格式进行识别
def detect_encoding(text_file, min_confidence = 0.98, text_length = 1024):
    with open(text_file, 'rb') as text:
        result = chardet.detect(text.read(text_length))
    if result['confidence'] < min_confidence:
        raise EncodingDetectError('can not detect the text file encoding')
    return result['encoding']

#转换编码字符，用于open()
def translate_str_encoding(encoding):
    if(encoding == 'utf-8'):
        return 'utf8'
    elif(encoding == 'GB2312'):
        return 'gbk'
    else:
        raise UsualError('can not translate type')

#打开并且读取json数据
def read_json(path):
    with open(path,'r') as fnote:
        params = json.load(fnote)
    return params

#打开并且保存json参数
def write_json(path,params):
    with open(path, 'w') as f:
        json.dump(params,f,indent=2)

#识别文本编码并打开
ftext = open(TXTPath, encoding = translate_str_encoding(detect_encoding(TXTPath)))
lines = ftext.readlines()
#json查询书是否存在，并且读取书签，若不存在则创建书
params = read_json(NotePath)
books = params["Books"]
for book_index,Book in enumerate(books):
    if(Book['Book_Name'] == TXTPath[8:]):
        line_index=Book['Note_Line']
        break
    elif(book_index==len(books)-1):
        print("no this book ,add book to json")
        line_index = 0
        books.append({"Book_Name":TXTPath[8:],"Note_Line": 0})
        write_json(NotePath,params)
        break  
#预览一行 
print(lines[line_index])


while(1):
    if keyboard.is_pressed(' ') or keyboard.is_pressed('up'):
        time.sleep(0.2)
        #skip all empty line                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        while(line_index<len(lines)-1):
            if(lines[line_index]!='\n'):
                break
            else:
                line_index += 1 

        if(line_index<len(lines)-1):
            print(lines[line_index])
            books[book_index]["Note_Line"] = line_index
            line_index += 1
        else:
            print("END PAGE")
            books[book_index]["Note_Line"] = line_index
            write_json(NotePath,params)
            print("note start line OK")
            break   

    elif keyboard.is_pressed('esc'):
        #note line to json 
        write_json(NotePath,params)
        print("note line "+str(line_index-1)+" OK ")
        break;
#json文件保存数据    
    