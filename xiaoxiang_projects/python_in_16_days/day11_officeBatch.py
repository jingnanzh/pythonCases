# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=9

'''
    1. 自动把文件放入文件名后缀为名的folder
    2. 批量自动发送邮件


'''


import os
import shutil

# path= 'C:/Users/Maggie/Dropbox/Camera Uploads/'
# files=os.listdir(path)
# for f in files:
#     folder_name=path+f.split('.')[-1]
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#         shutil.move(f,folder_name)
#     else:
#         shutil.move(f,folder_name)

import pandas as pd
df = pd.read_excel(r'C:\Users\Maggie\Desktop\Udemy-desktop\xiaoxiangxueyuan\Python认知打卡课课程资料包\资料代码整理\办公自动化\司庆自动邮件发送\员工信息.xlsx')
# print(df.head())

# 把准备好的三种不同奖项放置在列表中。
gift = ['一个月奶茶券', '运动手环+3天带薪年假抽奖名额', 'kindle阅读器+特斯拉抽奖名额']

# 定义一个方法，实现的功能是计算入职天数，再用入职天数/365取整得到入职年限，匹配对应的礼物等级。
from datetime import datetime
birthday = datetime(2019, 11, 11)
def get_gift_type(time):
    # 计算时间差
    delta = birthday - time
    delta_year = delta.days // 365
    # 根据相差年份数返回奖品等级
    if delta_year == 0:
        return delta.days, 0
    elif delta_year < 3:
        return delta.days, 1
    else:
        return delta.days, 2

# 下面来创建邮件的模版信息，姓名，入职天数，奖品的内容用大括号{}代替。
msg = '''
亲爱的{}：
感谢您在过去{}个日日夜夜，为了工作孜孜不倦地奋斗。值公司周年之际，我谨代表公司全体，对你的付出表达诚挚的谢意。
在这特殊的日子，送上一份小小礼物：{}，聊表心意。
期望在未来的日子里，我们继续携手共进，再创辉煌！
   此致
敬礼！
董事长办公室
'''

# Python内置的smtplib和email模块可以帮我们实现邮件的构造和发送功能。
# 定义一个名为send_email的方法实现发送邮件的发送效果，邮件主题为‘感谢一路有你’：

import smtplib
from email.utils import formataddr
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
def Send_email(sender,password,content,receive):
    receivers = receive
    msg = MIMEMultipart()
    msg["Subject"] = "感谢一路有你"
    msg["From"] = sender
    if len(receivers)>1:
        msg["To"] = ",".join(receivers)
    else:
        msg["To"] = receivers[0]
    part = MIMEText(content,_charset="UTF-8")
    msg.attach(part)
    try:
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.ehlo()
        smtp.login(sender,password)
        smtp.sendmail(sender,receivers,
                     msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error, 发送失败", e)
    finally:
        smtp.close()

# sender = "covid2020@gmail.com"
# password = "1234567"
# content = "测试：土豆土豆，我是地瓜，收到请回答！"
# receive = ["xianmaoyuan@xiaoxiangxueyuan.com"]
# Send_email(sender, password, content, receive)

def handle_row(row):
    # 构建发送消息
    name = row['姓名']
    email = row['邮箱']
    delta_days, gift_type = get_gift_type(row['入职时间'])
    sent_msg = msg.format(name, delta_days, gift[gift_type])
    print(sent_msg)
    # 调用Send_email()发送邮件
    sender = "xianmaoyuan@xiaoxiangxueyuan.com" #验证gmail时需要turn on Less secure app access： https://myaccount.google.com/u/1/lesssecureapps?pli=1&rapt=AEjHL4O3LYw-hfy0nl0mmajUDIQBk-RF__KXf0fQ1nWvgcC_grj6872iFsXWAcZ_2_YQfkJHuLx_eEjlIrcYIWgq6sCtrmK2Mw
    password = "1234567"
    print('发邮件给{}...'.format(name))
    #     receive = ['xianmaoyuan@xiaoxiangxueyuan.com']
    receive = [email]
    Send_email(sender, password, sent_msg, receive)
    return 'Done'

# 最后一步，按下启动键，让程序按行读取表格中的数据，坐等收邮件咯。
# Function to apply to each column or row. axis : {0 or 'index', 1 or 'columns'}, default 0
df.apply(handle_row, axis=1)