import requests
from bs4 import BeautifulSoup
import lxml
import datetime

url = 'https://tophub.today/'
#设置请求头 可以在网页检查-网络获取
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

#自定义的选择模块
def Select_module(Web_Name):
    node =  ""
    node_str = ""
    match Web_Name:
        case "weibo":   
            node =  "node-1" 
            node_str = "微博热搜"
        case "zhihu":   
            node =  "node-6"
            node_str = "知乎热榜"
        case "github":  
            node =  "node-54"
            node_str = "Github热榜"
        case "wuaipojie":
            node =  "node-68"
            node_str = "吾爱破解"
        case _:     
            node =  "node-1"
            node_str = "微博热搜"

    return node,node_str
#网页代码解析提取
def GetTop_UsingNode(Web_Name = "weibo",LinkDisp = 0):
    start_time = datetime.datetime.now()
    Node,Node_str = Select_module(Web_Name)
    
    #获取网站源代码
    response = requests.get(url=url,headers=headers) 
    # 创建BeautifulSoup对象并指定解析器
    soup = BeautifulSoup(response.text, 'lxml') 
    # 找到模块节点 例:微博node-1
    div_weibo = soup.find('div',id=Node)
    # 找到模块节点-内容节点
    div_weibo =  div_weibo.find(class_="cc-cd-cb-l nano-content")
    
    print(Node_str+': '+str(datetime.datetime.now()))
    rank=1
    for a_block in div_weibo.find_all('a'):
        link = a_block.get('href')  # 提取href属性。
        title = a_block.find(class_='t') # 查找热榜内容
        print(str(rank)+'\t'+title.text)
        if(LinkDisp):
            print('\t'+link)
        rank += 1
    
    end_time = datetime.datetime.now()
    print('Cost_Time = ', (end_time - start_time).seconds,'s')

GetTop_UsingNode(Web_Name = "weibo")