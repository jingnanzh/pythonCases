# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=23

'''
    选择要爬取故事的网站
    爬取网页内容
    提取网页中故事主体内容
    发送邮件
'''


# 下面的这段代码用来构建爬取函数，读入url，返回url中的内容。
import requests
def getHTMLText(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',}
    try:
        r=requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

# 利用下面这段代码取出一个30以内的随机数，决定幸运小故事从第几页产生，
# 将得到的随机数结果存放在page_num这个变量中。

import random
page_num = random.randint(1,30)
print('从第{}页取故事...'.format(page_num))

# +加号在Python中不仅可以实现数字加法，还能完成字符串的拼接工作，这样一来就能轻松得到url了：

if page_num==1:
    url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index.html'
else:
    url = 'http://www.tom61.com/ertongwenxue/shuiqiangushi/index_'+str(page_num)+'.html'
print("将要爬取：", url)

html=getHTMLText(url)
# print(html)

# 对获得的网页内容进行处理，这里使用到BeatifulSoup4模块，它的主要的功能也是解析和提取html数据。
# 下面这段代码使用BeautifulSoup解析html内容，将链接放入列表urllist中。

import bs4
base_url='http://www.tom61.com/'
soup=bs4.BeautifulSoup(html,'lxml')
txt_box=soup.find('dl',attrs={'class':'txt_box'})
a_tags=txt_box.find_all('a')
urllist=[]
for link in a_tags:
    urllist.append(base_url+link.get('href'))
print('获取链接列表：', urllist)

# 随机取出一个作为今晚发送给Gakki的幸运小故事～
story_item = random.choice(urllist)
print(story_item)

# 调用getHTMLText()爬取该网页内容：
html=getHTMLText(story_item)
# print("html",html)

# 接下来对网页内容进行处理，将故事主体内容提取出来，存储在contents中。
text=[]
soup=bs4.BeautifulSoup(html,'lxml')
tags=soup.find('div',class_='t_news_txt')
for i in tags.findAll('p'):
    text.append(i.text)
contents =  "\n".join(text)
print(contents)


# 照例导入邮件处理模块，以contents为内容发送邮件给女盆友就大功告成！
import zmail
# 使用邮件账户名和密码登录服务器
server = zmail.server('xiaoxiang@gmail.com', '？？')
mail = {
    'subject': '睡前小故事',  # 邮件的标题
    'content_text': contents,  # 邮件的文字内容
}
# 发送邮件
ret = server.send_mail(['lisashi3000@gmail.com'], mail)
print('发送结果：', ret)