import requests
from bs4 import BeautifulSoup
import lxml
import datetime

# 源代码解析放置全局，如果放在函数内则会重复网页解析，增加耗时
url = 'https://tophub.today/'
## 设置请求头 可以在网页检查-网络获取
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
print("Analyzing web,please wait...")
start_time = datetime.datetime.now()
## 获取网站源代码
response = requests.get(url=url,headers=headers) 
## 创建BeautifulSoup对象并指定解析器
soup = BeautifulSoup(response.text, 'lxml') 
## 获取解析时间
end_time = datetime.datetime.now()
print('Web_Analyze_Time = ', (end_time - start_time).seconds,'s')

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
        case "sspai":
            node = "node-33861"
            node_str = "少数派"
        case "ithome":  
            node =  "node-119"
            node_str = "IT之家"
        case "github":  
            node =  "node-54"
            node_str = "Github热榜"
        case "52pojie":
            node =  "node-68"
            node_str = "吾爱破解"
        case "36ke":
            node =  "node-11"
            node_str = "36氪"
        case "smzdm":
            node =  "node-167"
            node_str = "什么值得买"
        case _:     
            node =  "node-1"
            node_str = "微博热搜"

    return node,node_str
#网页代码解析提取
def GetTop_UsingNode(Web_Name = "weibo",Link_Display = 0):
    
    Node,Node_str = Select_module(Web_Name)
    # 找到模块节点 例:微博node-1
    div = soup.find('div',id=Node)
    # 找到模块节点-内容节点
    div =  div.find(class_="cc-cd-cb-l nano-content")
    
    print(Node_str+': '+str(datetime.datetime.now()))
    rank=1
    for a_block in div.find_all('a'):
        # 查找热榜内容
        title = a_block.find(class_='t') 
        print(str(rank)+'\t'+title.text)
        # Link_Display：连接显示选项
        if(Link_Display):
            # 提取href属性并且打印
            link = a_block.get('href')  
            print('\t'+link)
        rank += 1
    #查询间的隔行
    print('\n')
    
#   weibo   zhihu   36ke    ithome  52pojie   github    smzdm   sspai
while(1):
    web=input("please inpt web_name:")
    GetTop_UsingNode(Web_Name = web)
# GetTop_UsingNode(Web_Name = "weibo")
