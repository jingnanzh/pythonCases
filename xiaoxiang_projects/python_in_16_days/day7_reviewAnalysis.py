# Practice python in 16 days
# https://clock.kaiwenba.com/clock/course?sn=ExhvY&course_id=12#

'''
 分析入海这首歌的评论
  自动替换信息，批量生成邀请函文件。
'''
# 导入包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from collections import Counter
from pyecharts.charts import Bar, Pie, Line, WordCloud, Page
from pyecharts import options as opts
from pyecharts.globals import SymbolType

# 读入数据
df = pd.read_excel('C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/Python认知打卡课课程资料包/资料代码整理/数据分析/毛不易《入海》评论数据分析/B站评论数据-入海5.23.xlsx')
df.head() #first 5 rows
print(df.shape) #(19099, 8)

# drop 重复值
df = df.drop_duplicates()
print(df.shape) #说明原数据中没有完全相同的数据出现。

df.info() #查看数据摘要，包括所有列的列表，非空值的数量以及数据类型：

# 接下来把时间戳转换为我们常用的表示形式：
df['评论时间'] = pd.to_datetime(df['评论时间'], unit='s')
df['评论时间'] = df['评论时间'].dt.tz_localize('utc').dt.tz_convert('Asia/Shanghai').dt.strftime('%Y-%m-%d %H:%M:%S').astype(str)
print(df.head()) #时间已经改变格式

# 总体评分分布
# ‘用户性别’可选‘男’，‘女’或‘保密’，把三个内容对应的数量统计出来，再把‘保密’一栏的数据删除不做统计就可以啦。
# 使用value_counts方法统计‘性别’一列的不同数据总和，再使用drop方法把‘保密’一栏删除，最后打印得到结果
sex_num = df['性别'].value_counts()
sex_num.drop('保密', inplace=True)
print(sex_num) #男性观众4537人，女性观众3759人

# 绘制饼图
data_pair =  [list(z) for z in zip(sex_num.index.tolist(), sex_num.values.tolist())]
# 绘制饼图
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie1.add('', data_pair, radius=['35%', '60%'])
pie1.set_global_opts(title_opts=opts.TitleOpts(title='评论用户性别占比'),
                     legend_opts=opts.LegendOpts(orient='vertical', pos_top='15%', pos_left='2%'))
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
pie1.set_colors(['#EF9050', '#3B7BA9', '#6FB27C'])
pie1.render() #generate a file:///C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/pythonCases/xiaoxiang_projects/python_in_16_days/render.html

# 这次我们需要操作的是‘设备’这一列的数据。
device_num = df.设备.value_counts(ascending=True)
print(device_num)

# 绘制一个柱状图来展示一下
# 柱形图
bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar1.add_xaxis(device_num.index.tolist())
bar1.add_yaxis('', device_num.values.tolist(),
               label_opts=opts.LabelOpts(position='right'))
bar1.set_global_opts(title_opts=opts.TitleOpts(title='评论客户端分布'),
                     visualmap_opts=opts.VisualMapOpts(max_=3000))
bar1.reversal_axis()
bar1.render() # replace the file:///C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/pythonCases/xiaoxiang_projects/python_in_16_days/render.html

# B站根据用户的参与程度还给用户划分了Lv0-Lv6几个等级，数字越大，等级越高。
# 我们统计一下观看《入海》视频的用户等级分布：
level_num = df.等级.value_counts()
print(level_num)

# 画一个饼图呈现结果
data_pair2 =  [list(z) for z in zip(['LV' + i for i in level_num.index.astype('str').tolist()] , level_num.values.tolist())]
# 绘制饼图
pie2 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie2.add('', data_pair=data_pair2, radius=['35%', '60%'])
pie2.set_global_opts(title_opts=opts.TitleOpts(title='评论用户等级分布'),
                     legend_opts=opts.LegendOpts(orient='vertical', pos_top='15%', pos_left='2%'))
pie2.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}({d}%)"))
pie2.set_colors(['#EF9050', '#3B7BA9', '#6FB27C', '#FFAF34'])
pie2.render() # replace the file:///C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/pythonCases/xiaoxiang_projects/python_in_16_days/render.html

# 看评论量走势和时间的关系。
df['时间'] = df.评论时间.str.split('-').str[1] + '-' + df.评论时间.str.split('-').str[2]
# print(df.head())

# 下面用冒号：分割‘时间’这栏的数据就能得到我们需要的日期和小时的数据
df['时间'] = df.时间.str.split(':').str[0]
time_num = df.时间.value_counts().sort_index()
time_num[:5]
print(time_num[:5])


# 用下面两行代码设定横坐标为时间，纵坐标表示评论数量。
# 产生数据
x1_line1 = time_num.index.values.astype('str').tolist()
y1_line1 = time_num.values.tolist()

# 绘制面积图
line1 = Line(init_opts=opts.InitOpts(width='1350px', height='750px'))
line1.add_xaxis(x1_line1)
line1.add_yaxis('', y1_line1, areastyle_opts=opts.AreaStyleOpts(opacity=0.3),
                markpoint_opts=opts.MarkPointOpts(data=[
                    opts.MarkPointItem(type_='max', name='最大值')
                ]))
line1.set_global_opts(title_opts=opts.TitleOpts('各个时段评论人数'),
                      xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate='30'))
                     )
line1.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                      axisline_opts=opts.AxisLineOpts()
                     )
line1.render()  # replace the file:///C:/Users/Maggie/Desktop/Udemy-desktop/xiaoxiangxueyuan/pythonCases/xiaoxiang_projects/python_in_16_days/render.html
                # #从5月20日8:30发布MV后，评论数量逐渐上升，12点左右有一个快速增加，达到高峰。后续随着时间的推移，评论人数逐渐减少，趋于平缓。