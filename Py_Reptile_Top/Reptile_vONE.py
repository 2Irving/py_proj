import requests
from bs4 import BeautifulSoup
import lxml
import datetime

## 设置请求头 可以在网页检查-网络获取
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

#分析网页代码找到结点
print("Analyzing web,please wait...")
start_time = datetime.datetime.now()
# 获取网站源代码
response = requests.get(url='https://tophub.today/',headers=headers) 
# 创建BeautifulSoup对象并指定解析器
soup = BeautifulSoup(response.text, 'lxml') 
# 解析时间
end_time = datetime.datetime.now()
print('Web_Analyze_Time = ', (end_time - start_time).seconds,'s')

def GetTop_UsingNode(topic_Name = "weibo",Link_Display = 0):
    '''链接代码解析提取
    topic_Name:
    Link_Display:链接显示
    '''
    Node = Select_module(topic_Name)

    # 找到模块 例:微博node-1
    div = soup.find('div',id=Node)
    # 模块-名称
    span_name = div.find('span').text
    # 模块-内容
    div =  div.find(class_="cc-cd-cb-l nano-content")
    print(span_name+': '+str(datetime.datetime.now()))

    rank=1
    for a_block in div.find_all('a'):
        # 查找热榜内容
        title = a_block.find(class_='t') 
        print(str(rank)+'\t'+title.text)
        if(Link_Display):# 打印话题链接
            link = a_block.get('href')  
            print('\t' + link + '\n')
        rank += 1

def Select_module(topic_Name):
    '''
    用户输入模块命跳转
    '''
    match topic_Name:
        case "weibo":   
            node =  "node-1" 
        case "zhihu":   
            node =  "node-6"
        case "sspai":
            node = "node-137"
        case "ithome":  
            node =  "node-119"
        case "github":  
            node =  "node-54"
        case "52pojie":
            node =  "node-68"
        case "36ke":
            node =  "node-11"
        case "smzdm":
            node =  "node-167"

        case _:
            node =  "node-1"

    return node

'''
    zhihu   github  weibo    sspai 
    
    ithome  36ke    smzdm    52pojie
'''
if __name__=='__main__':
    while(1):
        topic=input("please inpt topic_name:")
        GetTop_UsingNode(topic_Name = topic,Link_Display = 1)
