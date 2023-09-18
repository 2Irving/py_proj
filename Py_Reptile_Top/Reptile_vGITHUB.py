import requests
from bs4 import BeautifulSoup
import lxml
import datetime
'''
由于今日热板的板块没办法爬到github月榜，故特开此份，但是链接是索引太难看
'''
node_github_today = "https://tophub.today/n/rYqoXQ8vOD"
#node_github_weekly = "https://tophub.today/n/Q1Vd5xKv85"
node_github_monthly = "https://tophub.today/n/n3moBYVeN5"

node_weibo = "https://tophub.today/n/KqndgxeLl9"

node_zhihu = "https://tophub.today/n/mproPpoq6O"

node_sspai = "https://tophub.today/n/Y2KeDGQdNP"

node_ithome = "https://tophub.today/n/74Kvx59dkx"

node_juejin = "https://tophub.today/n/QaqeEaVe9R"

node_wuaipojie = "https://tophub.today/n/NKGoRAzel6"

node_smzdm = "https://tophub.today/n/K7GdagpoQy"

node_3dm = "https://tophub.today/n/YqoXQR0vOD"

## 设置请求头 可以在网页检查-网络获取
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


def GetTop_UsingNode(Link = node_weibo,Link_Display = 0):
    ''' 链接代码解析提取
    analyz web code and get topic information
    Link:网页链接
    Link_Display:是否显示话题链接
    ''' 

    print("Analyzing web,please wait...")
    start_time = datetime.datetime.now()
    ## 获取网站源代码
    response = requests.get(url=Link,headers=headers) 
    ## 创建BeautifulSoup对象并指定解析器
    soup = BeautifulSoup(response.text, 'lxml') 
    ## 获取解析时间
    end_time = datetime.datetime.now()
    print('Web_Analyze_Time = ', (end_time - start_time).seconds,'s')

    # 找到版名以便打印
    topic = soup.find('div',class_='Xc-ec-L b-L')
    print(topic.text+': '+str(datetime.datetime.now()))
    # 找到第一个匹配块
    table = soup.find('table')
    rank=1
    #查找各个标题块
    for a_block in table.find_all('a'): 
        #跳过所有非标题块
        if(a_block.get('class') == ['collect-a']):
            continue

        print(str(rank)+'\t'+a_block.text+'\n')

        if(Link_Display):
            link = a_block.get('href')  
            print('https://tophub.today'+link+'\n')
        rank += 1
        
    
if __name__=='__main__':
    while(1):
        web_name=input("please inpt web_name:")
        match web_name:
            case 'weibo':
                link =  node_weibo 
            case 'zhihu':
                link =  node_zhihu
            case 'sspai':
                link =  node_sspai
            case 'ithome':
                link =  node_ithome
            case 'juejin':
                link =  node_juejin
            case 'wuaipojie':
                link =  node_wuaipojie
            case 'smzdm':
                link =  node_smzdm
            case '3dm':
                link =  node_3dm

            case 'github_today':
                link =  node_github_today
            case 'github_monthly':
                link =  node_github_monthly
            case _:
                link =  node_weibo 
        GetTop_UsingNode(Link = link,Link_Display = 1)